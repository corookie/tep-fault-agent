"""记录真实回答与证据供逐条复核。默认只展示用例，--live 才调用已配置模型。"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import time
from unittest.mock import patch

import qa

BASE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true', help='使用已有模型配置，会产生实际调用')
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    suite_path = BASE / 'evaluation/answer_acceptance_v1.json'
    suite = json.loads(suite_path.read_text())
    if not args.live:
        for case in suite['cases']:
            print(case['id'], case['question'], '→', case['expected_status'])
        print('仅展示用例；执行 --live 后调用模型并保存回答供复核。')
        return
    from app import load_saved_key
    load_saved_key()
    output = args.output_dir or BASE / 'acceptance_build' / datetime.now().strftime('%Y%m%d-%H%M%S')
    output.mkdir(parents=True, exist_ok=False)
    report = {
        'suite_id': suite['suite_id'], 'suite_sha256': hashlib.sha256(suite_path.read_bytes()).hexdigest(),
        'started_at': datetime.now(timezone.utc).isoformat(), 'model': os.getenv('TEP_LLM_MODEL', ''),
        'prompt_version': qa.PROMPT_VERSION, 'index_sha256': qa.get_index().index_sha256,
        'code_sha256': {n: hashlib.sha256((BASE / n).read_bytes()).hexdigest()
                        for n in ('qa.py', 'query_rules.py', 'followup_query.py')},
        'review_note': 'status_matches仅检查路由；回答忠实性须逐条核对sources，不能以引用存在代替语义复核。',
        'cases': [],
    }
    for case in suite['cases']:
        start = time.monotonic()
        with patch('qa.chat_completion', wraps=qa.chat_completion) as model:
            try:
                result = qa.answer_question(case['question'], case.get('previous_question', ''))
            except qa.QAError as exc:
                result = {'status': 'error', 'answer': str(exc), 'sources': []}
            row = {**case, 'result': result, 'model_calls': model.call_count,
                   'elapsed_seconds': round(time.monotonic() - start, 2),
                   'status_matches': result['status'] == case['expected_status'], 'semantic_review': '待逐条复核'}
        report['cases'].append(row)
        (output / 'answers.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
        print(case['id'], result['status'], 'model_calls=' + str(row['model_calls']), flush=True)
    lines = ['# 真实回答验收原始记录', '', report['review_note'], '']
    for row in report['cases']:
        lines += [f"## {row['id']}：{row['question']}", '',
                  f"预期：{row['criteria']}", '',
                  f"实际状态：{row['result']['status']}；模型调用：{row['model_calls']}；耗时：{row['elapsed_seconds']}秒。", '',
                  row['result']['answer'], '']
        for source in row['result']['sources']:
            lines += [f"### {source['marker']} {source['id']}", '', source['source'], '', source['content'], '']
    (output / 'answers.md').write_text('\n'.join(lines) + '\n')
    print('Output:', output)


if __name__ == '__main__':
    main()
