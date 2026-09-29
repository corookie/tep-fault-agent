# 追问怎样进入检索

后续更新：网页现已接入，当前状态见 [WEB_RAG_RELEASE.md](WEB_RAG_RELEASE.md)。下文保留本阶段最初的离线设计记录。

本阶段增加 `followup_query.py`，把依赖上一轮的问题补成可独立检索的问题。仍然使用本地规则和文本索引，不调用模型、不产生 API 费用，也尚未接入网页问答。

先看 [实际运行示例](retrieval_build/FOLLOWUP_DEMO.md)，其中包含原问题、补全结果、判断依据和命中片段原文。

## 处理流程

1. **先检查当前问题是否独立。** “X15是什么变量？”明确指定对象，直接处理，不继承上一轮故障编号。
2. **识别省略或指代。** “那15呢？”继承上一轮唯一主体的类型和问法；“它的单位是什么？”用上一轮主体替换“它”，保留当前问题的意图。
3. **不能确定就澄清。** 没有历史、上一问涉及多个主体、指代类型冲突或编号越界时，返回澄清提示，不检索附近编号来猜答案。“前者”“它们”等复杂指代暂不支持。
4. **重新解析并检索。** 对补全问题运行已有编号与意图规则；当前主体优先，上一轮不同主体可作辅助证据。上一主体不替代当前主体，也不等于用户要求比较两者。

例如：

| 上一问 | 当前问 | 处理结果 |
| --- | --- | --- |
| IDV(14)是什么故障？ | 那15呢？ | IDV(15)是什么故障？ |
| X14是什么变量？ | 那15呢？ | X15是什么变量？ |
| X4是什么变量？ | 它的单位是什么？ | X4的单位是什么？ |
| X4和X45有什么区别？ | 它的单位是什么？ | 先询问具体指哪个变量 |

这说明连续问答需要处理上下文，但不要求检索器本身是大模型。当前规则只覆盖明确、有限的表达；后续可以在同一接口里比较模型改写的效果与成本。

## 保留哪些记录

- `original_query`：用户原话。
- `resolved_query`：补全后的独立问题。
- `retrieval_query`：编号标准化、别名补充后实际用于文本检索的内容。
- `resolution_status`：独立问题、已补全、需要澄清。
- `resolution_reason`、`context_used`、`previous_question`：为什么补全、用了什么历史。
- 命中片段的 `score`、`priority`、`rank_reason`：相似度与规则排序分别记录。

原始问题不会被覆盖。调试时可以区分“理解错了问题”和“问题正确但检索不到证据”。

## 会话如何保存

`ContextIndex` 是可共享的只读索引，不保存聊天历史；`ConversationRetriever` 每个实例对应一个会话，只记上一条已明确的问题。连续“14→15→16”使用最近补全的问题继续解析。

不使用助手生成的答案作为故障事实或主体依据。遇到未解决的歧义，会清空可继承状态，避免下一问跳回更早的话题。新话题覆盖旧话题，`reset()` 清空会话。当前不持久化历史，重启会丢失状态；网页接入时还需要实现会话标识、隔离与生命周期管理，不能让所有用户共用一个会话实例。

## 本地运行

在项目目录执行：

```sh
python3 retrieve_chunks.py query '那15呢？' --mode context --previous-question 'IDV(14)是什么故障？' --top-k 2
python3 retrieve_chunks.py evaluate --mode context
```

程序里可以连续调用：

```python
from retrieve_chunks import ContextIndex
from followup_query import ConversationRetriever

session = ConversationRetriever(ContextIndex())
for question in ['IDV(14)是什么故障？', '那15呢？', '那16呢？']:
    result = session.ask(question, top_k=2)
    print(result['analysis']['resolved_query'])
    print(result['clarification'] or [h['unit_id'] for h in result['hits']])
```

不指定模式时仍是原始文本检索；`--mode rules` 保留上一阶段行为。上下文评测另存 `retrieval_build/evaluation_context/`，不覆盖历史报告。

## 验证与边界

33项自动检查通过，其中13项针对追问补全、连续追问、会话隔离、重置、歧义澄清和数据范围边界，其余20项检查原有解析与检索行为。

相同索引、相同18问开发集，前3块找齐必要证据从17/18提升至18/18。这个结果只说明已登记问题的证据覆盖；不是回答正确率，也不是生产验收通过。原阈值0.16下仍只有12/18，阈值需要单独评估。

接下来需要未参与开发的追问样例检验泛化，并在网页接入后验证会话隔离、回答忠实性、引用和失败提示。知识不足不能靠补全或模型猜测解决，故障传播路径仍需区分文献设定与实验诊断结果。
