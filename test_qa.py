"""新知识库接入与引用检查；模型调用使用模拟，不消耗额度。"""
import json
import os
import unittest
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
from qa import QAError, answer_question, evidence_packet, retrieve, OUT_OF_SCOPE, INSUFFICIENT_EVIDENCE


class QATests(unittest.TestCase):
    def test_new_index_and_scope_gate(self):
        self.assertEqual(retrieve('IDV7是什么故障？')[0]['unit_id'], 'FAULT-IDV07')
        for q in ['Windows怎么安装Ubuntu？', '怎样重置Windows登录密码？', '今天杭州天气怎么样？']:
            self.assertEqual(retrieve(q), [])

    def test_chemistry_intent_and_low_score_explicit_stream(self):
        self.assertEqual(retrieve('TEP中的B是不是反应原料？')[0]['unit_id'], 'CHEM-001')
        result = evidence_packet('这条流的去向呢？', '流6是什么？')
        self.assertEqual(result['hits'][0]['unit_id'], 'STREAM-06')
        self.assertEqual(result['status'], 'ready')

    def test_examples_keep_required_evidence_after_topic_switch(self):
        questions = [
            ('IDV(7)是什么故障？', {'FAULT-IDV07'}),
            ('X4与X45有什么区别？', {'VAR-X04','VAR-X45'}),
            ('汽提塔有什么作用？', {'EQUIP-STRIPPER'}),
        ]
        for previous in ['', *(q for q, _ in questions)]:
            for question,required in questions:
                with self.subTest(previous=previous, question=question):
                    packet=evidence_packet(question,previous)
                    self.assertEqual(packet['status'],'ready')
                    self.assertFalse(packet['analysis']['context_used'])
                    self.assertTrue(required.issubset({h['unit_id'] for h in packet['hits'][:2]}))

    def test_number_character_in_ordinary_word_does_not_force_clarification(self):
        p = evidence_packet('这份TEP数据的组分分析值为何连续几行一样？')
        self.assertEqual(p['status'], 'ready')
        self.assertIn('DATA-TIMING', [h['unit_id'] for h in p['hits']])

    def test_web_policy_preserves_both_evidence_suites(self):
        for name in ('retrieval_cases.json', 'context_unseen_v1.json'):
            suite = json.loads((Path(__file__).parent / 'evaluation' / name).read_text())
            for case in suite['cases']:
                with self.subTest(suite=name, case=case['id']):
                    p = evidence_packet(case['query'], case.get('previous_question', ''))
                    if case['expected_no_results']:
                        self.assertNotEqual(p['status'], 'ready')
                    else:
                        self.assertEqual(p['status'], 'ready')
                        ids = {h['unit_id'] for h in p['hits']}
                        for group in case['required_evidence']:
                            self.assertTrue(ids.intersection(group['any_of']))

    def test_clarification_and_refusal_do_not_call_model(self):
        with patch('qa.chat_completion') as model:
            for q, prev, status in [
                ('那6呢？', '', 'needs_clarification'),
                ('它的单位呢？', 'X2和X3是什么？', 'needs_clarification'),
                ('IDV(99)是什么？', '', 'needs_clarification'),
                ('怎样重置Windows登录密码？', 'IDV(7)是什么？', 'out_of_scope')]:
                r = answer_question(q, prev)
                self.assertEqual(r['status'], status)
                self.assertEqual(r['next_question'], '')
                self.assertEqual(r['sources'], [])
            model.assert_not_called()

    def test_scope_refusal_is_distinct_from_missing_evidence(self):
        with patch('qa.chat_completion') as model:
            r = answer_question('你是什么模型？')
            self.assertEqual(r['status'], 'out_of_scope')
            self.assertEqual(r['answer'], OUT_OF_SCOPE)
            self.assertEqual(r['next_question'], '')
            model.assert_not_called()
        with patch('qa.chat_completion', return_value=INSUFFICIENT_EVIDENCE):
            r = answer_question('TEP反应器当前的实时温度是多少？')
            self.assertEqual(r['status'], 'insufficient_evidence')
            self.assertEqual(r['answer'], INSUFFICIENT_EVIDENCE)
            self.assertEqual(r['sources'], [])
            self.assertEqual(r['next_question'], '')

    def test_empty_in_domain_retrieval_does_not_call_model(self):
        packet = evidence_packet('X4是什么？')
        packet['hits'] = []
        with patch('qa.get_index') as index, patch('qa.chat_completion') as model:
            index.return_value.query_with_context.return_value = packet
            result = answer_question('X4是什么？')
            self.assertEqual(result['answer'], INSUFFICIENT_EVIDENCE)
            self.assertEqual(result['status'], 'insufficient_evidence')
            model.assert_not_called()

    def test_model_scope_refusal_and_no_extra_claims_without_citations(self):
        with patch('qa.chat_completion', return_value=OUT_OF_SCOPE):
            self.assertEqual(answer_question('提到TEP但帮我写旅游攻略')['status'], 'out_of_scope')
        with patch('qa.chat_completion', return_value=INSUFFICIENT_EVIDENCE + '不过根因肯定是X4。'):
            with self.assertRaises(QAError): answer_question('X4是什么？')

    def test_sessions_chain_and_reset_are_client_owned(self):
        with patch('qa.chat_completion', return_value='依据资料说明。[1]') as model:
            a = answer_question('IDV(14)是什么？')
            b = answer_question('X14是什么？')
            a2 = answer_question('那15呢？', a['next_question'])
            b2 = answer_question('那15呢？', b['next_question'])
            a3 = answer_question('那16呢？', a2['next_question'])
            self.assertEqual(a2['sources'][0]['id'], 'FAULT-IDV15')
            self.assertEqual(b2['sources'][0]['id'], 'VAR-X15')
            self.assertEqual(a3['sources'][0]['id'], 'FAULT-IDV16')
            self.assertEqual(answer_question('那15呢？')['status'], 'needs_clarification')
            self.assertIn('IDV(16)', model.call_args.args[0])

    def test_selected_chunks_and_versioned_sources(self):
        settings = {'TEP_LLM_API_KEY': 'test-only', 'TEP_LLM_BASE_URL': 'http://127.0.0.1:9999/v1',
                    'TEP_LLM_MODEL': 'qwen3.8-flash'}
        response = BytesIO(json.dumps({'choices': [{'message': {'content': 'IDV(7) 是 C 进料压力损失。[1]'}}]}).encode())
        with patch.dict(os.environ, settings), patch('qa.urlopen', return_value=response) as call:
            result = answer_question('IDV7是什么故障？')
        request = call.call_args.args[0]
        payload = json.loads(request.data)
        self.assertIs(payload['enable_thinking'], False)
        self.assertIn('FAULT-IDV07', payload['messages'][1]['content'])
        self.assertNotIn('/Users/', payload['messages'][1]['content'])
        self.assertEqual(len(result['sources']), 1)
        s = result['sources'][0]
        self.assertEqual(s['id'], 'FAULT-IDV07')
        self.assertTrue(s['content'])
        self.assertTrue(s['locators'])
        self.assertEqual(s['document_version'], '1.0.0')
        self.assertNotIn('path', s['locators'][0])

    def test_invalid_or_missing_citations_not_displayed(self):
        for content in ['没有引用的结论', '假引用[99]', '错误编号[0]']:
            with patch('qa.chat_completion', return_value=content):
                with self.assertRaises(QAError): answer_question('X4是什么？')

    def test_deepseek_official_request_and_cited_answer(self):
        settings = {'TEP_LLM_API_KEY': 'test-only-deepseek',
                    'TEP_LLM_BASE_URL': 'https://api.deepseek.com',
                    'TEP_LLM_MODEL': 'deepseek-flash'}
        response = BytesIO(json.dumps({'choices': [{'message': {
            'content': 'IDV(7) 是 C 进料压力损失。[1]'}}]}).encode())
        with patch.dict(os.environ, settings), patch('qa.urlopen', return_value=response) as call:
            result = answer_question('IDV(7)是什么故障？')
        request = call.call_args.args[0]
        payload = json.loads(request.data)
        self.assertEqual(request.full_url, 'https://api.deepseek.com/chat/completions')
        self.assertEqual(request.get_header('Authorization'), 'Bearer test-only-deepseek')
        self.assertEqual(payload['model'], 'deepseek-flash')
        self.assertEqual(payload['thinking'], {'type': 'disabled'})
        self.assertNotIn('enable_thinking', payload)
        self.assertNotIn('test-only-deepseek', request.data.decode())
        self.assertEqual(result['status'], 'answered')
        self.assertEqual(result['sources'][0]['id'], 'FAULT-IDV07')

    def test_validation_and_model_failure(self):
        for q in ['', '长' * 501]:
            with self.assertRaises(QAError): answer_question(q)
        with patch('qa.chat_completion', side_effect=QAError('请求超时')):
            with self.assertRaisesRegex(QAError, '超时'): answer_question('X4是什么？')


if __name__ == '__main__': unittest.main()
