# TEP 故障助手 / TEP Fault Assistant

中文说明在前；[English](#english) follows below.

三个功能的制作过程、当前代码实现、算法计算示例、28个面试追问和动手练习，见 [项目技术实现与面试手册](docs/TECHNICAL_GUIDE_ZH.md)（2026-09-29核对）。
英文技术概览见 [Technical Overview](docs/TECHNICAL_OVERVIEW_EN.md)。

完整交付说明、五分钟演示、验收结果与面试表述见 [PROJECT_GUIDE.md](PROJECT_GUIDE.md)。

页面已按“了解工艺 → 知识查证 → 故障诊断”完成整页重构，设备和候选变量可带着问题进入问答，诊断图与候选路径联动。界面、交互与验收记录见 [PRODUCT_REDESIGN.md](PRODUCT_REDESIGN.md)。

项目有三个功能：用8秒循环动画介绍TEP过程；回答TEP领域知识问题；用核岭回归分析IDV(7)数据，给出候选变量和预测关系。三者都在同一个页面中；过程图说明见 [PROCESS_OVERVIEW.md](PROCESS_OVERVIEW.md)。

## 运行

在项目目录安装依赖。若使用阿里云百炼，先到[百炼 API Key 页面](https://bailian.console.aliyun.com/)创建**模型 API Key**；阿里云 AccessKey ID/Secret 不用于这里的模型调用。然后运行：

```bash
python -m pip install -r requirements.txt
python retrieve_chunks.py build  # 首次克隆到新电脑后，重建本机检索索引
python configure_local.py  # 首次配置；已有密钥则跳过
python app.py
```

首次在终端运行 `python configure_local.py`，按隐藏输入提示保存 API Key，再启动服务。已有配置无需重新输入。浏览器打开 `http://127.0.0.1:8765` 即可使用，网页不再提供密钥设置入口，旧配置接口也已移除。密钥保存在本机 `~/.tep-fault-agent/bailian-api-key`，目录权限为 700、文件权限为 600；服务重启后自动读取，不写入网页源码或项目文件。服务端默认使用**华北2（北京）**的 `qwen3.8-flash`；其他地域可用下面的手动配置方式。知识问答以聊天窗口呈现，每个页面仅保存上一条补全后的问题；刷新或点击“新对话”会清空。追问有歧义时要求用户补充编号；问题和匹配到的参考条目会发给在线模型。故障诊断无需调用模型。

也可手动设置 `TEP_LLM_API_KEY`、`TEP_LLM_BASE_URL`、`TEP_LLM_MODEL` 三个环境变量，再运行 `python app.py`。

若需要保存诊断的完整 JSON 结果，运行 `python diagnose.py`；例如 `python diagnose.py --samples 200 --lag 3` 可以比较不同时间窗。

诊断默认读取公开的 `data/raw/d07_te.dat`，从第 161 个采样点开始；变量采用论文实验中选出的 X4、X7、X13、X16、X20、X45、X46。

知识问答现已使用 [TEP_SOURCE_MAP.md](TEP_SOURCE_MAP.md) 切分出的110个片段，加载本地索引，通过编号/意图规则和追问补全检索前5块，再交给在线模型。明显偏题、歧义或无结果时不调用模型；分别提示范围外、需要澄清或资料不足；模型阅读资料后也可以明确弃答；引用可展开到片段正文与来源位置。原 knowledge.json 保留作旧版记录，不再参与当前问答。诊断功能调用第三方库 `scikit-learn` 的 `KernelRidge`，默认使用故障后的 100 个采样点。

诊断图升级说明见 [DIAGNOSIS_GRAPHS.md](DIAGNOSIS_GRAPHS.md)：分析后展示关系矩阵、有向图、统计反馈环与候选传播路径，且不刷新聊天窗口。点击候选路径可联动高亮有向图，默认显示3条，其余折叠。计算依据保留在折叠区，说明预测误差降低和排序的含义。

## 如何读结果

IDV(7) 的仿真设定是 C 进料压力损失；X4 是混合进料流量，X45 是相应阀门开度。算法只能评估记录变量之间的**时序预测关系**，不能直接观测或证明压力损失。X4 与 X45 可能形成控制反馈，所以候选并列是可以讨论的结果。

100 点和 200 点的分析可能给出不同的排名。时序测试点也可能彼此相关，因此本版 p/q 值只作探索性参考。不要把单次排名写成“已确认物理根因”；面试展示时应同时说明数据窗口、参数和上述限制。

诊断是论文方法的最小工程版；论文中 PCA 变量选择、BIC 选阶、FIR 滤波和 20 点样本结果尚未复现。在线问答已通过本地模拟测试及真实模型网页连续问答验证，详情见 [本轮接入记录](WEB_RAG_RELEASE.md)。这只是本地单用户版本，尚不能据此认定生产验收通过。

数据来源及检查记录见 [data/README.md](data/README.md)。

后续知识库、界面和诊断的迭代顺序及验收点见 [ITERATION_PLAN.md](ITERATION_PLAN.md)。

## GitHub Pages 公开预览

仓库的 `docs/` 目录可发布为 GitHub Pages 页面。它保留交互式工艺图，并提供当前程序对9组采样点数/时滞参数预先计算的诊断结果。运行 `python3 export_pages.py` 可重新生成页面和结果。GitHub Pages 无法运行 Python，也不能安全保存模型 API Key，因此公开预览中的在线问答暂不可用；完整三功能版本可按上面的步骤在本机运行。接入独立后端后应将 Key 放在后端环境变量中，不要写进公开源码或浏览器脚本。

已上线地址和后端接入方式见 [双语部署说明](DEPLOYMENT.md)。

## English

### Overview

TEP Fault Assistant combines three features in one web interface:

1. An interactive SVG overview of the Tennessee Eastman Process, with an eight-second material-flow animation.
2. A domain question-answering assistant. It retrieves relevant passages from a curated TEP handbook and asks an online language model to answer with source references.
3. A root-cause exploration tool for the IDV(7) fault data. It compares full and restricted kernel-ridge predictors, filters Granger-predictive relationships, and displays candidate root variables, a directed graph, and candidate propagation paths.

The intended workflow is **understand the process → check a technical question → inspect the fault data**. The graph reports predictive relationships under a chosen window and model; it does not by itself prove a physical root cause.

### Local setup

```bash
python -m pip install -r requirements.txt
python retrieve_chunks.py build  # Rebuild the local retrieval index after cloning.
python configure_local.py  # First run only; enter the model API key using the hidden prompt.
python app.py
```

Open `http://127.0.0.1:8765/`. The server reads the API key from a private file in the user's home directory. Alternatively, configure `TEP_LLM_API_KEY`, `TEP_LLM_BASE_URL`, and `TEP_LLM_MODEL` in the server environment. Never place the key in browser JavaScript or the repository.

The handbook is split into 110 structured passages. Retrieval uses character-level TF-IDF plus entity and intent rules, then sends up to five passages to the language model. A limited follow-up resolver handles cases such as “And fault 15?” after a question about IDV(14). The diagnosis uses the seven variables X4, X7, X13, X16, X20, X45, and X46, starting at sample 161 of the public IDV(7) data.

Run `python -m unittest discover -q` for the local regression suite. Read the [English technical overview](docs/TECHNICAL_OVERVIEW_EN.md) or the [full Chinese implementation and interview guide](docs/TECHNICAL_GUIDE_ZH.md). Other detailed project notes are currently in Chinese. Data provenance is in [data/README.md](data/README.md).

### Deployment note

GitHub Pages can publish the static web interface, but it cannot run Python or keep an API key secret. Online Q&A therefore requires a separate backend. Keep the API key as a server-side secret on that backend; the static page must never contain it. The repository includes the original local Python application so the full three-feature version remains reproducible.

See the [bilingual deployment guide](DEPLOYMENT.md) for the live preview, configuration, and backend integration steps.
