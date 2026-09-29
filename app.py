"""无需额外网页框架的 TEP 故障诊断演示入口。"""

import json
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
import tempfile
from pathlib import Path
from urllib.parse import parse_qs

from diagnose import VARIABLES, diagnose
from diagnosis_graph import NAMES, render_graphs
from inspect_data import load_data
from qa import QAError, answer_question
from process_diagram import PROCESS_CSS, PROCESS_JS, render_process_diagram


HOST = "127.0.0.1"
PORT = 8765
BAILIAN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
BAILIAN_MODEL = "qwen3.8-flash"
KEY_DIR = Path.home() / ".tep-fault-agent"
KEY_FILE = KEY_DIR / "bailian-api-key"


def activate_key(api_key: str) -> None:
    os.environ.setdefault("TEP_LLM_BASE_URL", BAILIAN_BASE_URL)
    os.environ.setdefault("TEP_LLM_MODEL", BAILIAN_MODEL)
    os.environ["TEP_LLM_API_KEY"] = api_key


def save_key(api_key: str) -> None:
    KEY_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(KEY_DIR, 0o700)
    descriptor, temporary = tempfile.mkstemp(prefix=".key-", dir=KEY_DIR)
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as file:
            file.write(api_key)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, KEY_FILE)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def load_saved_key() -> None:
    if os.getenv("TEP_LLM_API_KEY"):
        return
    try:
        api_key = KEY_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return
    if api_key.startswith("sk-"):
        activate_key(api_key)
WEB_DIR = Path(__file__).parent / "web"
PAGE = (WEB_DIR.joinpath("index.html").read_text(encoding="utf-8")
        .replace("{ui_css}", WEB_DIR.joinpath("styles.css").read_text(encoding="utf-8"))
        .replace("{ui_js}", WEB_DIR.joinpath("app.js").read_text(encoding="utf-8"))
        .replace("{process_css}", PROCESS_CSS)
        .replace("{process_js}", PROCESS_JS)
        .replace("{process_overview}", render_process_diagram()))


def render_result(samples: int, lag: int) -> str:
    frame = load_data("d07_te.dat")
    values = frame.iloc[160 : 160 + samples].loc[:, VARIABLES].to_numpy(dtype=float)
    result = diagnose(values, lag=lag)
    selected = [edge for edge in result["edges"] if edge["selected"]]
    candidate_cards = ''.join(
        f'<button type="button" class="candidate-chip" data-question="{escape(v)}代表什么？" aria-label="了解{escape(v)}的变量含义">'
        f'<span class="candidate">{escape(v)}</span><small>{escape(NAMES.get(v,v))}</small><i aria-hidden="true">↗</i></button>'
        for v in result['candidates']
    ) or '<span class="candidate result-empty-title">证据不足</span>'
    result_note = ('这些变量在本次格兰杰关系图中排名最高，可能是故障传播的起点。点击变量可查询含义；实际根因仍需结合工艺验证。'
                   if result['candidates'] else '当前数据不足以给出可能的根源变量，可尝试增加采样点数。')
    ranking_rows = "".join(
        f"<tr><td>{escape(item['variable'])}</td><td>{item['outgoing']}</td>"
        f"<td>{item['incoming']}</td><td>{item['score']}</td></tr>"
        for item in result["rankings"]
    )
    edge_rows = "".join(
        f"<tr><td>{escape(edge['source'])} → {escape(edge['target'])}</td>"
        f"<td>{edge['improvement']:.1%}</td><td>{edge['q_value']:.3g}</td></tr>"
        for edge in sorted(selected, key=lambda item: item["q_value"])
    ) or "<tr><td colspan='3'>当前参数下没有筛出关系</td></tr>"
    return (
        "<section class='card result-summary'><div class='result-summary-top'><h3>可能的故障根源变量</h3>"
        f"<span class='result-window'>分析范围：第 161–{160 + samples} 个采样点 · {samples}点窗口 · 时滞 {lag} 点</span></div>"
        f"<div class='candidate-row'><div class='candidate-list'>{candidate_cards}</div><div class='result-stat'><strong>{len(selected)}</strong>条格兰杰因果关系 / {len(VARIABLES)} 个变量</div></div>"
        f"<p class='result-note'>{result_note}</p></section>"
        + render_graphs(result) +
        "<details class='card evidence-section'><summary>查看计算依据：根源变量如何排名？</summary>"
        "<h2>根源变量排名</h2><p>指向其他变量的关系越多、来自其他变量的关系越少，当前排序分数越高。"
        "这里的关系表示历史信息对预测有帮助，不等于已确认的物理影响。</p>"
        "<div class='calculation-table'><table><tr><th>变量</th><th>指向其他变量的关系数</th><th>来自其他变量的关系数</th><th>排序分数（前者−后者）</th></tr>"
        f"{ranking_rows}</table></div><p><small>仅把正分最高的变量列为候选；并列时全部保留。分数不是根因概率。</small></p>"
        "<h2>每条关系的预测依据</h2><p>A → B表示：预测B时，使用A的历史信息，比去掉A的历史信息更有帮助。"
        "例如，不使用A时平均误差为10，使用后为8，预测误差就降低了20%。这不表示A造成了B的20%变化。</p>"
        "<div class='calculation-table'><table><tr><th>关系（预测帮助方向）</th><th>加入源变量后，预测误差降低</th><th>q值</th></tr>"
        f"{edge_rows}</table></div><p><small>误差采用测试段的平均绝对误差。筛选要求误差改善为正、探索性q值&lt;0.10。"
        "q值为多重检验调整值，不是因果关系成立的概率；测试点可能相关。不同窗口可能得到不同结果。</small></p>"
        "<h2>方法与边界</h2><p>当前采用基于核岭回归（KRR）的简化格兰杰因果检验，不输出逐边传播时延或正负作用。滞后阶数不能当作每条边的传播时间；尚未复现论文JGC章节图4.8的完整方法。候选路径需结合工艺、时滞及更多窗口验证。</p></details>"

    )


def render_answer(question: str) -> str:
    result = answer_question(question)
    sources = "".join(
        f"<li>{escape(item['marker'])} {escape(item['source'])}<p>{escape(item.get('content', ''))}</p></li>" for item in result["sources"]
    )
    source_section = f"<h3>参考来源</h3><ul>{sources}</ul>" if sources else ""
    return (
        "<section class='card'>"
        f"<p><strong>问题：</strong>{escape(question)}</p>"
        f"<p class='answer'>{escape(result['answer'])}</p>"
        f"{source_section}</section>"
    )


class Handler(BaseHTTPRequestHandler):
    def send_page(self, result: str, status: int = 200, slot: str = "qa") -> None:
        configured = all(os.getenv(name) for name in (
            "TEP_LLM_API_KEY", "TEP_LLM_BASE_URL", "TEP_LLM_MODEL"
        ))
        configuration_status = "问答服务已配置" if configured else "问答服务未配置"
        body = (PAGE.replace("{configuration_status}", configuration_status)
                .replace("{diagnose_result}", result if slot == "diagnose" else "")
                .replace("{qa_result}", result if slot == "qa" else "")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/":
            self.send_page("")
        else:
            self.send_error(404)

    def do_POST(self) -> None:
        if self.path not in ("/run", "/api/diagnose", "/ask", "/api/ask"):
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        if length < 0 or length > 16000:
            if self.path.startswith("/api/"):
                self.send_json({"error": "请求过大"}, 400)
            else:
                self.send_page("<section class='card error'>请求过大</section>", 400)
            return
        form = parse_qs(self.rfile.read(length).decode("utf-8"))
        try:
            if self.path == "/api/ask":
                question = form.get("question", [""])[0]
                previous_question = form.get("previous_question", [""])[0]
                self.send_json(answer_question(question, previous_question=previous_question))
            elif self.path == "/ask":
                question = form.get("question", [""])[0]
                self.send_page(render_answer(question))
            else:
                samples = int(form.get("samples", ["100"])[0])
                lag = int(form.get("lag", ["3"])[0])
                if samples not in (50, 100, 200) or lag not in (1, 2, 3):
                    raise ValueError("请选择页面提供的参数")
                if self.path == "/api/diagnose":
                    self.send_json({"html": render_result(samples, lag)})
                else:
                    self.send_page(render_result(samples, lag), slot="diagnose")
        except (ValueError, ArithmeticError, QAError) as exc:
            if self.path.startswith("/api/"):
                self.send_json({"error": str(exc)}, 400)
            else:
                self.send_page(f"<section class='card error'>{escape(str(exc))}</section>", 400)


def serve() -> None:
    load_saved_key()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"打开 http://{HOST}:{PORT}，按 Ctrl+C 退出")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    serve()
