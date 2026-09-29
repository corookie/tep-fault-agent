"""离线检索索引的完整性、持久化与评测计分检查。"""
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from retrieve_chunks import BASE, TextIndex, build_index, document_text, evidence_coverage, evaluate, normalize


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.chunks=self.root/'chunks.jsonl'
        self.manifest=self.root/'manifest.json'
        self.chunks.write_bytes((BASE/'knowledge_build/chunks.jsonl').read_bytes())
        self.manifest.write_bytes((BASE/'knowledge_build/manifest.json').read_bytes())
        self.indexdir=self.root/'index'
        build_index(self.chunks,self.manifest,self.indexdir)
        self.index=TextIndex(self.indexdir)

    def test_saved_index_matches_fresh_computation(self):
        v=TfidfVectorizer(analyzer='char',ngram_range=(2,3),lowercase=True)
        matrix=v.fit_transform([document_text(c) for c in self.index.chunks])
        query='IDV(7) 的压力传感器是 X4 吗？'
        expected=cosine_similarity(v.transform([normalize(query)]),matrix)[0]
        actual={h['chunk_id']:h['score'] for h in self.index.search(query,110)}
        for c,score in zip(self.index.chunks,expected):
            self.assertAlmostEqual(actual.get(c['chunk_id'],0),score,places=12)
        self.assertEqual(len(self.index.chunks),110)

    def test_queries_respect_threshold_and_validation(self):
        self.assertEqual(self.index.search('明天杭州会下雨吗？'),[])
        self.assertEqual(self.index.search('Windows 怎么安装 Ubuntu？',min_score=.16),[])
        allhits=self.index.search('IDV(7) 的压力传感器是 X4 吗？',110)
        filtered=self.index.search('IDV(7) 的压力传感器是 X4 吗？',3,.16)
        self.assertEqual([h['unit_id'] for h in filtered],[h['unit_id'] for h in allhits if h['score']>=.16][:3])
        for kwargs in [dict(query=''),dict(query='x',top_k=0),dict(query='x',min_score=-1)]:
            with self.assertRaises(ValueError):self.index.search(**kwargs)

    def test_bad_chunk_batch_not_indexed(self):
        self.chunks.write_text(self.chunks.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'指纹'):
            build_index(self.chunks,self.manifest,self.root/'bad')
        self.assertFalse((self.root/'bad/index.json').exists())

    def test_stale_index_rejected(self):
        self.chunks.write_text(self.chunks.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'过期'):TextIndex(self.indexdir)

    def test_mixed_matrix_batch_rejected(self):
        with (self.indexdir/'vectors.npz').open('ab') as f:f.write(b'changed')
        with self.assertRaisesRegex(ValueError,'损坏'):TextIndex(self.indexdir)

    def test_evidence_groups_are_not_just_any_hit(self):
        case={'required_evidence':[{'description':'a','any_of':['A','B']},{'description':'c','any_of':['C']}]}
        partial=evidence_coverage(case,[{'unit_id':'B'}])
        self.assertTrue(partial['any_relevant'])
        self.assertFalse(partial['complete'])
        self.assertEqual(partial['coverage'],.5)
        self.assertTrue(evidence_coverage(case,[{'unit_id':'A'},{'unit_id':'C'}])['complete'])

    def test_report_keeps_real_followup_and_no_fake_answer(self):
        report=evaluate(self.index,BASE/'evaluation/retrieval_cases.json',self.root/'report')
        row=next(r for r in report['results'] if r['id']=='Q15')
        self.assertEqual(row['query_used'],'那 15 呢？')
        self.assertFalse(row['context_used'])
        self.assertEqual(report['summary']['positive_count'],18)
        self.assertEqual(report['summary']['negative_count'],3)
        self.assertNotIn('answer',row)
        ids=[c['chunk_id'] for c in self.index.chunks]
        self.assertTrue(all(h['chunk_id'] in ids for r in report['results'] for h in r['hits']))

    def test_invalid_evidence_id_rejected(self):
        suite=json.loads((BASE/'evaluation/retrieval_cases.json').read_text())
        suite['cases'][0]['required_evidence'][0]['any_of']=['NONEXISTENT']
        path=self.root/'bad-cases.json';path.write_text(json.dumps(suite))
        with self.assertRaisesRegex(ValueError,'证据标签无效'):
            evaluate(self.index,path,self.root/'bad-report')

    def test_index_text_excludes_source_paths(self):
        self.assertEqual(normalize('查看 [故障定义](/Users/a/doc.md#s01)'),'查看 故障定义')
        for chunk in self.index.chunks:
            text=document_text(chunk)
            self.assertNotIn('/Users/rowen/',text)
            self.assertNotIn('https://',text)


if __name__=='__main__':unittest.main()
