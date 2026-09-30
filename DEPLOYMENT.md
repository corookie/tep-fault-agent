# 部署说明 / Deployment Guide

## 中文

### 当前部署

- 前端：<https://corookie.github.io/tep-fault-agent/>
- Python 后端：<https://tep-fault-agent-api.onrender.com>
- 健康检查：<https://tep-fault-agent-api.onrender.com/health>
- Render：免费 Python 3.12 服务，Singapore 区域。模型密钥和独立访问口令保存在服务端环境变量。

网页首次问答或诊断会询问访问口令。项目持有者本机的口令保存在 `~/.tep-fault-agent/render-access-token`；请仅提供给获准使用的人，不要提交到仓库。免费实例闲置后会休眠，首次请求可能等待约一分钟或更久；网页超时为两分钟。当前使用公开仓库来源，更新后端代码后应在 Render 控制台确认是否触发部署，必要时选择 Manual Deploy → Deploy latest commit。

### 当前公开页面

GitHub Pages 从 `main` 分支的 `docs/` 目录发布：<https://corookie.github.io/tep-fault-agent/>。

该页面使用同一套工艺 SVG、样式和交互代码。未接入后端时，诊断的50/100/200点与1/2/3阶时滞共9组结果由 `export_pages.py` 在构建时调用当前 Python 算法生成，页面加载相应 JSON。接入后端后，问答与诊断均请求在线 Python 服务。更新算法后，先运行 `python3 export_pages.py --api-base https://tep-fault-agent-api.onrender.com`，再提交生成文件。

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
| `TEP_ACCESS_TOKEN` | 另设一串随机访问口令，放在服务端私密环境变量中；它不是模型 API Key |

仓库根目录的 `render.yaml` 已设置免费 Python 服务、依赖安装、检索索引构建、启动命令和健康检查；`.python-version` 固定 Python 3.12。部署时需在 Render 后台分别填写 `TEP_LLM_API_KEY` 与 `TEP_ACCESS_TOKEN`，不要提交它们的值。Render 上缺少任一项时，服务会拒绝启动。网页首次调用线上接口时会询问访问口令，并仅在当前浏览器会话中保存；访问口令不能代替模型服务的消费上限。

后端有正式 HTTPS 域名后，在项目目录执行：

```bash
python3 export_pages.py --api-base https://YOUR-BACKEND-HOST
git add docs/index.html docs/diagnosis
git commit -m "Connect hosted Q&A backend"
git push
```

这里的`--api-base`是公开后端地址，不能包含 Key。后端访问口令校验所有计算与问答 POST 请求；只设置 CORS 并不能阻止别人从服务器直接请求接口。投入使用后仍应设置模型消费上限并检查托管服务日志。不要把模型密钥放到 GitHub Pages、网页本地存储或 GitHub Actions 构建产物里。

## English

### Current deployment

- Frontend: <https://corookie.github.io/tep-fault-agent/>
- Python backend: <https://tep-fault-agent-api.onrender.com>
- Health endpoint: <https://tep-fault-agent-api.onrender.com/health>
- Render: free Python 3.12 service in Singapore, with both secrets stored in server-side environment variables.

The owner’s local access-token file is `~/.tep-fault-agent/render-access-token`; share it only with approved users and never commit it. The free instance sleeps when idle, and waking it may take around a minute or longer. The browser timeout is two minutes. With the public repository source, verify that a deployment starts after backend changes; otherwise use Manual Deploy → Deploy latest commit.

### Published website

GitHub Pages serves the `docs/` folder on `main` at <https://corookie.github.io/tep-fault-agent/>. The process SVG remains interactive. Q&A and diagnosis use the hosted Python backend when an API base is configured. Without an API base, the exported page loads one of nine precomputed diagnosis results. Local mode also calculates on demand.

### Hosting online Q&A

Pages cannot execute Python or protect an API key. Use a separate Python host. The repository includes a free-plan `render.yaml` that installs dependencies, rebuilds the retrieval index, starts `app.py`, and checks `/health`. Set `TEP_HOST=0.0.0.0`, use the provider's `PORT`, store `TEP_LLM_API_KEY` and a separate random `TEP_ACCESS_TOKEN` as private runtime variables, and set `TEP_ALLOWED_ORIGIN=https://corookie.github.io`. Render deployments refuse to start without both secrets. `TEP_LLM_BASE_URL` and `TEP_LLM_MODEL` may override the defaults.

Once the backend has an HTTPS origin, run `python3 export_pages.py --api-base https://YOUR-BACKEND-HOST` and push the generated `docs/` files. The API base is public; the model key never enters the site output. The page asks for the separate access token on its first online request and stores it only for that browser session. Both Q&A and diagnosis then run on the backend. Configure model spending limits and inspect service logs as well; CORS alone does not block direct server-to-server calls.
