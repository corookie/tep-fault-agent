"""在本机终端隐藏输入百炼 API Key 后启动故障助手；密钥不落盘。"""

import getpass
import os

from app import serve


DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_MODEL = "qwen3.8-flash"


def main() -> None:
    print("请输入百炼模型 API Key；不要输入 LTAI 开头的 AccessKey ID 或 AccessKey Secret。")
    api_key = getpass.getpass("百炼 API Key（输入时不显示）：").strip()
    if not api_key:
        raise SystemExit("未输入 API Key，已取消启动。")
    if api_key.startswith("LTAI"):
        raise SystemExit("这看起来是 AccessKey ID。请到百炼控制台创建模型 API Key。")
    base_url = input(f"API 地址 [{DEFAULT_BASE_URL}]：").strip() or DEFAULT_BASE_URL
    model = input(f"模型名称 [{DEFAULT_MODEL}]：").strip() or DEFAULT_MODEL

    os.environ["TEP_LLM_API_KEY"] = api_key
    os.environ["TEP_LLM_BASE_URL"] = base_url
    os.environ["TEP_LLM_MODEL"] = model
    print("密钥仅保留在当前进程内；关闭程序后需重新输入。")
    serve()


if __name__ == "__main__":
    main()
