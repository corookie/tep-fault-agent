"""规则解析和排序的语义边界，不把评测分数当成单元测试目标。"""
import unittest
from query_rules import parse_query, priority
from retrieve_chunks import RuleIndex, TextIndex


class QueryRulesTests(unittest.TestCase):
    def units(self,q):return parse_query(q)['primary_units']

    def test_typed_numbers_are_distinct(self):
        self.assertEqual(self.units('故障7是什么'),['FAULT-IDV07'])
        self.assertEqual(self.units('X7是什么'),['VAR-X07'])
        self.assertEqual(self.units('流7去哪'),['STREAM-07'])
        self.assertEqual(self.units('ＸＭＶ（４）和 xmeas(4)'),['VAR-X04','VAR-X45'])
        self.assertEqual(self.units('第十五个故障与第七号故障'),['FAULT-IDV15','FAULT-IDV07'])
        self.assertEqual(self.units('7号故障'),['FAULT-IDV07'])

    def test_quantities_are_not_entities(self):
        for q in ['21种故障','21个变量','52列数据','故障21种都测试了吗']:
            self.assertEqual(self.units(q),[])
        a=parse_query('这21种故障我们都测过了吗？')
        self.assertEqual(a['intent'],'validation_scope')
        self.assertEqual(a['quantities'][0]['number'],21)
        self.assertNotIn('21',a['retrieval_query'])

    def test_ranges_aliases_and_case(self):
        self.assertEqual(self.units('x23至x25'),['VAR-X23','VAR-X24','VAR-X25'])
        self.assertEqual(self.units('idv(3)–IDV(5)'),['FAULT-IDV03','FAULT-IDV04','FAULT-IDV05'])
        self.assertEqual(self.units('流股四到六'),['STREAM-04','STREAM-05','STREAM-06'])
        self.assertEqual(self.units('ax45foo与MyIDV7'),[])

    def test_invalid_unknown_and_ambiguous_not_guessed(self):
        for q in ['IDV(99)','X0','X99','流99','XMV(13)','X5-X2']:
            a=parse_query(q)
            self.assertFalse(a['primary_units'])
            self.assertTrue(a['issues'])
        a=parse_query('XMV(12)是什么？')
        self.assertFalse(a['primary_units'])
        self.assertEqual(a['intent'],'data_schema')
        self.assertNotIn('VAR-X53',str(a))
        a=parse_query('那15呢？')
        self.assertTrue(a['ambiguous_number'])
        self.assertFalse(a['primary_units'])
        self.assertFalse(a['context_used'])

    def test_general_topics_do_not_force_domain_routes(self):
        for q in ['Windows安装测试过吗','明天去哪里玩','这21个软件都测过了吗']:
            self.assertEqual(parse_query(q)['intent'],'general')

    def test_lookup_comparison_flow_and_mechanism(self):
        self.assertEqual(parse_query('X4和X45有什么区别')['intent'],'comparison')
        self.assertEqual(parse_query('流4直接进反应器吗')['intent'],'process_topology')
        self.assertEqual(parse_query('为什么X23-X28相加不是100')['intent'],'composition_sum')
        self.assertEqual(parse_query('故障7按什么顺序传播')['intent'],'fault_mechanism')

    def test_primary_unit_beats_incidental_mention(self):
        p=parse_query('故障10是什么')
        direct={'unit_id':'FAULT-IDV10','kind':'fault','entities':[]}
        incidental={'unit_id':'FAULT-IDV21','kind':'fault','entities':['IDV(10)']}
        self.assertGreater(priority(direct,p)[0],priority(incidental,p)[0])

    def test_named_equipment_and_numbered_subjects(self):
        for name,unit in [('反应器','EQUIP-REACTOR'),('冷凝器','EQUIP-CONDENSER'),
                          ('气液分离器','EQUIP-SEPARATOR'),('循环压缩机','EQUIP-COMPRESSOR'),
                          ('汽提塔','EQUIP-STRIPPER'),('stripper','EQUIP-STRIPPER')]:
            with self.subTest(name=name):
                self.assertEqual(self.units(name+'有什么作用？'),[unit])
        self.assertEqual(self.units('X22是汽提塔温度吗？'),['VAR-X22'])
        self.assertEqual(self.units('流4进入反应器吗？'),['STREAM-04'])
        self.assertEqual(set(self.units('冷凝器和分离器的区别？')),
                         {'EQUIP-CONDENSER','EQUIP-SEPARATOR'})


class RuleSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index=RuleIndex()
        cls.baseline=TextIndex()

    def test_queries_locate_primary_units(self):
        for q,expected in [('故障三的定义','FAULT-IDV03'),('流股四的出口','STREAM-04'),
                           ('xmeas(22)是什么','VAR-X22'),('XMV(11)是什么','VAR-X52')]:
            self.assertEqual(self.index.search(q,1)[0]['unit_id'],expected)
        self.assertEqual({h['unit_id'] for h in self.index.search('X4与X45有什么区别',2)}, {'VAR-X04','VAR-X45'})

    def test_invalid_does_not_return_a_nearby_number(self):
        self.assertEqual(self.index.search('IDV(99)是什么'),[])

    def test_fallback_is_unchanged_for_unrecognized_question(self):
        q='Windows 怎么安装 Ubuntu？'
        for method in [self.index.search,self.baseline.search]:
            self.assertEqual(method(q,min_score=.16),[])
        self.assertEqual([h['chunk_id'] for h in self.index.search(q)],
                         [h['chunk_id'] for h in self.baseline.search(q)])

    def test_score_is_not_disguised_as_rule_bonus(self):
        hits=self.index.search('这21种故障我们都测过了吗')
        self.assertEqual(hits[0]['unit_id'],'DATA-FILES')
        self.assertEqual(hits[0]['priority'],1)
        self.assertTrue(0<hits[0]['score']<.16)
        self.assertIn('rank_reason',hits[0])


if __name__=='__main__':unittest.main()
