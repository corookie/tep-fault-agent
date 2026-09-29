"""Build a key-free GitHub Pages preview from the local TEP application.

The process animation stays interactive. The nine supported diagnosis parameter
combinations are precomputed with the same Python code as the local service.
Online Q&A requires a separate backend and is not emulated here.
"""

import json
from pathlib import Path

from app import PAGE, render_result


ROOT = Path(__file__).parent
OUTPUT = ROOT / "docs"


def main() -> None:
    diagnosis_dir = OUTPUT / "diagnosis"
    diagnosis_dir.mkdir(exist_ok=True)
    for samples in (50, 100, 200):
        for lag in (1, 2, 3):
            html = render_result(samples, lag)
            (diagnosis_dir / f"{samples}-{lag}.json").write_text(
                json.dumps({"html": html}, ensure_ascii=False), encoding="utf-8"
            )

    page = PAGE.replace(
        "<script>",
        '<script>window.TEP_DEPLOYMENT = {staticMode: true, apiBase: ""};</script><script>',
        1,
    )
    page = page.replace("{configuration_status}", "GitHub Pages 演示：知识问答需独立后端")
    page = page.replace("{diagnose_result}", "").replace("{qa_result}", "")
    page = page.replace(" · 本地研究演示", " · 公开交互演示")
    page = page.replace(
        '<div class="chat-toolbar">',
        '<p class="deployment-note" role="status">此公开页面可体验工艺动画和预计算的故障诊断结果（9组参数）。在线知识问答暂未启用；本地运行版本可使用完整功能。</p><div class="chat-toolbar">',
        1,
    )
    (OUTPUT / "index.html").write_text(page, encoding="utf-8")
    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {OUTPUT / 'index.html'} and nine diagnosis responses")


if __name__ == "__main__":
    main()
