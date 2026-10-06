"""Build a key-free GitHub Pages preview from the local TEP application.

The process animation stays interactive. The nine supported diagnosis parameter
combinations are precomputed with the same Python code as the local service.
Online Q&A and live diagnosis use a separately hosted backend when configured.
"""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

from app import PAGE, render_result


ROOT = Path(__file__).parent
OUTPUT = ROOT / "docs"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--api-base", default="", help="HTTPS origin of the separately hosted Q&A backend")
    args = parser.parse_args()
    api_base = args.api_base.rstrip("/")
    if api_base:
        parsed = urlparse(api_base)
        if parsed.scheme != "https" or not parsed.netloc or parsed.path or parsed.username or parsed.password:
            parser.error("--api-base must be an HTTPS origin without a path or credentials")

    diagnosis_dir = OUTPUT / "diagnosis"
    diagnosis_dir.mkdir(exist_ok=True)
    for samples in (50, 100, 200):
        for lag in (1, 2, 3):
            html = render_result(samples, lag)
            (diagnosis_dir / f"{samples}-{lag}.json").write_text(
                json.dumps({"html": html}, ensure_ascii=False), encoding="utf-8"
            )

    configuration = json.dumps({"staticMode": True, "apiBase": api_base}, ensure_ascii=False)
    page = PAGE.replace(
        "<script>",
        f'<script>window.TEP_DEPLOYMENT = {configuration};</script><script>',
        1,
    )
    status = "GitHub Pages：在线问答与实时诊断已接入" if api_base else "GitHub Pages 演示：知识问答需独立后端"
    page = page.replace("{configuration_status}", status)
    page = page.replace("{diagnose_result}", "").replace("{qa_result}", "")
    page = page.replace(" · 本地研究演示", " · 公开交互演示")
    note = ("此页面可直接体验工艺动画、在线知识问答和实时故障诊断，无需登录或访问口令。"
            if api_base else
            "此公开页面可体验工艺动画和预计算的故障诊断结果（9组参数）。在线知识问答暂未启用；本地运行版本可使用完整功能。")
    page = page.replace(
        '<div class="chat-toolbar">',
        f'<p class="deployment-note" role="status">{note}</p><div class="chat-toolbar">',
        1,
    )
    (OUTPUT / "index.html").write_text(page, encoding="utf-8")
    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {OUTPUT / 'index.html'} and nine diagnosis responses")


if __name__ == "__main__":
    main()
