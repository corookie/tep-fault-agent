"""本地聊天页面与 API Key 持久化的回归检查。"""

import json
import os
import stat
import tempfile
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from unittest.mock import patch
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

import app


class AppTests(unittest.TestCase):
    def test_hosted_api_requires_access_token_without_exposing_model_key(self) -> None:
        with patch.dict(os.environ, {"TEP_ACCESS_TOKEN": "test-access-only"}):
            server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
            thread = Thread(target=server.serve_forever, daemon=True)
            thread.start()
            root = f"http://127.0.0.1:{server.server_port}/"
            try:
                self.assertEqual(json.load(urlopen(root + "health")), {"status": "ok"})
                page = urlopen(root).read().decode("utf-8")
                self.assertNotIn("test-access-only", page)
                with patch.object(app, "answer_question", return_value={"answer": "ok"}) as answer:
                    for route in ("api/ask", "ask", "api/diagnose", "run"):
                        with self.assertRaises(HTTPError) as error:
                            urlopen(Request(root + route, data=b"question=X4"))
                        self.assertEqual(error.exception.code, 401)
                    answer.assert_not_called()
                    request = Request(root + "api/ask", data=b"question=X4",
                                      headers={"Authorization": "Bearer test-access-only"})
                    self.assertEqual(json.load(urlopen(request))["answer"], "ok")
                    answer.assert_called_once()
            finally:
                server.shutdown()
                server.server_close()

    def test_hosted_api_only_advertises_configured_browser_origin(self) -> None:
        with patch.dict(os.environ, {"TEP_ALLOWED_ORIGIN": "https://corookie.github.io"}):
            server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
            thread = Thread(target=server.serve_forever, daemon=True)
            thread.start()
            url = f"http://127.0.0.1:{server.server_port}/api/ask"
            try:
                with patch.object(app, "answer_question", return_value={"answer": "ok", "sources": []}):
                    for origin, expected in [
                        ("https://corookie.github.io", "https://corookie.github.io"),
                        ("https://example.org", None),
                    ]:
                        request = Request(url, data=b"question=X4", headers={"Origin": origin})
                        with urlopen(request) as response:
                            self.assertEqual(response.headers.get("Access-Control-Allow-Origin"), expected)
            finally:
                server.shutdown()
                server.server_close()

    def test_diagnosis_api_returns_graphs_and_updates_for_empty_window(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        Thread(target=server.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{server.server_port}/api/diagnose"
        try:
            for samples, expected in [(100, 'X4 → X20 → X46'), (50, '当前窗口没有筛出关系')]:
                request = Request(url, data=urlencode({'samples': samples, 'lag': 3}).encode())
                with urlopen(request) as response:
                    html = json.load(response)['html']
                self.assertEqual(html.count('<svg '), 2)
                self.assertIn(expected, html)
                self.assertIn('列为驱动变量', html)
                self.assertIn('候选故障传播路径', html)
        finally:
            server.shutdown()
            server.server_close()

    def test_chat_and_saved_key_work_after_restart(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            key_dir = Path(temporary) / "config"
            key_file = key_dir / "bailian-api-key"
            with patch.object(app, "KEY_DIR", key_dir), patch.object(app, "KEY_FILE", key_file), patch.dict(os.environ, {}):
                server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
                thread = Thread(target=server.serve_forever, daemon=True)
                thread.start()
                root = f"http://127.0.0.1:{server.server_port}/"
                try:
                    page = urlopen(root).read().decode("utf-8")
                    self.assertIn('id="chat-log"', page)
                    self.assertIn("protectedPost('/api/ask'", page)
                    self.assertNotIn('id="config-form"', page)
                    self.assertNotIn('type="password"', page)
                    self.assertNotIn('config_token', page)
                    app.save_key("sk-local-test-only")
                    for route in ('configure', 'api/configure'):
                        for method in ('GET', 'POST'):
                            request = Request(root + route, method=method,
                                              data=b'api_key=sk-replacement' if method == 'POST' else None)
                            with self.assertRaises(HTTPError) as error:
                                urlopen(request)
                            self.assertEqual(error.exception.code, 404)
                    self.assertEqual(stat.S_IMODE(key_dir.stat().st_mode), 0o700)
                    self.assertEqual(stat.S_IMODE(key_file.stat().st_mode), 0o600)
                    self.assertEqual(key_file.read_text(), "sk-local-test-only")
                    self.assertNotIn("sk-local-test-only", urlopen(root).read().decode("utf-8"))

                    os.environ.pop("TEP_LLM_API_KEY", None)
                    app.load_saved_key()
                    self.assertEqual(os.environ["TEP_LLM_API_KEY"], "sk-local-test-only")

                    with patch.object(app, "answer_question", return_value={
                        "answer": "IDV(7) 是 C 进料压力损失。[1]", "sources": []
                    }) as answer:
                        request = Request(root + "api/ask", data=urlencode({
                            "question": "它是什么故障？", "previous_question": "IDV(7) 是什么？"
                        }).encode())
                        with urlopen(request) as response:
                            self.assertIn("压力损失", json.load(response)["answer"])
                        answer.assert_called_once_with("它是什么故障？", previous_question="IDV(7) 是什么？")
                finally:
                    server.shutdown()
                    server.server_close()


if __name__ == "__main__":
    unittest.main()
