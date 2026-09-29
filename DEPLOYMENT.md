# 部署说明 / Deployment Guide

## 中文

### 当前公开页面

GitHub Pages 从 `main` 分支的 `docs/` 目录发布：<https://corookie.github.io/tep-fault-agent/>。

该页面使用同一套工艺 SVG、样式和交互代码。诊断的50/100/200点与1/2/3阶时滞共9组结果由 `export_pages.py` 在构建时调用当前 Python 算法生成，页面加载相应 JSON。因此公开页面展示的是预计算结果；本地版点击诊断时才重新运行算法。更新算法后，先运行 `python3 export_pages.py`，再提交生成文件。

### 在线问答为什么需要独立服务

GitHub Pages 只托管静态文件，不运行 Python。浏览器脚本对所有访问者可见，不能放模型 API Key。仓库中的页面不会读入或上传本机密钥文件。在线问答要由独立 Python 服务接收请求、检索本地知识库并使用服务端环境变量中的 Key 调用模型。

### Python 后端部署参数

选择支持 Python 常驻进程的托管服务后，使用这些配置：

| 名称 | 值或作用 |
| --- | --- |
| 构建 | `python -m pip install -r requirements.txt`，然后 `python retrieve_chunks.py build` |
| 启动 | `python app.py` |
| `TEP_HOST` | `0.0.0.0`，使托管平台可转发请求；本机默认仍为 `127.0.0.1` |
| `PORT` | 由平台注入；本机默认8765 |
| `TEP_LLM_API_KEY` | 放在托管平台的私密环境变量，绝不提交到仓库 |
| `TEP_LLM_BASE_URL` | 默认百炼兼容接口地址；可在平台上覆盖 |
| `TEP_LLM_MODEL` | 默认 `qwen3.8-flash`；可在平台上覆盖 |
| `TEP_ALLOWED_ORIGIN` | `https://corookie.github.io`，只允许该浏览器来源读取跨域响应 |

后端有正式 HTTPS 域名后，在项目目录执行：

```bash
python3 export_pages.py --api-base https://YOUR-BACKEND-HOST
git add docs/index.html docs/diagnosis
git commit -m "Connect hosted Q&A backend"
git push
```

这里的`--api-base`是公开后端地址，不能包含 Key。只设置CORS并不能防止别人从服务器直接请求公开接口；将公开问答投入使用前，还应设置调用限额、成本上限或访问控制，并检查托管服务日志。不要把密钥放到 GitHub Pages、网页本地存储或 GitHub Actions 构建产物里。

## English

### Published preview

GitHub Pages serves the `docs/` folder on `main` at <https://corookie.github.io/tep-fault-agent/>. The process SVG remains interactive. The nine supported diagnosis parameter combinations are generated ahead of time by the current Python implementation and served as JSON. Local mode performs the calculation on demand; the Pages preview loads the matching precomputed result.

### Hosting online Q&A

Pages cannot execute Python or protect an API key. Use a separate Python host. Install `requirements.txt`, rebuild the retrieval index with `python retrieve_chunks.py build`, and start `python app.py`. Set `TEP_HOST=0.0.0.0`, use the provider's `PORT`, store `TEP_LLM_API_KEY` as a private runtime environment variable, and set `TEP_ALLOWED_ORIGIN=https://corookie.github.io`. `TEP_LLM_BASE_URL` and `TEP_LLM_MODEL` may override the defaults.

Once the backend has an HTTPS origin, run `python3 export_pages.py --api-base https://YOUR-BACKEND-HOST` and push the generated `docs/` files. The API base is public; the model key never enters the site output. CORS alone does not block direct server-to-server calls, so apply usage limits, a spending cap, or access control before making the Q&A endpoint public.
