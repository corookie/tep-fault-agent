"""离线 TF-IDF 检索与评测；无模型调用。build / query / evaluate 三个子命令。"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import tempfile
import time

import numpy as np
import scipy
from scipy.sparse import load_npz, save_npz
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from query_rules import RULE_VERSION, parse_query, priority
from followup_query import FOLLOWUP_VERSION, resolve_followup

BASE = Path(__file__).resolve().parent
VERSION = '1.0.0'
DEFAULT_INDEX = BASE/'retrieval_build/index'
CONFIG = {'analyzer':'char','ngram_range':[2,3],'lowercase':True,
          'fields':['title','entities','content'],
          'normalization':'保留Markdown链接文字，去掉链接地址/裸URL/Markdown符号；合并空白；不做同义词或编号改写',
          'conversation_context':'unused','algorithm':'char_tfidf_cosine','version':VERSION}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def dump(data):
    return json.dumps(data,ensure_ascii=False,indent=2)+'\n'


def write_atomic(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent,delete=False) as f:
        f.write(data)
        temp=Path(f.name)
    temp.replace(path)


def normalize(text):
    text=re.sub(r'\[([^\]]+)\]\([^\n]*?\)',r'\1',text)
    text=re.sub(r'https?://\S+',' ',text)
    text=re.sub(r'[`*#|]',' ',text)
    return re.sub(r'\s+',' ',text).strip()


def document_text(chunk):
    return normalize(' '.join([chunk['title'],*chunk['entities'],chunk['content']]))


def build_index(chunks_path, manifest_path, output):
    raw=chunks_path.read_bytes()
    chunk_manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    if digest(raw)!=chunk_manifest['chunks_sha256']:
        raise ValueError('chunk 文件与切分清单指纹不一致，请先重新切分')
    chunks=[json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
    if len(chunks)!=chunk_manifest['chunk_count'] or not chunks:
        raise ValueError('chunk 数量与清单不一致或为空')
    ids=[c['chunk_id'] for c in chunks]
    if len(ids)!=len(set(ids)):
        raise ValueError('chunk_id 重复')
    for c in chunks:
        if digest(c['content'].encode())!=c['content_sha256']:
            raise ValueError(f"片段正文指纹不一致：{c['unit_id']}")
    texts=[document_text(c) for c in chunks]
    vectorizer=TfidfVectorizer(analyzer='char',ngram_range=(2,3),lowercase=True)
    matrix=vectorizer.fit_transform(texts)
    output.mkdir(parents=True,exist_ok=True)
    # 不使用 pickle/joblib 加载代码对象；保存稀疏矩阵和JSON参数。
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'vectors.npz'
        save_npz(p,matrix)
        matrix_bytes=p.read_bytes()
    write_atomic(output/'vectors.npz',matrix_bytes)
    write_atomic(output/'chunks.jsonl',raw)
    metadata={'index_version':VERSION,'config':CONFIG,'chunk_count':len(chunks),'feature_count':matrix.shape[1],
              'source_chunks_path':str(chunks_path.resolve()),'chunks_sha256':digest(raw),
              'chunk_manifest_sha256':digest(manifest_path.read_bytes()),'matrix_sha256':digest(matrix_bytes),
              'document_version':chunk_manifest['document_version'],
              'vocabulary':{k:int(v) for k,v in vectorizer.vocabulary_.items()},'idf':vectorizer.idf_.tolist(),
              'library_versions':{'sklearn':sklearn.__version__,'scipy':scipy.__version__,'numpy':np.__version__}}
    write_atomic(output/'index.json',dump(metadata).encode())
    return {'chunks':len(chunks),'features':matrix.shape[1],'index_dir':str(output)}


class TextIndex:
    def __init__(self,path=DEFAULT_INDEX):
        self.path=Path(path)
        index_raw=(self.path/'index.json').read_bytes()
        self.metadata=json.loads(index_raw)
        self.index_sha256=digest(index_raw)
        if self.metadata['index_version']!=VERSION or self.metadata['config']!=CONFIG:
            raise ValueError('检索规则版本不一致，请重新 build')
        raw=(self.path/'chunks.jsonl').read_bytes()
        matrix_raw=(self.path/'vectors.npz').read_bytes()
        if digest(raw)!=self.metadata['chunks_sha256'] or digest(matrix_raw)!=self.metadata['matrix_sha256']:
            raise ValueError('索引文件批次不一致或已损坏，请重新 build')
        current=Path(self.metadata['source_chunks_path'])
        if not current.exists() or digest(current.read_bytes())!=self.metadata['chunks_sha256']:
            raise ValueError('源片段已修改或移动，索引过期，请重新 build')
        self.chunks=[json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
        self.vectorizer=TfidfVectorizer(analyzer='char',ngram_range=(2,3),lowercase=True,
                                       vocabulary=self.metadata['vocabulary'])
        self.vectorizer.idf_=np.array(self.metadata['idf'])
        self.matrix=load_npz(self.path/'vectors.npz')
        if self.matrix.shape!=(len(self.chunks),len(self.metadata['vocabulary'])):
            raise ValueError('索引矩阵维度不匹配')

    def search(self,query,top_k=5,min_score=0.0):
        if not isinstance(query,str) or not query.strip():
            raise ValueError('问题不能为空')
        if len(query)>2000 or top_k<1 or not 0<=min_score<=1:
            raise ValueError('问题至多2000字符，top_k须为正数，min_score须在0–1之间')
        scores=cosine_similarity(self.vectorizer.transform([normalize(query)]),self.matrix)[0]
        ranked=sorted(range(len(scores)),key=lambda i:(-float(scores[i]),self.chunks[i]['chunk_id']))
        result=[]
        for i in ranked:
            score=float(scores[i])
            if score<=0 or score<min_score:
                continue
            result.append({'rank':len(result)+1,'score':score,**self.chunks[i]})
            if len(result)>=top_k:
                break
        return result


class RuleIndex(TextIndex):
    """复用同一索引，只添加查询解析与可解释排序。原始相似度仍单独保留。"""
    def explain(self, query):
        return parse_query(query)

    def search(self,query,top_k=5,min_score=0.0):
        parsed=self.explain(query)
        return self.search_parsed(parsed,top_k,min_score)

    def search_parsed(self,parsed,top_k=5,min_score=0.0):
        if top_k<1 or not 0<=min_score<=1:
            raise ValueError('top_k须为正数，min_score须在0–1之间')
        if parsed['entities'] and not any(e['valid'] for e in parsed['entities']):
            return []
        scores=cosine_similarity(self.vectorizer.transform([normalize(parsed['retrieval_query'])]),self.matrix)[0]
        result=[]
        for i,c in enumerate(self.chunks):
            tier,reason=priority(c,parsed)
            if parsed['primary_units'] and c['unit_id'] in parsed.get('context_units',[]) and tier<2:
                tier,reason=2,'上一轮主体作为辅助对照；当前主体仍优先'
            score=float(scores[i])
            # 普通意图不能把完全不相关的零分片段召回；显式主体允许零分精确定位。
            direct=c['unit_id'] in parsed['primary_units']
            if (score<=0 and not direct) or score<min_score:
                continue
            result.append({'score':score,'priority':tier,'rank_reason':reason,**c})
        result.sort(key=lambda h:(-h['priority'],-h['score'],h['chunk_id']))
        return [dict(h,rank=i+1) for i,h in enumerate(result[:top_k])]


class ContextIndex(RuleIndex):
    """上下文模式显式接收上一问，不将会话历史保存在共享索引中。"""
    def explain(self,query,previous_question=''):
        return resolve_followup(query,previous_question)

    def query_with_context(self,query,previous_question='',top_k=5,min_score=0.0):
        if top_k<1 or not 0<=min_score<=1:
            raise ValueError('top_k须为正数，min_score须在0–1之间')
        analysis=self.explain(query,previous_question)
        hits=[] if analysis['resolution_status']=='needs_clarification' else self.search_parsed(analysis,top_k,min_score)
        return {'analysis':analysis,'hits':hits,'clarification':analysis['clarification']}

    def search(self,query,top_k=5,min_score=0.0,previous_question=''):
        return self.query_with_context(query,previous_question,top_k,min_score)['hits']


def evidence_coverage(case,hits):
    ids={h['unit_id'] for h in hits}
    groups=case['required_evidence']
    flags=[bool(ids.intersection(g['any_of'])) for g in groups]
    return {'any_relevant':any(flags),'complete':bool(flags) and all(flags),
            'coverage':sum(flags)/len(flags) if flags else None,
            'missing':[g for g,found in zip(groups,flags) if not found]}


def evaluate(index,suite_path,output):
    raw=suite_path.read_bytes()
    suite=json.loads(raw)
    known={c['unit_id'] for c in index.chunks}
    ids=[c['id'] for c in suite['cases']]
    if len(ids)!=len(set(ids)):
        raise ValueError('评测问题编号重复')
    for c in suite['cases']:
        for group in c['required_evidence']:
            unknown=set(group['any_of'])-known
            if unknown or not group['any_of']:
                raise ValueError(f"{c['id']} 证据标签无效：{unknown}")
    rows=[]
    for case in suite['cases']:
        t=time.perf_counter()
        if isinstance(index,ContextIndex):
            packet=index.query_with_context(case['query'],case.get('previous_question',''),len(index.chunks),0)
            hits=packet['hits'];analysis=packet['analysis']
        else:
            hits=index.search(case['query'],top_k=len(index.chunks),min_score=0)
            analysis=index.explain(case['query']) if isinstance(index,RuleIndex) else None
        elapsed=(time.perf_counter()-t)*1000
        legacy=[h for h in hits[:3] if h['score']>=0.16]
        metrics={str(k):evidence_coverage(case,hits[:k]) for k in [1,3,5,10]}
        ranks={h['unit_id']:h['rank'] for h in reversed(hits)}
        expected_ranks={uid:ranks.get(uid) for g in case['required_evidence'] for uid in g['any_of']}
        first=min((r for r in expected_ranks.values() if r is not None),default=None)
        # 包含排名前十的完整正文与来源，便于审阅；完整排名只保存ID和分数。
        rows.append({**case,'latency_ms':round(elapsed,3),
                     'query_used':analysis['retrieval_query'] if analysis else case['query'],
                     'query_analysis':analysis,
                     'context_used':analysis.get('context_used',False) if analysis else False,
                     'metrics':metrics,'legacy_top3_threshold016':evidence_coverage(case,legacy),
                     'legacy_returned':[h['unit_id'] for h in legacy],
                     'expected_ranks':expected_ranks,'first_relevant_rank':first,
                     'hits':hits[:10],'all_ranks':[{'unit_id':h['unit_id'],'rank':h['rank'],'score':h['score']} for h in hits]})
    positive=[r for r in rows if not r['expected_no_results']]
    negative=[r for r in rows if r['expected_no_results']]
    summary={'positive_count':len(positive),'negative_count':len(negative),'at_k':{},
             'legacy_top3_threshold016_complete':sum(r['legacy_top3_threshold016']['complete'] for r in positive),
             'legacy_negative_rejected':sum(not r['legacy_returned'] for r in negative),
             'mrr':sum(1/r['first_relevant_rank'] if r['first_relevant_rank'] else 0 for r in positive)/len(positive)}
    for k in ['1','3','5','10']:
        summary['at_k'][k]={'any_relevant':sum(r['metrics'][k]['any_relevant'] for r in positive),
                           'complete':sum(r['metrics'][k]['complete'] for r in positive),
                           'mean_evidence_coverage':sum(r['metrics'][k]['coverage'] for r in positive)/len(positive)}
    report={'run_at':datetime.now(timezone.utc).isoformat(),'suite_id':suite['suite_id'],
            'suite_sha256':digest(raw),'index_sha256':index.index_sha256,
            'chunks_sha256':index.metadata['chunks_sha256'],'config':dict(CONFIG,
                query_rules_version=RULE_VERSION if isinstance(index,RuleIndex) else None,
                query_rules_sha256=digest((BASE/'query_rules.py').read_bytes()) if isinstance(index,RuleIndex) else None,
                followup_version=FOLLOWUP_VERSION if isinstance(index,ContextIndex) else None,
                followup_sha256=digest((BASE/'followup_query.py').read_bytes()) if isinstance(index,ContextIndex) else None),
            'limitations':[f'开发回归集{len(positive)}问，不是独立测试集','只评测检索证据，不评测答案正确性或抗注入能力',
                           ('只使用显式提供的上一轮用户问题；复杂指代仍可能需要澄清' if isinstance(index,ContextIndex)
                            else '不使用追问历史；Q15保留短问法以暴露该限制'),
                           '相关性标签为人工整理的候选证据，支持进一步复核','相似度不是正确概率'],
            'summary':summary,'results':rows}
    output.mkdir(parents=True,exist_ok=True)
    write_atomic(output/'results.json',dump(report).encode())
    write_atomic(output/'report.md',render_report(report).encode())
    return report


def render_report(report):
    s=report['summary']; total=s['positive_count']
    is_rules=bool(report['config'].get('query_rules_version'))
    is_context=bool(report['config'].get('followup_version'))
    lines=['# TEP '+('上下文追问检索报告' if is_context else '编号与意图规则检索报告' if is_rules else '文本检索基线报告'),'',
           '本轮检索110个新片段，不调用聊天模型。这里的“完整”指预先登记的证据组全部命中，不表示回答已经正确。','',
           f"评测集：{report['suite_id']}；时间：{report['run_at']}。",'',
           '## 总体结果','', '| 返回数量（不设0.16阈值） | 至少命中一组证据 | 所有必要证据齐全 |',
           '| --- | ---: | ---: |']
    for k,v in s['at_k'].items():
        lines.append(f"| 前 {k} 块 | {v['any_relevant']}/{total} | {v['complete']}/{total} |")
    lines.extend(['',f"前三块再按原始相似度≥0.16筛选：证据完整 {s['legacy_top3_threshold016_complete']}/{total}；"
                  f"无关问题拒绝 {s['legacy_negative_rejected']}/{s['negative_count']}。",'',
                  '阈值0的列表仅供诊断排序，零分片段不返回；它不是经过校准的上线配置。关键词索引使用标题、实体和正文，去掉链接地址以避免路径文字干扰。','',
                  '## 逐题结果','', '| 问题 | 前5块证据完整 | 前3名 | 未命中的证据组 |', '| --- | --- | --- | --- |'])
    for r in report['results']:
        top='；'.join(f"{h['unit_id']} ({h['score']:.3f})" for h in r['hits'][:3])
        status=('无关问题' if r['expected_no_results'] else '是' if r['metrics']['5']['complete'] else '否')
        missing='；'.join(g['description'] for g in r['metrics']['5']['missing'])
        lines.append(f"| {r['id']}：{r['query']} | {status} | {top or '无'} | {missing or '—'} |")
    lines.extend(['','## 每题命中文本与来源',''])
    for r in report['results']:
        lines.extend([f"### {r['id']} · {r['query']}",''])
        if r.get('query_analysis'):
            lines.extend(['规则解析：','', '```json',dump(r['query_analysis']).strip(),'```',''])
        if r['previous_question']:
            lines.extend([f"上一问：{r['previous_question']}。是否使用历史：{r['context_used']}。实际检索问题：{r['query_used'] or '待澄清，未检索'}。",''])
        lines.extend([f"预期证据排名：`{json.dumps(r['expected_ranks'],ensure_ascii=False)}`。null 表示无正分命中。",''])
        for h in r['hits'][:5]:
            span=h['provenance']['spans'][0]
            lines.extend([f"#### 第 {h['rank']} 名 · {h['unit_id']} · 分数 {h['score']:.4f}",'',
                          f"[原文位置]({h['provenance']['document_path']}:{span['start_line']})",'',h['content'],''])
            if 'rank_reason' in h:
                lines.extend([f"排序依据：{h['rank_reason']}；优先级 {h['priority']}；分数仍为文本余弦相似度。",''])
            lines.append('来源：'+'；'.join(f"[{src['source_id']}]({src.get('url',src.get('path',''))})" for src in h['sources']))
            lines.append('')
    lines.extend(['## 评测边界','',*[f'- {x}' for x in report['limitations']], ''])
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    b=sub.add_parser('build'); b.add_argument('--chunks',type=Path,default=BASE/'knowledge_build/chunks.jsonl')
    b.add_argument('--manifest',type=Path,default=BASE/'knowledge_build/manifest.json')
    b.add_argument('--index-dir',type=Path,default=DEFAULT_INDEX)
    q=sub.add_parser('query');q.add_argument('question');q.add_argument('--top-k',type=int,default=5)
    q.add_argument('--min-score',type=float,default=0.0);q.add_argument('--index-dir',type=Path,default=DEFAULT_INDEX)
    q.add_argument('--mode',choices=['baseline','rules','context'],default='baseline')
    q.add_argument('--previous-question',default='')
    e=sub.add_parser('evaluate');e.add_argument('--index-dir',type=Path,default=DEFAULT_INDEX)
    e.add_argument('--cases',type=Path,default=BASE/'evaluation/retrieval_cases.json')
    e.add_argument('--mode',choices=['baseline','rules','context'],default='baseline')
    e.add_argument('--output-dir',type=Path)
    args=parser.parse_args()
    try:
        if args.command=='build':
            print(dump(build_index(args.chunks,args.manifest,args.index_dir)))
        elif args.command=='query':
            index={'baseline':TextIndex,'rules':RuleIndex,'context':ContextIndex}[args.mode](args.index_dir)
            if args.previous_question and args.mode!='context':
                raise ValueError('--previous-question 需要 --mode context')
            if args.mode=='context':
                packet=index.query_with_context(args.question,args.previous_question,args.top_k,args.min_score)
                print(dump(packet['analysis']))
                hits=packet['hits']
                if packet['clarification']:print('需要澄清：'+packet['clarification'])
            else:
                if args.mode=='rules':print(dump(index.explain(args.question)))
                hits=index.search(args.question,args.top_k,args.min_score)
            for h in hits:
                print(f"\n[{h['rank']}] {h['unit_id']}  score={h['score']:.4f}\n{h['content']}\n")
            if not hits: print('没有达到阈值的片段。')
        else:
            index={'baseline':TextIndex,'rules':RuleIndex,'context':ContextIndex}[args.mode](args.index_dir)
            output=args.output_dir or BASE/'retrieval_build'/({'baseline':'evaluation','rules':'evaluation_rules','context':'evaluation_context'}[args.mode])
            result=evaluate(index,args.cases,output)
            print(dump(result['summary']))
    except (ValueError,KeyError,OSError) as exc:
        parser.exit(1,f'检索任务失败：{exc}\n')


if __name__=='__main__':
    main()
