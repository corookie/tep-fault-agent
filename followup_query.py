"""保守的单步追问补全。历史只取上一轮用户已明确/已消歧的问题，不取助手答案。"""
import re
import unicodedata
from query_rules import NUM, entity, number, parse_query

FOLLOWUP_VERSION = '1.0.0'
BARE_NUMBER = re.compile(rf'^\s*(?:那|那么|还有|换成|改成)?\s*({NUM})\s*(?:号)?\s*(?:呢|怎么样)?\s*[?？。!！]*\s*$')
PRONOUN = re.compile(r'这个变量|那个变量|该变量|这个故障|那个故障|该故障|这条流(?:股)?|那条流(?:股)?|它|(?:这个|那个)(?=\s*(?:的|呢|是|和|与|为什么|怎么|[?？]))')
# 这些表达依赖更复杂的语境，本轮宁可询问，不擅自选择前一对象。
UNSUPPORTED = re.compile(r'前者|后者|上一个|刚才那个|它们|二者|两者|为什么会这样|为什么这样')


def resolve_followup(query, previous_question=''):
    current=parse_query(query)
    text=current['normalized_query']
    base={**current,'followup_version':FOLLOWUP_VERSION,'previous_question':previous_question,
          'resolved_query':query,'resolution_status':'standalone','resolution_reason':'当前问题独立解析',
          'clarification':None,'context_units':[],'context_used':False}

    def clarify(reason, message='这次指的是哪个故障、变量或流股？请补充具体编号。'):
        return {**base,'resolution_status':'needs_clarification','resolution_reason':reason,
                'clarification':message,'retrieval_query':'','primary_units':[], 'context_units':[]}

    bare=BARE_NUMBER.fullmatch(text)
    pronoun=PRONOUN.search(text)
    if UNSUPPORTED.search(text):
        return clarify('指代表达超出当前规则支持范围')
    if not bare and not pronoun:
        # 有歧义的裸数字即使不像标准短问也不自动按X编号检索。
        if current['ambiguous_number'] and re.search(r'那|呢|换成|改成',text):
            return clarify('包含未明确类型的数字，且不符合可补全的短问格式')
        return base
    if pronoun and any(e['span'][0]>=pronoun.end() and not text[pronoun.end():e['span'][0]].strip()
                       for e in current['entities']):
        # “这个变量X15”已经明确指名，不套用上一轮X14。
        return base
    if bare and current['entities']:
        return base
    if not previous_question:
        return clarify('缺少可用上一轮问题')
    previous=parse_query(previous_question)
    old_entities=previous['entities']
    if len(old_entities)!=1 or not old_entities[0]['valid']:
        return clarify('上一问没有唯一且有效的主体，不能安全继承')
    old=old_entities[0]
    if pronoun:
        noun=pronoun[0]
        expected=('fault' if '故障' in noun else 'stream' if '流' in noun else 'variable' if '变量' in noun else None)
        actual='variable' if old['kind'] in ('variable','xmeas','xmv') else old['kind']
        if expected and expected!=actual:
            return clarify('指代类型与上一主体不一致')
        resolved=PRONOUN.sub(lambda _:old['canonical'],text)
        reason='用上一轮唯一主体替换指代词，保留当前问法'
    else:
        new=entity(old['kind'],number(bare[1]))
        if not new['valid']:
            return clarify('继承类型后编号越界',f"按上一轮的 {old['kind']} 类型，编号 {bare[1]} 超出当前手册范围；请核对编号或说明类型。")
        # 只替换主体的字符区间，保留历史问题里的单位、时间等其他数字。
        start,end=old['span']
        previous_text=previous['normalized_query']
        resolved=previous_text[:start]+new['canonical']+previous_text[end:]
        reason=f"从上一轮继承 {old['kind']} 类型及问法，仅替换主体编号"
    parsed=parse_query(resolved)
    if any(not e['valid'] for e in parsed['entities']):
        return clarify('补全后的主体编号无效')
    context_units=[old['primary_unit']] if old['primary_unit'] and old['primary_unit'] not in parsed['primary_units'] else []
    return {**parsed,'original_query':query,'normalized_query':text,
            'followup_version':FOLLOWUP_VERSION,'previous_question':previous_question,
            'resolved_query':resolved,'resolution_status':'resolved','resolution_reason':reason,
            'clarification':None,'context_units':context_units,'context_used':True}


class ConversationRetriever:
    """一个实例对应一个会话。仅保存上一条已消歧查询，防止串用其他会话或旧话题。"""
    def __init__(self,index):
        self.index=index
        self.previous_question=''

    def ask(self,query,top_k=5,min_score=0.0):
        result=self.index.query_with_context(query,self.previous_question,top_k,min_score)
        analysis=result['analysis']
        if analysis['resolution_status']=='needs_clarification' or any(not e['valid'] for e in analysis['entities']):
            # 不让后续追问跳过未解决的一轮，悄悄继承更早话题。
            self.previous_question=''
        else:
            self.previous_question=analysis['resolved_query']
        return result

    def reset(self):
        self.previous_question=''
