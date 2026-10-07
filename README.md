# TEP 故障助手 / TEP Fault Assistant

这是一个围绕 Tennessee Eastman Process（TEP）构建的网页，包含过程介绍、智能助手和故障根源诊断三个独立 Tab。顶部导航和页面底部的文字箭头都可以切换功能，无需沿长页面往下找。

## 网页由哪三部分组成

### 01 过程介绍

用可交互的工艺图介绍 TEP 的主要设备与物流。页面展示反应器、冷凝器、汽液分离器、循环压缩机和汽提塔；约 8 秒一轮的动画演示原料进入、反应、分离、循环以及产品输出。点击设备可以查看它的作用和相连的物流。这一部分帮助第一次接触 TEP 的人建立整体认识。

### 02 智能助手

在聊天窗口提问，例如“汽提塔有什么作用？”或“IDV(7) 是什么故障？”。聊天记录按时间排列，输入框固定在聊天窗口底部；点击示例问题只填入输入框。助手从 TEP 知识手册中检索相关片段，再由在线大模型组织答案，并附上可展开的资料依据。知识范围包括工艺流程、设备、变量含义和预设故障；支持围绕上一问继续追问。资料不足或问题超出范围时，助手会明确说明。切换 Tab 会保留当前对话和诊断结果。

### 03 故障根源诊断

以 TEP 的 IDV(7) 仿真故障为案例，选择故障后的采样点数和历史时滞，点击“开始分析”。页面给出可能的根源变量、变量间的格兰杰预测关系图和候选故障传播路径；点击路径可以在关系图中高亮对应变量与箭头。还可以查看关系矩阵及计算依据，比较不同参数下的结果。

这部分是**基于数据的线索分析**：图中的箭头表示一个变量的历史数据有助于预测另一个变量，并不能单凭这张图证明物理因果或确认真实根因。

## 怎么使用

### 在线体验

打开 [TEP 故障助手](https://corookie.github.io/tep-fault-agent/)，可使用工艺介绍、在线知识问答和实时故障诊断。前端由 GitHub Pages 托管，问答与诊断请求 [Render 上的 Python 后端](https://tep-fault-agent-api.onrender.com)。所有访问者都可以直接提问和诊断，无需登录或访问口令。模型 API Key 保存在后端环境变量中，不发送到浏览器。

后端使用 Render 免费实例，闲置后会休眠；重新访问时可能需要等待约一分钟或更久。网页最多等待两分钟，超时可稍后重试。未配置后端地址时，导出页面仍支持 9 组预计算诊断结果。

### 本地运行完整版本

准备 Python 环境和阿里云百炼的**模型 API Key**。依次执行：

```bash
git clone https://github.com/corookie/tep-fault-agent.git
cd tep-fault-agent
python -m pip install -r requirements.txt
python retrieve_chunks.py build
python configure_local.py
python app.py
```

首次运行 `configure_local.py` 时，按终端的隐藏输入提示保存 Key；以后启动只需运行 `python app.py`。打开 `http://127.0.0.1:8765/`，即可依次体验工艺介绍、知识问答和故障诊断。检索索引包含本机路径，因此首次克隆到新电脑后需要执行一次 `python retrieve_chunks.py build`。

Key 保存在当前用户的本地配置文件，不写入仓库或网页源码。也可以在服务端设置 `TEP_LLM_API_KEY`、`TEP_LLM_BASE_URL` 和 `TEP_LLM_MODEL` 环境变量。这里需要的是百炼模型 API Key，不是阿里云 AccessKey ID/Secret。

项目也支持 DeepSeek 官方 API：设置 `TEP_LLM_API_KEY` 为 DeepSeek Key、`TEP_LLM_BASE_URL=https://api.deepseek.com` 和 `TEP_LLM_MODEL=deepseek-flash`，然后启动服务。三项必须匹配同一个服务商，具体配置见[部署说明](DEPLOYMENT.md)。上面的 `configure_local.py` 流程仍用于百炼本地配置。

## 技术与项目文档

- **过程介绍：** SVG 工艺图、设备交互和循环动画。
- **知识问答：** 结构化知识手册切分、检索、追问补全、在线大模型生成和资料引用。
- **故障诊断：** `scikit-learn` 核岭回归比较预测误差，筛选格兰杰预测关系，并展示关系图与候选路径。当前案例使用 IDV(7) 数据中的 7 个变量；这是论文方法的最小工程版本，不能视为完整复现。

制作过程、关键实现、结果限制和面试追问见[中文技术手册](docs/TECHNICAL_GUIDE_ZH.md)及 [English technical overview](docs/TECHNICAL_OVERVIEW_EN.md)。部署方式见[双语部署说明](DEPLOYMENT.md)，数据来源见[数据说明](data/README.md)。本地回归检查可运行 `python -m unittest discover -q`。

## English

TEP Fault Assistant is a web application built around the Tennessee Eastman Process (TEP). Three independent tabs provide a process overview, a knowledge assistant, and root-cause exploration. Use the top navigation or the text-and-arrow links at the bottom of each view to switch between them.

### What is on the page?

**01 Process overview.** An interactive SVG diagram explains the reactor, condenser, vapor–liquid separator, recycle compressor, and stripper. An approximately eight-second loop shows material moving from feed to product. Click a device to see its role and connected streams.

**02 Knowledge assistant.** Ask about the process, equipment, variables, or predefined faults. Messages appear in chronological order above the bottom input area. Example questions fill the input without moving the page. The application retrieves passages from its TEP handbook and sends the relevant material to an online language model, which answers with expandable source references. It supports limited follow-up questions and says when the available material is insufficient. Switching tabs preserves the current conversation and diagnosis results.

**03 Root-cause exploration.** Using the IDV(7) simulated fault, choose a post-fault sample window and time lag, then start the analysis. The page shows candidate root variables, a directed graph of Granger-predictive relationships, and candidate propagation paths. Selecting a path highlights it in the graph. These are predictive clues under the selected settings, **not proof of physical causality**.

### How to use it

Open [TEP Fault Assistant](https://corookie.github.io/tep-fault-agent/) for the process diagram, online Q&A, and live diagnosis. GitHub Pages hosts the frontend; a [Python service on Render](https://tep-fault-agent-api.onrender.com) handles Q&A and diagnosis. All visitors can ask questions and run diagnosis without signing in or entering an access token. The model API key stays in server-side environment variables and is never sent to the browser.

The free Render instance sleeps when idle; waking it can take around a minute or longer. The page waits up to two minutes; retry later if it times out. Exports without a backend URL still support nine precomputed diagnosis settings. To run locally:

```bash
git clone https://github.com/corookie/tep-fault-agent.git
cd tep-fault-agent
python -m pip install -r requirements.txt
python retrieve_chunks.py build
python configure_local.py
python app.py
```

On the first run, `configure_local.py` asks for an Alibaba Cloud Bailian **model API key** through a hidden terminal prompt. After that, start the server with `python app.py` and open `http://127.0.0.1:8765/`. The key stays in a private local configuration file, never in the repository or browser code. Rebuild the retrieval index once after cloning because it contains local file paths. Server-side environment variables `TEP_LLM_API_KEY`, `TEP_LLM_BASE_URL`, and `TEP_LLM_MODEL` are also supported.

The official DeepSeek API is also supported. Set `TEP_LLM_API_KEY` to your DeepSeek key, `TEP_LLM_BASE_URL=https://api.deepseek.com`, and `TEP_LLM_MODEL=deepseek-flash` before starting the server. All three settings must match the same provider; see the [deployment guide](DEPLOYMENT.md). The `configure_local.py` flow above remains specific to local Bailian configuration.

### Implementation and documentation

The process view uses SVG and browser animation. The assistant combines structured handbook retrieval with an online language model and cited answers. The diagnosis compares kernel-ridge predictors to identify Granger-predictive relationships in seven IDV(7) variables, then visualizes candidate paths. This is a minimal engineering version of the thesis method, not a full reproduction.

See the [Chinese implementation and interview guide](docs/TECHNICAL_GUIDE_ZH.md), [English technical overview](docs/TECHNICAL_OVERVIEW_EN.md), [bilingual deployment guide](DEPLOYMENT.md), and [data provenance](data/README.md). Run `python -m unittest discover -q` for the local regression suite.
