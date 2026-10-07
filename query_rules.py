"""TEP 问题的可解释规则解析；不调用模型，不读取评测答案，不使用聊天历史。"""
import re
import unicodedata

RULE_VERSION = '1.2.0'
NUM = r'(?:\d+|[零〇一二两三四五六七八九十百]+)'
EQUIPMENT_NAMES = {
    'EQUIP-REACTOR': r'反应器|反应釜|(?<![A-Za-z0-9_])reactor(?![A-Za-z0-9_])',
    'EQUIP-CONDENSER': r'冷凝器|(?<![A-Za-z0-9_])condenser(?![A-Za-z0-9_])',
    'EQUIP-SEPARATOR': r'[汽气]液分离器|分离器|(?<![A-Za-z0-9_])separator(?![A-Za-z0-9_])',
    'EQUIP-COMPRESSOR': r'(?:循环)?压缩机|(?<![A-Za-z0-9_])compressor(?![A-Za-z0-9_])',
    'EQUIP-STRIPPER': r'[汽气]提塔|(?<![A-Za-z0-9_])stripper(?![A-Za-z0-9_])',
}


def number(text):
    if text.isdigit():
        return int(text)
    digits = dict(zip('零〇一二两三四五六七八九', [0,0,1,2,2,3,4,5,6,7,8,9]))
    result = current = 0
    for char in text:
        if char in digits:
            current = digits[char]
        elif char in ('十','百'):
            result += (current or 1) * (10 if char == '十' else 100)
            current = 0
        else:
            raise ValueError('不支持的中文数字')
    return result + current


def entity(kind,n):
    limits={'fault':21,'variable':52,'stream':13,'xmeas':41,'xmv':12}
    canonical={'fault':f'IDV({n})','variable':f'X{n}','stream':f'流 {n}',
               'xmeas':f'XMEAS({n})','xmv':f'XMV({n})'}[kind]
    valid=1 <= n <= limits[kind]
    target=None
    if valid:
        if kind=='fault':target=f'FAULT-IDV{n:02}'
        elif kind in ('variable','xmeas'):target=f'VAR-X{n:02}'
        elif kind=='xmv' and n<=11:target=f'VAR-X{n+41:02}'
        elif kind=='stream':target=f'STREAM-{n:02}' if n<=11 else f'UTILITY-{n:02}'
    return {'kind':kind,'number':n,'canonical':canonical,'valid':valid,'primary_unit':target}


def parse_query(query):
    if not isinstance(query,str) or not query.strip() or len(query)>2000:
        raise ValueError('问题须为非空文本且不超过2000字符')
    text=unicodedata.normalize('NFKC',query)
    entities=[]; counts=[]; occupied=[]; reasons=[]
    # 数量词优先识别，后续只有带类型前缀/后缀的数字才能被视作编号。
    count_pattern=rf'({NUM})\s*(种|个|列|条|次|分钟|小时|天)'
    for m in re.finditer(count_pattern,text):
        if re.search(r'第\s*$',text[:m.start()]):
            continue
        counts.append({'text':m[0],'number':number(m[1]),'unit':m[2],'span':list(m.span())})
    count_spans=[c['span'] for c in counts]

    def take(m,kind,a,b=None):
        span=m.span()
        if any(span[0]<end and span[1]>start for start,end in occupied):return
        # “故障21种”属于数量表达，也不能按故障号识别。
        if any(span[0]<end and span[1]>start for start,end in count_spans):return
        occupied.append(span)
        lo=number(a);hi=number(b) if b is not None else lo
        if hi<lo or hi-lo>52:
            entities.append({**entity(kind,lo),'valid':False,'primary_unit':None,
                             'raw':m[0],'span':list(span),'issue':'编号区间倒序或过长'})
            return
        for n in range(lo,hi+1):
            entities.append({**entity(kind,n),'raw':m[0],'span':list(span)})

    # 范围先于单编号，避免只吃掉“X23–X28”的第一个端点。
    for label,kind in [('XMEAS','xmeas'),('XMV','xmv'),('IDV','fault'),('X','variable')]:
        boundary=r'(?<![A-Za-z0-9_])'
        one=rf'{label}\s*\(?\s*({NUM})\s*\)?'
        pat=boundary+one+rf'\s*[-–—~至到]\s*(?:{label}\s*)?\(?\s*({NUM})\s*\)?(?![\dA-Za-z_])'
        for m in re.finditer(pat,text,re.I):take(m,kind,m[1],m[2])
        for m in re.finditer(boundary+one+r'(?![\dA-Za-z_])',text,re.I):take(m,kind,m[1])
    for pat,kind in [
        (rf'故障\s*(?:编号\s*)?[(:]?\s*({NUM})\s*\)?(?:\s*[-–—~至到]\s*(?:故障\s*)?({NUM}))?','fault'),
        (rf'第\s*({NUM})\s*(?:号|个)?\s*故障','fault'),
        (rf'({NUM})\s*号\s*故障','fault'),
        (rf'(?:流股|物流|流)\s*(?:编号\s*)?[(:]?\s*({NUM})\s*\)?(?:\s*[-–—~至到]\s*(?:流股|物流|流)?\s*({NUM}))?','stream'),
    ]:
        for m in re.finditer(pat,text):take(m,kind,m[1],m[2] if m.lastindex and m.lastindex>=2 else None)
    unique={}
    for e in entities:
        unique.setdefault((e['kind'],e['number']),e)
    entities=list(unique.values())
    issues=[f"{e['raw']} 超出本手册编号范围或区间无效" for e in entities if not e['valid']]
    targets=list(dict.fromkeys(e['primary_unit'] for e in entities if e['valid'] and e['primary_unit']))
    equipment_units=[unit for unit,pattern in EQUIPMENT_NAMES.items() if re.search(pattern,text,re.I)]
    if any(e['kind']=='xmv' and e['number']==12 and e['valid'] for e in entities):
        issues.append('XMV(12) 是搅拌器操纵量，但未记录在52列文件中；不映射为X53')

    # 意图只由词组与实体类型判断；不按Q01等题号或完整题目写特例。
    intent='general'; intent_kinds=[]
    domain_context=bool(entities or equipment_units) or bool(re.search(r'TEP|TE过程|故障|反应器|汽提|分离器|冷凝|压缩机|物料|物流|流股|组分|本项目',text,re.I))
    if domain_context and not targets and re.search(r'反应式|化学反应|反应原料|惰性|催化剂|组分角色|反应生成',text):
        intent='chemistry';intent_kinds=['chemistry']
        reasons.append('询问组分角色或反应关系，优先化学反应说明')
    elif domain_context and re.search(r'测过|验证过|测试过|都验证|覆盖了|验证范围|测试范围|实验范围',text):
        intent='validation_scope';intent_kinds=['dataset_scope']
        reasons.append('询问已做实验/验证的范围，优先数据范围说明')
    elif re.search(r'加起来|加总|总和|相加|合计|归一化',text) and any(
            e['kind'] in ('variable','xmeas') and 23<=e['number']<=41 for e in entities):
        intent='composition_sum';intent_kinds=['editorial_guidance']
        reasons.append('组分变量的求和/归一化问题，优先数据解释，再保留变量定义')
    elif re.search(r'12.*操纵|操纵.*12|52\s*列|搅拌器',text) or any(
            e['kind']=='xmv' and e['number']==12 and e['valid'] for e in entities):
        intent='data_schema';intent_kinds=['scope','variable_conventions']
        reasons.append('询问数据列/操纵变量覆盖范围')
    elif domain_context and re.search(r'哪里|哪儿|去向|流向|流经|进.*吗|进入|出口|入口|连接|路径|流程',text) and not any(
            e['kind']=='fault' for e in entities):
        intent='process_topology';intent_kinds=['process_overview','stream','equipment']
        reasons.append('询问进出口或物流连接，优先流程类资料')
    elif re.search(r'顺序|传播|先影响|先变化|根源|根因',text):
        intent='fault_mechanism';intent_kinds=['fault_conventions','limitations']
        reasons.append('询问机理/传播；匹配注入定义和解释边界，不生成传播结论')
    elif re.search(r'区别|比较|对比|有什么不同',text):
        intent='comparison'
    elif targets:
        intent='entity_lookup'
    elif equipment_units:
        intent='equipment_lookup';intent_kinds=['equipment']
    ambiguous=False
    if not entities and not counts and re.search(NUM,text):
        ambiguous=True
        issues.append('存在没有类型标识的数字；本阶段不根据历史猜测编号类型')
    retrieval_text=text
    # 只在缺少显式实体的范围问句里去掉数量，避免数量21与X21重合。
    if intent in ('validation_scope','data_schema') and not entities:
        for count in reversed(counts):
            a,b=count['span'];retrieval_text=retrieval_text[:a]+' '+retrieval_text[b:]
    for e in entities:
        if e['valid']:
            retrieval_text+=' '+e['canonical']
    if targets:reasons.append('仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体')
    # 有显式编号时仍以编号为主体；否则将点名设备定位到设备说明，避免被变量表淹没。
    if not targets and equipment_units:
        targets=equipment_units
        reasons.append('设备名称匹配到设备说明条目，优先于仅提到设备的变量或流股')
    return {'parser_version':RULE_VERSION,'original_query':query,'normalized_query':text,
            'retrieval_query':retrieval_text.strip(),'entities':entities,'quantities':counts,
            'intent':intent,'intent_kinds':intent_kinds,'primary_units':targets,'equipment_units':equipment_units,
            'ambiguous_number':ambiguous,'issues':issues,'reasons':reasons,'context_used':False}


def priority(chunk,parsed):
    """显式主体优先；意图是次序提示，其他资料仍保留，不作硬过滤。"""
    direct=chunk['unit_id'] in parsed['primary_units']
    intent_match=chunk['kind'] in parsed['intent_kinds']
    if parsed['intent']=='composition_sum':
        return (3 if intent_match else 2 if direct else 0,
                '组分求和解释' if intent_match else '编号主体' if direct else '文本匹配')
    if direct:return 3,'主体条目精确匹配'
    if intent_match:
        # 未指明某条流时，完整总览优先于单独流股。
        if parsed['intent']=='process_topology' and not parsed['primary_units']:
            return (2 if chunk['kind']=='process_overview' else 1),'流程意图匹配'
        return 1,'意图匹配'
    return 0,'文本匹配'
