"""验证领域证据保留、来源继承、异常文档拒绝以及可重复构建。"""
from pathlib import Path
import tempfile
import unittest

from chunk_knowledge import BASE, Piece, build, entities, split_prose


class ChunkKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chunks, cls.manifest = build(BASE/'TEP_SOURCE_MAP.md', BASE/'docs/knowledge_sources.json')
        cls.by_id = {c['unit_id']: c for c in cls.chunks}

    def test_domain_evidence_survives(self):
        fault = self.by_id['FAULT-IDV07']
        for text in ['压力下降', '没有该总管压力', 'X4 为流 4 流量', '不是压力', '不表示这些字段必然异常']:
            self.assertIn(text, fault['content'])
        self.assertEqual(fault['parts'], 1)
        self.assertIn('mol%', self.by_id['VAR-X24']['content'])
        self.assertIn('流 6', self.by_id['VAR-X24']['content'])
        self.assertIn('归一化', self.by_id['VAR-X45']['content'])
        self.assertIn('不属于原始', self.by_id['FAULT-IDV21']['content'])
        self.assertIn('Unknown', self.by_id['FAULT-IDV16']['content'])

    def test_corrections_sources_and_units_attached(self):
        x22 = self.by_id['VAR-X22']
        self.assertIn('论文表 2-1', x22['content'])
        self.assertIn('本手册采用的表述：分离器冷却水出口温度', x22['content'])
        self.assertIn('流 4 进料温度随机变化', self.by_id['FAULT-IDV10']['content'])
        self.assertIn('kscmh 表示千标准立方米/小时', self.by_id['VAR-X04']['content'])
        self.assertIn('table_header', [s['role'] for s in x22['provenance']['spans']])
        self.assertTrue(any(s.get('sha256') for s in x22['sources']))
        self.assertTrue(any(s['mentions'] for s in x22['sources']))
        self.assertNotIn('](#src-', x22['content'])

    def test_only_current_handbook_is_ingested(self):
        text='\n'.join(c['content'] for c in self.chunks)
        self.assertNotIn('```mermaid', text)
        self.assertNotIn('先看三个实际样例', text)
        self.assertNotIn('更改记录：', text)
        self.assertNotIn('RAG_KNOWLEDGE_GUIDE', text)

    def test_repeat_build_is_identical(self):
        again, manifest = build(BASE/'TEP_SOURCE_MAP.md', BASE/'docs/knowledge_sources.json')
        self.assertEqual(self.chunks, again)
        self.assertEqual(self.manifest, manifest)

    def test_broken_inputs_are_rejected(self):
        raw=(BASE/'TEP_SOURCE_MAP.md').read_text(encoding='utf-8')
        row=next(s for s in raw.splitlines(keepends=True) if s.startswith('| VAR-X04 |'))
        variants = [raw.replace(row,''), raw.replace(row,row+row),
                    raw.replace('| X4 | XMEAS(4) |','| X4 | XMEAS(3) |'),
                    raw.replace('### 6.3 ', '### 6.4 新主题\n\n新增内容\n\n### 6.3 '),
                    raw.replace('version: 1.0.0','version: 2.0.0',1),
                    raw.replace('[S03，文件头接口说明]', '[S99，文件头接口说明]')]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'input.md'
            for index,text in enumerate(variants):
                p.write_text(text,encoding='utf-8')
                with self.subTest(variant=index), self.assertRaises(ValueError):
                    build(p, BASE/'docs/knowledge_sources.json')

    def test_edited_fact_is_read_from_document(self):
        raw=(BASE/'TEP_SOURCE_MAP.md').read_text(encoding='utf-8')
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'input.md'
            p.write_text(raw.replace('A/C 混合进料总流量；流 4','A/C 混合进料总流量（核对标记）；流 4'),encoding='utf-8')
            chunks,_=build(p,BASE/'docs/knowledge_sources.json')
            new=next(c for c in chunks if c['unit_id']=='VAR-X04')
            self.assertIn('核对标记',new['content'])
            self.assertNotEqual(new['content_sha256'],self.by_id['VAR-X04']['content_sha256'])
            self.assertEqual(new['chunk_id'],self.by_id['VAR-X04']['chunk_id'])

    def test_long_prose_preserves_sentences_and_fences(self):
        sentences=['甲'*70+'。', '乙'*70+'。', '丙'*70+'。']
        parts=split_prose(Piece(''.join(sentences), 8, 8),100)
        self.assertEqual([p.text for p in parts],sentences)
        self.assertTrue(all(p.start==8 and p.end==8 for p in parts))
        fence='```mermaid\n'+'A --> B\n'*20+'```'
        parts=split_prose(Piece(fence,1,22),100)
        self.assertEqual(len(parts),1)
        self.assertEqual(parts[0].text,fence)
        table='| A | B |\n|---|---|\n'+'| 甲 | 乙 |\n'*20
        self.assertEqual(len(split_prose(Piece(table,1,22),100)),1)

    def test_entity_ranges(self):
        result=entities('X23–X28，IDV(4)/(11)，IDV(16)–(20)，流 4')
        for entity in ['X24','X27','IDV(11)','IDV(18)','STREAM-04']:
            self.assertIn(entity,result)

    def test_soft_limit_keeps_fault_atomic(self):
        chunks,manifest=build(BASE/'TEP_SOURCE_MAP.md',BASE/'docs/knowledge_sources.json',200)
        self.assertGreater(len(manifest['warnings']),0)
        for c in chunks:
            if c['kind']=='fault':
                self.assertEqual(c['parts'],1)
                self.assertIn('可观测性',c['content'])
                self.assertIn('解释边界',c['content'])


if __name__=='__main__':
    unittest.main()
