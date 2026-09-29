import unittest
from followup_query import ConversationRetriever, resolve_followup
from retrieve_chunks import ContextIndex, RuleIndex


class FollowupParsingTests(unittest.TestCase):
    def test_inherits_type_and_preserves_current_original(self):
        for previous,target in [('IDV(14)是什么故障？','FAULT-IDV15'),('X14是什么？','VAR-X15'),
                                ('流4通向哪里？','STREAM-05'),('XMV(4)的作用是什么？','VAR-X46')]:
            current='那5呢？' if '4' in previous and '14' not in previous else '那15呢？'
            a=resolve_followup(current,previous)
            self.assertEqual(a['primary_units'],[target])
            self.assertEqual(a['original_query'],current)
            self.assertTrue(a['context_used'])
            self.assertEqual(a['resolution_status'],'resolved')

    def test_keeps_other_numbers_in_previous_question(self):
        a=resolve_followup('那15呢？','X14每3分钟采样一次吗？')
        self.assertIn('X15',a['resolved_query'])
        self.assertIn('3分钟',a['resolved_query'])

    def test_pronoun_and_explicit_comparison(self):
        a=resolve_followup('它的单位是什么？','X4代表什么？')
        self.assertEqual(a['primary_units'],['VAR-X04'])
        self.assertIn('单位',a['resolved_query'])
        a=resolve_followup('它与X45有什么区别？','X4是什么？')
        self.assertEqual(set(a['primary_units']),{'VAR-X04','VAR-X45'})
        self.assertEqual(a['intent'],'comparison')

    def test_explicit_topic_wins_and_unrelated_topic_does_not_inherit(self):
        for q in ['X15是什么？','这个变量X15是什么？']:
            a=resolve_followup(q,'IDV(14)是什么？')
            self.assertFalse(a['context_used'])
            self.assertEqual(a['primary_units'],['VAR-X15'])
        for q in ['杭州明天的天气怎么样？','21种故障都测过了吗？','这个项目怎么启动？']:
            self.assertFalse(resolve_followup(q,'X14是什么？')['context_used'])

    def test_ambiguity_missing_history_and_type_mismatch(self):
        for previous,current in [('', '那15呢？'),('X14和IDV(14)是什么？','那15呢？'),
            ('X14和X15有什么区别？','它的单位是什么？'),('X4是什么？','这个故障是什么？'),
            ('IDV(99)是什么？','那15呢？'),('X4是什么？','为什么会这样？'),
            ('X4是什么？','那15和16呢？')]:
            a=resolve_followup(current,previous)
            self.assertEqual(a['resolution_status'],'needs_clarification')
            self.assertEqual(a['retrieval_query'],'')
            self.assertFalse(a['primary_units'])
            self.assertTrue(a['clarification'])

    def test_out_of_range_and_unrecorded_xmv(self):
        a=resolve_followup('那99呢？','IDV(14)是什么？')
        self.assertEqual(a['resolution_status'],'needs_clarification')
        a=resolve_followup('那12呢？','XMV(11)是什么？')
        self.assertEqual(a['intent'],'data_schema')
        self.assertNotIn('VAR-X53',str(a))

    def test_normalizes_full_width_and_chinese_numeral(self):
        a=resolve_followup('那十五呢？','ＩＤＶ（１４）是什么？')
        self.assertEqual(a['primary_units'],['FAULT-IDV15'])


class ConversationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.index=ContextIndex()

    def test_current_subject_first_previous_subject_auxiliary(self):
        result=self.index.query_with_context('那15呢？','IDV(14)是什么故障？',2)
        self.assertEqual([h['unit_id'] for h in result['hits']],['FAULT-IDV15','FAULT-IDV14'])
        self.assertIn('辅助',result['hits'][1]['rank_reason'])

    def test_xmv12_scope_not_displaced_by_old_subject(self):
        hits=self.index.search('那12呢？',previous_question='XMV(11)是什么？')
        self.assertEqual(hits[0]['unit_id'],'SCOPE-001')

    def test_chain_uses_last_resolved_user_question(self):
        session=ConversationRetriever(self.index)
        session.ask('IDV(14)是什么故障？')
        second=session.ask('那15呢？')
        third=session.ask('那16呢？')
        self.assertEqual(second['hits'][0]['unit_id'],'FAULT-IDV15')
        self.assertEqual(third['hits'][0]['unit_id'],'FAULT-IDV16')
        self.assertIn('IDV(15)',third['analysis']['previous_question'])
        self.assertIn('IDV(16)',session.previous_question)

    def test_sessions_are_isolated_and_reset_works(self):
        a=ConversationRetriever(self.index);b=ConversationRetriever(self.index)
        a.ask('IDV(14)是什么？');b.ask('X14是什么？')
        self.assertEqual(a.ask('那15呢？')['hits'][0]['unit_id'],'FAULT-IDV15')
        self.assertEqual(b.ask('那15呢？')['hits'][0]['unit_id'],'VAR-X15')
        a.reset()
        self.assertEqual(a.ask('那16呢？')['analysis']['resolution_status'],'needs_clarification')

    def test_ambiguity_and_topic_switch_do_not_reuse_stale_subject(self):
        s=ConversationRetriever(self.index)
        s.ask('IDV(14)是什么？')
        s.ask('杭州明天天气怎么样？')
        self.assertEqual(s.ask('那15呢？')['hits'],[])
        s.ask('X14和IDV(14)是什么？')
        r=s.ask('那15呢？')
        self.assertEqual(r['hits'],[])
        self.assertTrue(r['clarification'])
        self.assertEqual(s.previous_question,'')
        self.assertEqual(s.ask('X15是什么？')['hits'][0]['unit_id'],'VAR-X15')

    def test_standalone_results_remain_same_as_rule_mode(self):
        old=RuleIndex()
        for q in ['X4和X45有什么区别？','流4直接进反应器吗？','这21种故障都测过了吗？']:
            self.assertEqual(self.index.search(q),old.search(q))


if __name__=='__main__':unittest.main()
