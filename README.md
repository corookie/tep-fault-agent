# TEP 故障助手 / TEP Fault Assistant

这是一个围绕 Tennessee Eastman Process（TEP）构建的网页：先认识化工过程，再查询相关知识，最后用数据分析故障可能从哪里开始传播。页面按这个顺序分为三个部分。

## 网页由哪三部分组成

### 01 过程介绍

用可交互的工艺图介绍 TEP 的主要设备与物流。页面展示反应器、冷凝器、汽液分离器、循环压缩机和汽提塔；约 8 秒一轮的动画演示原料进入、反应、分离、循环以及产品输出。点击设备可以查看它的作用和相连的物流。这一部分帮助第一次接触 TEP 的人建立整体认识。

### 02 智能助手

在聊天窗口提问，例如“汽提塔有什么作用？”或“IDV(7) 是什么故障？”。助手从 TEP 知识手册中检索相关片段，再由在线大模型组织答案，并附上可展开的资料依据。知识范围包括工艺流程、设备、变量含义和预设故障；支持围绕上一问继续追问。资料不足或问题超出范围时，助手会明确说明。

### 03 故障根源诊断

以 TEP 的 IDV(7) 仿真故障为案例，选择故障后的采样点数和历史时滞，点击“开始分析”。页面给出可能的根源变量、变量间的格兰杰预测关系图和候选故障传播路径；点击路径可以在关系图中高亮对应变量与箭头。还可以查看关系矩阵及计算依据，比较不同参数下的结果。

这部分是**基于数据的线索分析**：图中的箭头表示一个变量的历史数据有助于预测另一个变量，并不能单凭这张图证明物理因果或确认真实根因。

## 怎么使用

### 在线体验

打开 [GitHub Pages 预览](https://corookie.github.io/tep-fault-agent/)。工艺图可以交互；诊断部分提供 9 组预先计算的参数组合，供浏览和比较。**在线知识问答在此预览中不可用**，因为 GitHub Pages 只能托管静态文件，无法运行 Python 服务或安全保存模型 API Key。要使用全部三个功能，请在本地运行。

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

## 技术与项目文档

- **过程介绍：** SVG 工艺图、设备交互和循环动画。
- **知识问答：** 结构化知识手册切分、检索、追问补全、在线大模型生成和资料引用。
- **故障诊断：** `scikit-learn` 核岭回归比较预测误差，筛选格兰杰预测关系，并展示关系图与候选路径。当前案例使用 IDV(7) 数据中的 7 个变量；这是论文方法的最小工程版本，不能视为完整复现。

制作过程、关键实现、结果限制和面试追问见[中文技术手册](docs/TECHNICAL_GUIDE_ZH.md)及 [English technical overview](docs/TECHNICAL_OVERVIEW_EN.md)。部署方式见[双语部署说明](DEPLOYMENT.md)，数据来源见[数据说明](data/README.md)。本地回归检查可运行 `python -m unittest discover -q`。

## English

TEP Fault Assistant is a web application built around the Tennessee Eastman Process (TEP). Its three sections follow one workflow: **understand the process → ask a technical question → explore fault data**.

### What is on the page?

**01 Process overview.** An interactive SVG diagram explains the reactor, condenser, vapor–liquid separator, recycle compressor, and stripper. An approximately eight-second loop shows material moving from feed to product. Click a device to see its role and connected streams.

**02 Knowledge assistant.** Ask about the process, equipment, variables, or predefined faults. The application retrieves passages from its TEP handbook and sends the relevant material to an online language model, which answers with expandable source references. It supports limited follow-up questions and says when the available material is insufficient.

**03 Root-cause exploration.** Using the IDV(7) simulated fault, choose a post-fault sample window and time lag, then start the analysis. The page shows candidate root variables, a directed graph of Granger-predictive relationships, and candidate propagation paths. Selecting a path highlights it in the graph. These are predictive clues under the selected settings, **not proof of physical causality**.

### How to use it

Open the [GitHub Pages preview](https://corookie.github.io/tep-fault-agent/) to explore the process diagram and nine precomputed diagnosis settings. Online Q&A is unavailable in that static preview. Run the project locally for all three features:

```bash
git clone https://github.com/corookie/tep-fault-agent.git
cd tep-fault-agent
python -m pip install -r requirements.txt
python retrieve_chunks.py build
python configure_local.py
python app.py
```

On the first run, `configure_local.py` asks for an Alibaba Cloud Bailian **model API key** through a hidden terminal prompt. After that, start the server with `python app.py` and open `http://127.0.0.1:8765/`. The key stays in a private local configuration file, never in the repository or browser code. Rebuild the retrieval index once after cloning because it contains local file paths. Server-side environment variables `TEP_LLM_API_KEY`, `TEP_LLM_BASE_URL`, and `TEP_LLM_MODEL` are also supported.

### Implementation and documentation

The process view uses SVG and browser animation. The assistant combines structured handbook retrieval with an online language model and cited answers. The diagnosis compares kernel-ridge predictors to identify Granger-predictive relationships in seven IDV(7) variables, then visualizes candidate paths. This is a minimal engineering version of the thesis method, not a full reproduction.

See the [Chinese implementation and interview guide](docs/TECHNICAL_GUIDE_ZH.md), [English technical overview](docs/TECHNICAL_OVERVIEW_EN.md), [bilingual deployment guide](DEPLOYMENT.md), and [data provenance](data/README.md). Run `python -m unittest discover -q` for the local regression suite.
