import unittest
import json
from html import unescape
import re
from diagnosis_graph import graph_data, matrix_svg, network_svg, render_graphs


def result(pairs, candidates=('X4',)):
    return {'variables':['X4','X7','X13','X45'], 'candidates':list(candidates),
            'edges':[{'source':s,'target':t,'selected':selected,'q_value':0.01,'improvement':0.2}
                     for s,t,selected in pairs]}


class GraphTests(unittest.TestCase):
    def test_matrix_column_is_source_and_row_is_target(self):
        data=graph_data(result([('X4','X7',True),('X7','X13',False)]))
        self.assertEqual(data['matrix'][1][0],1)
        self.assertEqual(data['matrix'][0][1],0)
        self.assertIsNone(data['matrix'][0][0])
        self.assertEqual(data['matrix'][2][1],0)

    def test_branch_paths_only_use_selected_edges(self):
        pairs=[('X4','X7',True),('X7','X13',True),('X4','X45',True),('X13','X45',False)]
        data=graph_data(result(pairs))
        self.assertEqual([p['nodes'] for p in data['paths']], [['X4','X45'],['X4','X7','X13']])
        allowed={(s,t) for s,t,keep in pairs if keep}
        for p in data['paths']:
            self.assertTrue(all(e in allowed for e in zip(p['nodes'],p['nodes'][1:])))
        self.assertFalse(data['feedback_groups'])

    def test_cycle_is_preserved_without_infinite_paths(self):
        data=graph_data(result([('X4','X7',True),('X7','X45',True),('X45','X7',True)]))
        self.assertEqual(data['feedback_groups'],[['X7','X45']])
        self.assertEqual(data['paths'][0]['termination'],'feedback')
        self.assertEqual(len(data['edges']),3)
        for p in data['paths']:self.assertEqual(len(p['nodes']),len(set(p['nodes'])))

    def test_no_forced_root_and_no_fabricated_path(self):
        self.assertFalse(graph_data(result([]))['paths'])
        r=result([('X7','X45',True),('X45','X7',True)],candidates=())
        data=graph_data(r)
        self.assertFalse(data['paths'])
        self.assertEqual(len(data['feedback_groups']),1)
        self.assertIn('不强行指定',render_graphs(r))

    def test_cap_is_reported_and_all_variables_still_present(self):
        data=graph_data(result([('X4','X7',True),('X4','X13',True),('X4','X45',True)]),max_paths=2)
        self.assertEqual(len(data['paths']),2)
        self.assertTrue(data['paths_truncated'])
        empty=graph_data(result([]))
        for v in empty['variables']:
            self.assertIn(v,network_svg(empty))
        self.assertEqual(len(empty['isolated']),4)

    def test_svg_is_valid_xml_and_includes_edge_evidence(self):
        from xml.etree import ElementTree
        data=graph_data(result([('X4','X7',True),('X7','X4',True)]))
        for svg in (matrix_svg(data),network_svg(data)):
            ElementTree.fromstring(svg)
        self.assertIn('q=0.01',network_svg(data))
        self.assertIn('stroke-dasharray',network_svg(data))

    def test_dashed_edges_require_a_direct_reverse_edge(self):
        from xml.etree import ElementTree
        three_way=result([('X4','X7',True),('X7','X13',True),('X13','X4',True)])
        data=graph_data(three_way)
        self.assertEqual(len(data['feedback_groups']),1)
        svg=ElementTree.fromstring(network_svg(data))
        edges=[node for node in svg.iter() if node.attrib.get('class')=='graph-edge']
        self.assertTrue(all('stroke-dasharray' not in edge.attrib for edge in edges))
        self.assertNotIn('虚线：变量间双向因果关系',network_svg(data))
        reciprocal=graph_data(result([('X4','X7',True),('X7','X4',True)]))
        svg=ElementTree.fromstring(network_svg(reciprocal))
        edges=[node for node in svg.iter() if node.attrib.get('class')=='graph-edge']
        self.assertTrue(all(edge.attrib.get('stroke-dasharray')=='6 4' for edge in edges))

    def test_path_cap_covers_different_roots(self):
        r=result([('X4','X7',True),('X4','X13',True),('X45','X7',True),('X45','X13',True)],
                 candidates=('X4','X45'))
        data=graph_data(r,max_paths=2)
        self.assertEqual([p['nodes'][0] for p in data['paths']], ['X4','X45'])
        self.assertTrue(data['paths_truncated'])
        full=graph_data(r)
        paths=[tuple(p['nodes']) for p in full['paths']]
        self.assertEqual(len(paths),len(set(paths)))
        self.assertFalse(full['paths_truncated'])

    def test_interaction_metadata_matches_graph_and_three_default_paths(self):
        r=result([('X4','X7',True),('X4','X13',True),('X45','X7',True),('X45','X13',True)],
                 candidates=('X4','X45'))
        html=render_graphs(r)
        before,after=html.split('<details class="more-paths">')
        self.assertEqual(before.count('class="path-option"'),3)
        self.assertEqual(after.count('class="path-option"'),1)
        encoded=re.findall('data-path-nodes="([^"]+)"',html)
        self.assertEqual([json.loads(unescape(p)) for p in encoded],
                         [p['nodes'] for p in graph_data(r)['paths']])
        from xml.etree import ElementTree
        svg=ElementTree.fromstring(network_svg(graph_data(r)))
        pairs={(node.attrib['data-source'],node.attrib['data-target'])
               for node in svg.iter() if node.attrib.get('class')=='graph-edge'}
        self.assertEqual(pairs,{(e['source'],e['target']) for e in r['edges']})
        self.assertNotIn('class="path-reset"',render_graphs(result([])))


if __name__=='__main__':unittest.main()
