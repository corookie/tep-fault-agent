# TEP 上下文追问检索报告

本轮检索110个新片段，不调用聊天模型。这里的“完整”指预先登记的证据组全部命中，不表示回答已经正确。

评测集：tep-context-new-wordings-v1；时间：2026-09-27T04:37:06.425562+00:00。

## 总体结果

| 返回数量（不设0.16阈值） | 至少命中一组证据 | 所有必要证据齐全 |
| --- | ---: | ---: |
| 前 1 块 | 18/18 | 16/18 |
| 前 3 块 | 18/18 | 18/18 |
| 前 5 块 | 18/18 | 18/18 |
| 前 10 块 | 18/18 | 18/18 |

前三块再按原始相似度≥0.16筛选：证据完整 11/18；无关问题拒绝 6/6。

阈值0的列表仅供诊断排序，零分片段不返回；它不是经过校准的上线配置。关键词索引使用标题、实体和正文，去掉链接地址以避免路径文字干扰。

## 逐题结果

| 问题 | 前5块证据完整 | 前3名 | 未命中的证据组 |
| --- | --- | --- | --- |
| N01：IDV(9)的扰动类型是什么？ | 是 | FAULT-IDV09 (0.355)；FAULT-IDV21 (0.327)；FAULTS-001 (0.321) | — |
| N02：十号故障改变的是哪一股进料的温度？ | 是 | FAULT-IDV10 (0.294)；FAULT-IDV21 (0.296)；FAULTS-001 (0.294) | — |
| N03：第十五个故障的预设是什么？ | 是 | FAULT-IDV15 (0.290)；FAULT-IDV21 (0.307)；FAULTS-001 (0.294) | — |
| N04：xmeas(22)对应的设备和单位是什么？ | 是 | VAR-X22 (0.361)；VAR-X02 (0.255)；VAR-X21 (0.209) | — |
| N05：XMV(10)在52列里对应哪个X编号？ | 是 | VAR-X51 (0.394)；SCOPE-001 (0.223)；VARS-001 (0.060) | — |
| N06：流股十一是产品流吗？ | 是 | STREAM-11 (0.089)；VAR-X17 (0.265)；VAR-X41 (0.131) | — |
| N07：流12和流13分别服务哪个设备？ | 是 | UTILITY-12 (0.135)；UTILITY-13 (0.121)；VAR-X12 (0.149) | — |
| N08：TEP为什么要有循环压缩机？ | 是 | EQUIP-COMPRESSOR (0.314)；STREAM-08 (0.149)；PROC-001 (0.133) | — |
| N09：TEP中的B是不是反应原料？ | 是 | CHEM-001 (0.040)；UTILITY-12 (0.122)；UTILITY-13 (0.068) | — |
| N10：TEP的产品G和H由什么反应生成？ | 是 | CHEM-001 (0.083)；STREAM-11 (0.099)；PROC-001 (0.088) | — |
| N11：流股八离开分离器之后如何分流？ | 是 | STREAM-08 (0.085)；PROC-001 (0.109)；VAR-X05 (0.102) | — |
| N12：这份TEP数据的组分分析值为何连续几行一样？ | 是 | DATA-002 (0.121)；DATA-TIMING (0.095)；C09 (0.094) | — |
| N13：那么十一呢？ | 是 | FAULT-IDV11 (0.398)；FAULT-IDV10 (0.204)；FAULT-IDV21 (0.478) | — |
| N14：换成四十九 | 是 | VAR-X49 (0.355)；VAR-X48 (0.074)；VARS-001 (0.151) | — |
| N15：该故障的预设扰动是什么？ | 是 | FAULT-IDV12 (0.349)；FAULT-IDV21 (0.412)；FAULTS-001 (0.409) | — |
| N16：这条流的去向呢？ | 是 | STREAM-06 (0.035)；PROC-001 (0.089)；EQUIP-REACTOR (0.054) | — |
| N17：那12呢？ | 是 | SCOPE-001 (0.214)；VARS-001 (0.060)；VAR-X12 (0.342) | — |
| N18：IDV(19)的确切物理起因有记载吗？ | 是 | FAULT-IDV19 (0.419)；FAULT-IDV21 (0.433)；FAULTS-001 (0.422) | — |
| B01：那6呢？ | 无关问题 | 无 | — |
| B02：它的单位呢？ | 无关问题 | 无 | — |
| B03：那99呢？ | 无关问题 | 无 | — |
| B04：今天杭州天气怎么样？ | 无关问题 | 无 | — |
| B05：帮我写一首关于春天的诗 | 无关问题 | 无 | — |
| B06：怎样重置Windows登录密码？ | 无关问题 | EQUIP-CONDENSER (0.066)；C04 (0.042)；FAULT-IDV17 (0.036) | — |

## 每题命中文本与来源

### N01 · IDV(9)的扰动类型是什么？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "IDV(9)的扰动类型是什么？",
  "normalized_query": "IDV(9)的扰动类型是什么?",
  "retrieval_query": "IDV(9)的扰动类型是什么? IDV(9)",
  "entities": [
    {
      "kind": "fault",
      "number": 9,
      "canonical": "IDV(9)",
      "valid": true,
      "primary_unit": "FAULT-IDV09",
      "raw": "IDV(9)",
      "span": [
        0,
        6
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "FAULT-IDV09"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "IDV(9)的扰动类型是什么？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"FAULT-IDV09": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV09 · 分数 0.3554

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:378)

7.9 IDV(9)：D 进料温度随机变化｜FAULT-IDV09

- **扰动类型：**随机变化。
- **预设注入：**流 2 的 D 进料温度随机变化。
- **可观测性：**无直接记录：流 2 温度不在 52 列中。
- **关联字段：**X2 为流 2 流量；X42 为 D 进料操纵量。
- **解释边界：**与 IDV(3) 的作用量相同，时间变化类型不同。
- **来源：**[S03，Process Disturbances 的 IDV(9)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · FAULT-IDV21 · 分数 0.3268

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486)

7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

- **扰动类型：**固定阀位（参考数据扩展）。
- **预设注入：**后续参考数据将本项定义为流 4 阀门位置保持常数。
- **可观测性：**X45 = XMV(4) 是对应进料操纵通道；X4 记录流 4 流量。
- **关联字段：**需结合具体生成器区分阀位固定值、控制命令和实际执行值。
- **解释边界：**不属于原始 1993 年 IDV(1)–(20) 表；固定阀位与 IDV(14)/(15) 的粘滞不能直接混用。
- **来源：**[S04，Fault Scenarios 的 d21](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULTS-001 · 分数 0.3210

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300)

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · SCOPE-001 · 分数 0.2368

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · VAR-X09 · 分数 0.2343

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:202)

X9 / XMEAS(9)：反应器温度

- 条目 ID：VAR-X09
- 项目字段：X9
- 原始标识：XMEAS(9)
- 含义与测点：反应器温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N02 · 十号故障改变的是哪一股进料的温度？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "十号故障改变的是哪一股进料的温度？",
  "normalized_query": "十号故障改变的是哪一股进料的温度?",
  "retrieval_query": "十号故障改变的是哪一股进料的温度? IDV(10)",
  "entities": [
    {
      "kind": "fault",
      "number": 10,
      "canonical": "IDV(10)",
      "valid": true,
      "primary_unit": "FAULT-IDV10",
      "raw": "十号故障",
      "span": [
        0,
        4
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "FAULT-IDV10"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "十号故障改变的是哪一股进料的温度？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"FAULT-IDV10": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV10 · 分数 0.2941

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:387)

7.10 IDV(10)：C 进料温度随机变化｜FAULT-IDV10

- **扰动类型：**随机变化。
- **预设注入：**流 4 的进料温度随机变化，原始名称为 C Feed Temperature。
- **可观测性：**无直接记录：流 4 进料温度不在 52 列中。
- **关联字段：**X4 为流 4 流量；X45 为流 4 进料操纵量。
- **解释边界：**按原始代码采用流 4；论文表中的流 2 已登记为来源冲突。
- **来源：**[S03，Process Disturbances 的 IDV(10)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C03
- 问题：论文表 2-2 的 IDV(10) 写流 2
- 本手册采用的表述：流 4 进料温度随机变化
- 核对依据与状态：S03 的 IDV(10)，S04 的 d10；已记录纠正

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 2 名 · FAULT-IDV21 · 分数 0.2960

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486)

7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

- **扰动类型：**固定阀位（参考数据扩展）。
- **预设注入：**后续参考数据将本项定义为流 4 阀门位置保持常数。
- **可观测性：**X45 = XMV(4) 是对应进料操纵通道；X4 记录流 4 流量。
- **关联字段：**需结合具体生成器区分阀位固定值、控制命令和实际执行值。
- **解释边界：**不属于原始 1993 年 IDV(1)–(20) 表；固定阀位与 IDV(14)/(15) 的粘滞不能直接混用。
- **来源：**[S04，Fault Scenarios 的 d21](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULTS-001 · 分数 0.2944

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300)

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · C03 · 分数 0.2338

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:501)

来源差异 C03：流 4 进料温度随机变化

- ID：C03
- 问题：论文表 2-2 的 IDV(10) 写流 2
- 本手册采用的表述：流 4 进料温度随机变化
- 核对依据与状态：S03 的 IDV(10)，S04 的 d10；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · SCOPE-001 · 分数 0.2289

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

### N03 · 第十五个故障的预设是什么？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "第十五个故障的预设是什么？",
  "normalized_query": "第十五个故障的预设是什么?",
  "retrieval_query": "第十五个故障的预设是什么? IDV(15)",
  "entities": [
    {
      "kind": "fault",
      "number": 15,
      "canonical": "IDV(15)",
      "valid": true,
      "primary_unit": "FAULT-IDV15",
      "raw": "第十五个故障",
      "span": [
        0,
        6
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "FAULT-IDV15"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "第十五个故障的预设是什么？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"FAULT-IDV15": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV15 · 分数 0.2900

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:432)

7.15 IDV(15)：冷凝器冷却水阀门粘滞｜FAULT-IDV15

- **扰动类型：**阀门粘滞。
- **预设注入：**冷凝器冷却水阀门出现粘滞。
- **可观测性：**X52 = XMV(11) 是对应操纵通道；并非另有一个实际阀位测量。
- **关联字段：**X22 为冷却水出口温度，X11 为分离器温度。
- **解释边界：**不能把本故障改写为压缩机冷却水阀故障。
- **来源：**[S03，Process Disturbances 的 IDV(15)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · FAULT-IDV21 · 分数 0.3073

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486)

7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

- **扰动类型：**固定阀位（参考数据扩展）。
- **预设注入：**后续参考数据将本项定义为流 4 阀门位置保持常数。
- **可观测性：**X45 = XMV(4) 是对应进料操纵通道；X4 记录流 4 流量。
- **关联字段：**需结合具体生成器区分阀位固定值、控制命令和实际执行值。
- **解释边界：**不属于原始 1993 年 IDV(1)–(20) 表；固定阀位与 IDV(14)/(15) 的粘滞不能直接混用。
- **来源：**[S04，Fault Scenarios 的 d21](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULTS-001 · 分数 0.2936

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300)

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · VAR-X15 · 分数 0.2278

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:208)

X15 / XMEAS(15)：汽提塔液位

- 条目 ID：VAR-X15
- 项目字段：X15
- 原始标识：XMEAS(15)
- 含义与测点：汽提塔液位
- 单位：%

【继承的限定与来源】
【单位与来源】
液位 % 是模型的液位标度，不保证等于容器总体积百分比。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · SCOPE-001 · 分数 0.2271

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

### N04 · xmeas(22)对应的设备和单位是什么？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "xmeas(22)对应的设备和单位是什么？",
  "normalized_query": "xmeas(22)对应的设备和单位是什么?",
  "retrieval_query": "xmeas(22)对应的设备和单位是什么? XMEAS(22)",
  "entities": [
    {
      "kind": "xmeas",
      "number": 22,
      "canonical": "XMEAS(22)",
      "valid": true,
      "primary_unit": "VAR-X22",
      "raw": "xmeas(22)",
      "span": [
        0,
        9
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "VAR-X22"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "xmeas(22)对应的设备和单位是什么？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"VAR-X22": 1}`。null 表示无正分命中。

#### 第 1 名 · VAR-X22 · 分数 0.3608

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:215)

X22 / XMEAS(22)：分离器冷却水出口温度；对应冷凝冷却系统

- 条目 ID：VAR-X22
- 项目字段：X22
- 原始标识：XMEAS(22)
- 含义与测点：分离器冷却水出口温度；对应冷凝冷却系统
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【来源差异处理】
- ID：C01
- 问题：论文表 2-1 将 X22 写成汽提塔冷却水出口温度
- 本手册采用的表述：分离器冷却水出口温度，对应冷凝冷却系统
- 核对依据与状态：S03 的 XMEAS(22)，S02 表 4；已记录纠正

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · VAR-X02 · 分数 0.2549

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:195)

X2 / XMEAS(2)：D 进料流量；流 2

- 条目 ID：VAR-X02
- 项目字段：X2
- 原始标识：XMEAS(2)
- 含义与测点：D 进料流量；流 2
- 单位：kg/h

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · VAR-X21 · 分数 0.2095

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:214)

X21 / XMEAS(21)：反应器冷却水出口温度

- 条目 ID：VAR-X21
- 项目字段：X21
- 原始标识：XMEAS(21)
- 含义与测点：反应器冷却水出口温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · C01 · 分数 0.2068

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:499)

来源差异 C01：分离器冷却水出口温度，对应冷凝冷却系统

- ID：C01
- 问题：论文表 2-1 将 X22 写成汽提塔冷却水出口温度
- 本手册采用的表述：分离器冷却水出口温度，对应冷凝冷却系统
- 核对依据与状态：S03 的 XMEAS(22)，S02 表 4；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · VAR-X20 · 分数 0.1916

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:213)

X20 / XMEAS(20)：压缩机功率

- 条目 ID：VAR-X20
- 项目字段：X20
- 原始标识：XMEAS(20)
- 含义与测点：压缩机功率
- 单位：kW

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N05 · XMV(10)在52列里对应哪个X编号？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "XMV(10)在52列里对应哪个X编号？",
  "normalized_query": "XMV(10)在52列里对应哪个X编号?",
  "retrieval_query": "XMV(10)在52列里对应哪个X编号? XMV(10)",
  "entities": [
    {
      "kind": "xmv",
      "number": 10,
      "canonical": "XMV(10)",
      "valid": true,
      "primary_unit": "VAR-X51",
      "raw": "XMV(10)",
      "span": [
        0,
        7
      ]
    }
  ],
  "quantities": [
    {
      "text": "52列",
      "number": 52,
      "unit": "列",
      "span": [
        8,
        11
      ]
    }
  ],
  "intent": "data_schema",
  "intent_kinds": [
    "scope",
    "variable_conventions"
  ],
  "primary_units": [
    "VAR-X51"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "询问数据列/操纵变量覆盖范围",
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "XMV(10)在52列里对应哪个X编号？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"VAR-X51": 1}`。null 表示无正分命中。

#### 第 1 名 · VAR-X51 · 分数 0.3942

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:256)

X51 / XMV(10)：反应器冷却水操纵量

- 条目 ID：VAR-X51
- 项目字段：X51
- 原始标识：XMV(10)
- 含义与作用对象：反应器冷却水操纵量
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · SCOPE-001 · 分数 0.2230

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · VARS-001 · 分数 0.0598

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:184)

5. 完整变量字典｜VARS-001

本节复用论文表 2-1 的 X1–X52 顺序，补齐原始标识、单位和测点范围；有冲突的中文名称见第 8 节。每行的 `VAR-Xnn` 是知识条目 ID，便于稳定引用。

**单位约定：**kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。kPa(g) 为表压。mol% 为摩尔百分数，不能当作质量百分数。液位 % 是模型的液位标度，不保证等于容器总体积百分比。操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【继承的限定与来源】
【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · VAR-X10 · 分数 0.3120

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:203)

X10 / XMEAS(10)：排放流量；流 9

- 条目 ID：VAR-X10
- 项目字段：X10
- 原始标识：XMEAS(10)
- 含义与测点：排放流量；流 9
- 单位：kscmh

【继承的限定与来源】
【单位与来源】
kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · FAULT-IDV10 · 分数 0.2873

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:387)

7.10 IDV(10)：C 进料温度随机变化｜FAULT-IDV10

- **扰动类型：**随机变化。
- **预设注入：**流 4 的进料温度随机变化，原始名称为 C Feed Temperature。
- **可观测性：**无直接记录：流 4 进料温度不在 52 列中。
- **关联字段：**X4 为流 4 流量；X45 为流 4 进料操纵量。
- **解释边界：**按原始代码采用流 4；论文表中的流 2 已登记为来源冲突。
- **来源：**[S03，Process Disturbances 的 IDV(10)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C03
- 问题：论文表 2-2 的 IDV(10) 写流 2
- 本手册采用的表述：流 4 进料温度随机变化
- 核对依据与状态：S03 的 IDV(10)，S04 的 d10；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

### N06 · 流股十一是产品流吗？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "流股十一是产品流吗？",
  "normalized_query": "流股十一是产品流吗?",
  "retrieval_query": "流股十一是产品流吗? 流 11",
  "entities": [
    {
      "kind": "stream",
      "number": 11,
      "canonical": "流 11",
      "valid": true,
      "primary_unit": "STREAM-11",
      "raw": "流股十一",
      "span": [
        0,
        4
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "STREAM-11"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "流股十一是产品流吗？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"STREAM-11": 1}`。null 表示无正分命中。

#### 第 1 名 · STREAM-11 · 分数 0.0886

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:118)

TEP 流股 11：汽提塔底 → 基准边界外

- 稳定 ID：STREAM-11
- 图中编号：11
- 上游 → 下游：汽提塔底 → 基准边界外
- 物料及作用：含 G/H 的产品混合物
- 本项目直接相关测量：X17 体积流量；X37–X41 的 D–H 组分

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 2 名 · VAR-X17 · 分数 0.2651

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:210)

X17 / XMEAS(17)：汽提塔底产品流量；流 11

- 条目 ID：VAR-X17
- 项目字段：X17
- 原始标识：XMEAS(17)
- 含义与测点：汽提塔底产品流量；流 11
- 单位：m³/h

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · VAR-X41 · 分数 0.1309

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:241)

X41 / XMEAS(41)：塔底产品中 H；流 11

- 条目 ID：VAR-X41
- 项目字段：X41
- 原始标识：XMEAS(41)
- 含义与测点：塔底产品中 H；流 11
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · VAR-X37 · 分数 0.1303

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:237)

X37 / XMEAS(37)：塔底产品中 D；流 11

- 条目 ID：VAR-X37
- 项目字段：X37
- 原始标识：XMEAS(37)
- 含义与测点：塔底产品中 D；流 11
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · VAR-X39 · 分数 0.1298

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:239)

X39 / XMEAS(39)：塔底产品中 F；流 11

- 条目 ID：VAR-X39
- 项目字段：X39
- 原始标识：XMEAS(39)
- 含义与测点：塔底产品中 F；流 11
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N07 · 流12和流13分别服务哪个设备？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "流12和流13分别服务哪个设备？",
  "normalized_query": "流12和流13分别服务哪个设备?",
  "retrieval_query": "流12和流13分别服务哪个设备? 流 12 流 13",
  "entities": [
    {
      "kind": "stream",
      "number": 12,
      "canonical": "流 12",
      "valid": true,
      "primary_unit": "UTILITY-12",
      "raw": "流12",
      "span": [
        0,
        3
      ]
    },
    {
      "kind": "stream",
      "number": 13,
      "canonical": "流 13",
      "valid": true,
      "primary_unit": "UTILITY-13",
      "raw": "流13",
      "span": [
        4,
        7
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "UTILITY-12",
    "UTILITY-13"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "流12和流13分别服务哪个设备？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"UTILITY-12": 1, "UTILITY-13": 2}`。null 表示无正分命中。

#### 第 1 名 · UTILITY-12 · 分数 0.1353

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:119)

TEP 流股 12：冷却水公用工程 ↔ 反应器冷却束

- 稳定 ID：UTILITY-12
- 图中编号：12
- 上游 → 下游：冷却水公用工程 ↔ 反应器冷却束
- 物料及作用：换热介质，不是反应原料
- 本项目直接相关测量：X21 出口温度；X51 操纵通道

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 2 名 · UTILITY-13 · 分数 0.1205

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:120)

TEP 流股 13：冷却水公用工程 ↔ 冷凝器

- 稳定 ID：UTILITY-13
- 图中编号：13
- 上游 → 下游：冷却水公用工程 ↔ 冷凝器
- 物料及作用：换热介质，不是反应器出料
- 本项目直接相关测量：X22 出口温度；X52 操纵通道

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 3 名 · VAR-X12 · 分数 0.1495

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:205)

X12 / XMEAS(12)：汽液分离器液位

- 条目 ID：VAR-X12
- 项目字段：X12
- 原始标识：XMEAS(12)
- 含义与测点：汽液分离器液位
- 单位：%

【继承的限定与来源】
【单位与来源】
液位 % 是模型的液位标度，不保证等于容器总体积百分比。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · FAULT-IDV12 · 分数 0.1061

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:405)

7.12 IDV(12)：冷凝器冷却水入口温度随机变化｜FAULT-IDV12

- **扰动类型：**随机变化。
- **预设注入：**冷凝器冷却水入口温度随机变化。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X22 为出口温度，X52 为操纵量；X11 为分离器温度。
- **解释边界：**不能将入口温度扰动等同于 X52 阀门故障。
- **来源：**[S03，Process Disturbances 的 IDV(12)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · STREAM-02 · 分数 0.1021

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:109)

TEP 流股 2：D 原料边界 → 进料混合处

- 稳定 ID：STREAM-02
- 图中编号：2
- 上游 → 下游：D 原料边界 → 进料混合处
- 物料及作用：D 新鲜进料
- 本项目直接相关测量：X2 流量

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

### N08 · TEP为什么要有循环压缩机？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "TEP为什么要有循环压缩机？",
  "normalized_query": "TEP为什么要有循环压缩机?",
  "retrieval_query": "TEP为什么要有循环压缩机?",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "TEP为什么要有循环压缩机？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"EQUIP-COMPRESSOR": 1}`。null 表示无正分命中。

#### 第 1 名 · EQUIP-COMPRESSOR · 分数 0.3142

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:162)

4.4 循环压缩机｜EQUIP-COMPRESSOR

**功能与边界。**循环压缩机处理分离器未凝气相循环支路，使循环物流经流 8 返回进料侧。经典图中还画有压缩机旁路/回流阀，因此“压缩机循环阀”不能简单画成串在流 8 上的普通进料阀。

**记录字段。**X5 是流 8 循环流量，X20 是压缩机功率，X46 = XMV(5) 是压缩机循环阀操纵量。功率单位 kW，既不是压力，也不是累计耗电量 kWh。

**知识边界。**这些变量说明部件、测点和执行通道关系，不能据此预先规定 X46 增加时所有工况下 X5 都按同一方向变化。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，XMEAS(5)/(20)、XMV(5)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · STREAM-08 · 分数 0.1494

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:115)

TEP 流股 8：分离器气相经压缩机循环支路 → 进料混合处

- 稳定 ID：STREAM-08
- 图中编号：8
- 上游 → 下游：分离器气相经压缩机循环支路 → 进料混合处
- 物料及作用：循环气体
- 本项目直接相关测量：X5 流量

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 3 名 · PROC-001 · 分数 0.1332

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:67)

3.1 从原料到产品，以及两条返回路径

TEP 的主设备为反应器、冷凝器、汽液分离器、循环压缩机和汽提塔。以下按物流讲解，**不是故障因果图**。

1. **原料补充与进料混合。**流 1 补充 A，流 2 补充 D，流 3 补充 E。这些原料与汽提塔顶返回的流 5、压缩机侧返回的循环流 8 汇合，形成流 6，进入反应器。流 6 是混合后的总进料，不能视为某一路新鲜原料。
2. **反应与移热。**反应器接收流 6，进行产品和副产物生成反应。内部冷却水回路承担移热。反应器物料通过流 7 离开并进入冷凝段；流 7 包含产品和未反应组分。
3. **冷却、冷凝与分相。**冷凝器先对反应器出料换热，使可凝组分形成液相。随后汽液分离器把气液两相分开。冷凝是热交换/相变环节，分离器是相分离及液体滞留环节，二者不可合并成一个变量名称。
4. **气相循环与排放。**分离器气相有两条去向：一部分经流 9 排出系统，另一部分经循环压缩机返回进料端，构成流 8。排放为循环系统提供物料出口；循环回收未反应组分。排放气并非只有 B 或 F，流 9 的分析仪记录 A–H 八个组分。
5. **液相汽提。**分离器液体由流 10 进入汽提塔。流 4 是含 A/C 的新鲜混合进料，它先进入汽提塔参与汽提，而不是从图上直接连到反应器。汽提塔还有蒸汽供热环节，塔顶物料通过流 5 返回反应器进料混合处。
6. **产品输出。**汽提塔底通过流 11 输出含 G/H 的产品混合物。它不是已经分成两路的纯 G、纯 H。后续产品精制不属于本基准的五个主设备。

这形成两条返回路径：**分离器气相 → 压缩机 → 进料混合处**，以及**分离器液相 → 汽提塔 → 塔顶返回进料混合处**。因此某条管线的结构上游，并不自动等同于统计诊断中的根源。

依据：[S01，图 2.3、§2.4](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)，对照 [S02，图 1、p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。设备和流股的文本连接为本手册依据上述图示整理。

【继承的限定与来源】
【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 4 名 · VAR-X46 · 分数 0.1112

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:251)

X46 / XMV(5)：压缩机循环／旁路阀操纵量

- 条目 ID：VAR-X46
- 项目字段：X46
- 原始标识：XMV(5)
- 含义与作用对象：压缩机循环／旁路阀操纵量
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · VAR-X20 · 分数 0.1095

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:213)

X20 / XMEAS(20)：压缩机功率

- 条目 ID：VAR-X20
- 项目字段：X20
- 原始标识：XMEAS(20)
- 含义与测点：压缩机功率
- 单位：kW

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N09 · TEP中的B是不是反应原料？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "TEP中的B是不是反应原料？",
  "normalized_query": "TEP中的B是不是反应原料?",
  "retrieval_query": "TEP中的B是不是反应原料?",
  "entities": [],
  "quantities": [],
  "intent": "chemistry",
  "intent_kinds": [
    "chemistry"
  ],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "询问组分角色或反应关系，优先化学反应说明"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "TEP中的B是不是反应原料？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"CHEM-001": 1}`。null 表示无正分命中。

#### 第 1 名 · CHEM-001 · 分数 0.0400

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:33)

2. 组分与反应｜CHEM-001

### 2.1 八个组分的角色

| 组分 | 在基准模型中的角色 | 阅读边界 |
| --- | --- | --- |
| A | 反应物 | 存在于 A 进料和 A/C 混合进料中 |
| B | 惰性组分 | 不出现在下列四条反应的反应物或产物项中；不是催化剂名称 |
| C | 反应物 | 随流 4 的混合进料进入过程 |
| D | 反应物 | 由流 2 补充 |
| E | 反应物 | 由流 3 补充 |
| F | 副产物 | 由两条副反应产生 |
| G | 目标产品之一 | 随塔底产品流输出 |
| H | 目标产品之一 | 随塔底产品流输出 |

A–H 是基准模型的组分标识。本手册不把它们擅自对应为具体商业化学品。

### 2.2 四条反应

| 反应 ID | 反应式 | 类型 |
| --- | --- | --- |
| RXN-01 | A + C + D → G | 生成产品 G |
| RXN-02 | A + C + E → H | 生成产品 H |
| RXN-03 | A + E → F | 生成副产物 F |
| RXN-04 | 3D → 2F | 生成副产物 F |

原始描述将这些反应设为不可逆放热反应；温度进入反应速率关系。反应器中的非挥发性催化剂溶于液相并留在反应器内。**催化剂与惰性组分 B 应分别理解**；不要因二手图式箭头上的标注把 B 写成催化剂。

反应式可以说明原料消耗与产物生成的关系，不能单独确定闭环运行时某个传感器先升后降的时间序列。

依据：[S01，§2.4 反应式与组分描述](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)；催化剂与反应属性核对：[S02，pp.245、247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【继承的限定与来源】
【来源差异处理】
- ID：C06
- 问题：论文反应式箭头上的 B 标注可能被误读为催化剂
- 本手册采用的表述：B 是惰性组分；催化剂另行描述
- 核对依据与状态：S02 pp.245、247；不继承有歧义的箭头标注

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)

#### 第 2 名 · UTILITY-12 · 分数 0.1220

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:119)

TEP 流股 12：冷却水公用工程 ↔ 反应器冷却束

- 稳定 ID：UTILITY-12
- 图中编号：12
- 上游 → 下游：冷却水公用工程 ↔ 反应器冷却束
- 物料及作用：换热介质，不是反应原料
- 本项目直接相关测量：X21 出口温度；X51 操纵通道

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 3 名 · UTILITY-13 · 分数 0.0685

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:120)

TEP 流股 13：冷却水公用工程 ↔ 冷凝器

- 稳定 ID：UTILITY-13
- 图中编号：13
- 上游 → 下游：冷却水公用工程 ↔ 冷凝器
- 物料及作用：换热介质，不是反应器出料
- 本项目直接相关测量：X22 出口温度；X52 操纵通道

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 4 名 · STREAM-02 · 分数 0.0584

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:109)

TEP 流股 2：D 原料边界 → 进料混合处

- 稳定 ID：STREAM-02
- 图中编号：2
- 上游 → 下游：D 原料边界 → 进料混合处
- 物料及作用：D 新鲜进料
- 本项目直接相关测量：X2 流量

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 5 名 · STREAM-01 · 分数 0.0583

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:108)

TEP 流股 1：A 原料边界 → 进料混合处

- 稳定 ID：STREAM-01
- 图中编号：1
- 上游 → 下游：A 原料边界 → 进料混合处
- 物料及作用：A 新鲜进料
- 本项目直接相关测量：X1 流量

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

### N10 · TEP的产品G和H由什么反应生成？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "TEP的产品G和H由什么反应生成？",
  "normalized_query": "TEP的产品G和H由什么反应生成?",
  "retrieval_query": "TEP的产品G和H由什么反应生成?",
  "entities": [],
  "quantities": [],
  "intent": "chemistry",
  "intent_kinds": [
    "chemistry"
  ],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "询问组分角色或反应关系，优先化学反应说明"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "TEP的产品G和H由什么反应生成？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"CHEM-001": 1}`。null 表示无正分命中。

#### 第 1 名 · CHEM-001 · 分数 0.0833

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:33)

2. 组分与反应｜CHEM-001

### 2.1 八个组分的角色

| 组分 | 在基准模型中的角色 | 阅读边界 |
| --- | --- | --- |
| A | 反应物 | 存在于 A 进料和 A/C 混合进料中 |
| B | 惰性组分 | 不出现在下列四条反应的反应物或产物项中；不是催化剂名称 |
| C | 反应物 | 随流 4 的混合进料进入过程 |
| D | 反应物 | 由流 2 补充 |
| E | 反应物 | 由流 3 补充 |
| F | 副产物 | 由两条副反应产生 |
| G | 目标产品之一 | 随塔底产品流输出 |
| H | 目标产品之一 | 随塔底产品流输出 |

A–H 是基准模型的组分标识。本手册不把它们擅自对应为具体商业化学品。

### 2.2 四条反应

| 反应 ID | 反应式 | 类型 |
| --- | --- | --- |
| RXN-01 | A + C + D → G | 生成产品 G |
| RXN-02 | A + C + E → H | 生成产品 H |
| RXN-03 | A + E → F | 生成副产物 F |
| RXN-04 | 3D → 2F | 生成副产物 F |

原始描述将这些反应设为不可逆放热反应；温度进入反应速率关系。反应器中的非挥发性催化剂溶于液相并留在反应器内。**催化剂与惰性组分 B 应分别理解**；不要因二手图式箭头上的标注把 B 写成催化剂。

反应式可以说明原料消耗与产物生成的关系，不能单独确定闭环运行时某个传感器先升后降的时间序列。

依据：[S01，§2.4 反应式与组分描述](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)；催化剂与反应属性核对：[S02，pp.245、247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【继承的限定与来源】
【来源差异处理】
- ID：C06
- 问题：论文反应式箭头上的 B 标注可能被误读为催化剂
- 本手册采用的表述：B 是惰性组分；催化剂另行描述
- 核对依据与状态：S02 pp.245、247；不继承有歧义的箭头标注

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)

#### 第 2 名 · STREAM-11 · 分数 0.0987

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:118)

TEP 流股 11：汽提塔底 → 基准边界外

- 稳定 ID：STREAM-11
- 图中编号：11
- 上游 → 下游：汽提塔底 → 基准边界外
- 物料及作用：含 G/H 的产品混合物
- 本项目直接相关测量：X17 体积流量；X37–X41 的 D–H 组分

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 3 名 · PROC-001 · 分数 0.0883

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:67)

3.1 从原料到产品，以及两条返回路径

TEP 的主设备为反应器、冷凝器、汽液分离器、循环压缩机和汽提塔。以下按物流讲解，**不是故障因果图**。

1. **原料补充与进料混合。**流 1 补充 A，流 2 补充 D，流 3 补充 E。这些原料与汽提塔顶返回的流 5、压缩机侧返回的循环流 8 汇合，形成流 6，进入反应器。流 6 是混合后的总进料，不能视为某一路新鲜原料。
2. **反应与移热。**反应器接收流 6，进行产品和副产物生成反应。内部冷却水回路承担移热。反应器物料通过流 7 离开并进入冷凝段；流 7 包含产品和未反应组分。
3. **冷却、冷凝与分相。**冷凝器先对反应器出料换热，使可凝组分形成液相。随后汽液分离器把气液两相分开。冷凝是热交换/相变环节，分离器是相分离及液体滞留环节，二者不可合并成一个变量名称。
4. **气相循环与排放。**分离器气相有两条去向：一部分经流 9 排出系统，另一部分经循环压缩机返回进料端，构成流 8。排放为循环系统提供物料出口；循环回收未反应组分。排放气并非只有 B 或 F，流 9 的分析仪记录 A–H 八个组分。
5. **液相汽提。**分离器液体由流 10 进入汽提塔。流 4 是含 A/C 的新鲜混合进料，它先进入汽提塔参与汽提，而不是从图上直接连到反应器。汽提塔还有蒸汽供热环节，塔顶物料通过流 5 返回反应器进料混合处。
6. **产品输出。**汽提塔底通过流 11 输出含 G/H 的产品混合物。它不是已经分成两路的纯 G、纯 H。后续产品精制不属于本基准的五个主设备。

这形成两条返回路径：**分离器气相 → 压缩机 → 进料混合处**，以及**分离器液相 → 汽提塔 → 塔顶返回进料混合处**。因此某条管线的结构上游，并不自动等同于统计诊断中的根源。

依据：[S01，图 2.3、§2.4](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)，对照 [S02，图 1、p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。设备和流股的文本连接为本手册依据上述图示整理。

【继承的限定与来源】
【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 4 名 · STREAM-06 · 分数 0.0636

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:113)

TEP 流股 6：进料混合处 → 反应器

- 稳定 ID：STREAM-06
- 图中编号：6
- 上游 → 下游：进料混合处 → 反应器
- 物料及作用：新鲜原料和返回物流形成的总进料
- 本项目直接相关测量：X6 流量；X23–X28 的 A–F 组分

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 5 名 · UTILITY-12 · 分数 0.0621

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:119)

TEP 流股 12：冷却水公用工程 ↔ 反应器冷却束

- 稳定 ID：UTILITY-12
- 图中编号：12
- 上游 → 下游：冷却水公用工程 ↔ 反应器冷却束
- 物料及作用：换热介质，不是反应原料
- 本项目直接相关测量：X21 出口温度；X51 操纵通道

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

### N11 · 流股八离开分离器之后如何分流？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "流股八离开分离器之后如何分流？",
  "normalized_query": "流股八离开分离器之后如何分流?",
  "retrieval_query": "流股八离开分离器之后如何分流? 流 8",
  "entities": [
    {
      "kind": "stream",
      "number": 8,
      "canonical": "流 8",
      "valid": true,
      "primary_unit": "STREAM-08",
      "raw": "流股八",
      "span": [
        0,
        3
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "STREAM-08"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "流股八离开分离器之后如何分流？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"STREAM-08": 1}`。null 表示无正分命中。

#### 第 1 名 · STREAM-08 · 分数 0.0849

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:115)

TEP 流股 8：分离器气相经压缩机循环支路 → 进料混合处

- 稳定 ID：STREAM-08
- 图中编号：8
- 上游 → 下游：分离器气相经压缩机循环支路 → 进料混合处
- 物料及作用：循环气体
- 本项目直接相关测量：X5 流量

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 2 名 · PROC-001 · 分数 0.1091

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:67)

3.1 从原料到产品，以及两条返回路径

TEP 的主设备为反应器、冷凝器、汽液分离器、循环压缩机和汽提塔。以下按物流讲解，**不是故障因果图**。

1. **原料补充与进料混合。**流 1 补充 A，流 2 补充 D，流 3 补充 E。这些原料与汽提塔顶返回的流 5、压缩机侧返回的循环流 8 汇合，形成流 6，进入反应器。流 6 是混合后的总进料，不能视为某一路新鲜原料。
2. **反应与移热。**反应器接收流 6，进行产品和副产物生成反应。内部冷却水回路承担移热。反应器物料通过流 7 离开并进入冷凝段；流 7 包含产品和未反应组分。
3. **冷却、冷凝与分相。**冷凝器先对反应器出料换热，使可凝组分形成液相。随后汽液分离器把气液两相分开。冷凝是热交换/相变环节，分离器是相分离及液体滞留环节，二者不可合并成一个变量名称。
4. **气相循环与排放。**分离器气相有两条去向：一部分经流 9 排出系统，另一部分经循环压缩机返回进料端，构成流 8。排放为循环系统提供物料出口；循环回收未反应组分。排放气并非只有 B 或 F，流 9 的分析仪记录 A–H 八个组分。
5. **液相汽提。**分离器液体由流 10 进入汽提塔。流 4 是含 A/C 的新鲜混合进料，它先进入汽提塔参与汽提，而不是从图上直接连到反应器。汽提塔还有蒸汽供热环节，塔顶物料通过流 5 返回反应器进料混合处。
6. **产品输出。**汽提塔底通过流 11 输出含 G/H 的产品混合物。它不是已经分成两路的纯 G、纯 H。后续产品精制不属于本基准的五个主设备。

这形成两条返回路径：**分离器气相 → 压缩机 → 进料混合处**，以及**分离器液相 → 汽提塔 → 塔顶返回进料混合处**。因此某条管线的结构上游，并不自动等同于统计诊断中的根源。

依据：[S01，图 2.3、§2.4](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)，对照 [S02，图 1、p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。设备和流股的文本连接为本手册依据上述图示整理。

【继承的限定与来源】
【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 3 名 · VAR-X05 · 分数 0.1016

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:198)

X5 / XMEAS(5)：循环气流量；流 8

- 条目 ID：VAR-X05
- 项目字段：X5
- 原始标识：XMEAS(5)
- 含义与测点：循环气流量；流 8
- 单位：kscmh

【继承的限定与来源】
【单位与来源】
kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · STREAM-07 · 分数 0.0735

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:114)

TEP 流股 7：反应器 → 冷凝器 → 分离器

- 稳定 ID：STREAM-07
- 图中编号：7
- 上游 → 下游：反应器 → 冷凝器 → 分离器
- 物料及作用：反应器出料在冷凝后送入分离器
- 本项目直接相关测量：没有流 7 独立流量/组分列

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 5 名 · VAR-X11 · 分数 0.0719

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:204)

X11 / XMEAS(11)：汽液分离器温度

- 条目 ID：VAR-X11
- 项目字段：X11
- 原始标识：XMEAS(11)
- 含义与测点：汽液分离器温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N12 · 这份TEP数据的组分分析值为何连续几行一样？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "这份TEP数据的组分分析值为何连续几行一样？",
  "normalized_query": "这份TEP数据的组分分析值为何连续几行一样?",
  "retrieval_query": "这份TEP数据的组分分析值为何连续几行一样?",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": true,
  "issues": [
    "存在没有类型标识的数字；本阶段不根据历史猜测编号类型"
  ],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "这份TEP数据的组分分析值为何连续几行一样？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"DATA-TIMING": 2, "DATA-002": 1}`。null 表示无正分命中。

#### 第 1 名 · DATA-002 · 分数 0.1207

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:289)

6.3 数据清洗时不要误删的现象｜DATA-002

以下是依据测量定义制定的检查规则，不是所有 TEP 文件都已出现的异常：

- 组分分析值重复：先检查分析仪保持和刷新机制，再决定是否为冻结测点；不能默认删除重复行。
- 故障附近的突变：与故障设定、时间窗对照，不能把需要诊断的变化先当离群点抹除。
- 不同量纲：流量、温度、压力、百分数不能直接比较绝对幅度；归一化参数应记录其拟合数据范围。
- 组分和不等于 100%：流 6 仅列 A–F，流 11 仅列 D–H，二者不是完整八组分列表；不能强行把每组归一到 100%。流 9 虽列八组分，也需考虑测量噪声与数值精度。
- 缺失、非有限值、列数或列顺序改变：应独立报告，不应通过静默补零让诊断继续。
- 进料或冷却水入口温度未测：不能把“没有这一列”处理为“这一列数值为零”。

【继承的限定与来源】
【补充上下文】
本节复用论文表 2-1 的 X1–X52 顺序，补齐原始标识、单位和测点范围；有冲突的中文名称见第 8 节。每行的 `VAR-Xnn` 是知识条目 ID，便于稳定引用。

**单位约定：**kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。kPa(g) 为表压。mol% 为摩尔百分数，不能当作质量百分数。液位 % 是模型的液位标度，不保证等于容器总体积百分比。操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【补充上下文】
| 数据对象 | 对应字段 | 原始模型的更新周期 | 分析延迟 | 本项目如何理解 |
| --- | --- | --- | --- | --- |
| 连续过程测量 | X1–X22 | 随仿真过程计算 | 本表不额外指定分析延迟 | 数据文件仍按保存间隔记录 |
| 流 6 组分分析 | X23–X28 | 6 分钟 | 6 分钟 | 刚获得的读数对应更早取得的样品 |
| 流 9 组分分析 | X29–X36 | 6 分钟 | 6 分钟 | 不能当成每 3 分钟都有一个新样品 |
| 流 11 组分分析 | X37–X41 | 15 分钟 | 15 分钟 | 可能连续多行维持同一组分读数 |
| 参考测试文件的保存 | 一整行 52 列 | 3 分钟 | 不等于各测点延迟 | 一行同时保存不代表测点同步采样 |

原始说明以 0.1 h / 0.25 h 表达分析仪周期及延迟。**3 分钟是文件记录间隔，不是所有传感器的真实刷新周期。**这个区别对后续时滞选择、格兰杰分析及“谁先变化”的解释有直接影响。

依据：[S03，Sampled Process Measurements](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。最后一句是本项目的方法使用注意事项，不是预设故障传播结论。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 2 名 · DATA-TIMING · 分数 0.0953

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:265)

6.1 文件记录间隔与分析仪延迟

| 数据对象 | 对应字段 | 原始模型的更新周期 | 分析延迟 | 本项目如何理解 |
| --- | --- | --- | --- | --- |
| 连续过程测量 | X1–X22 | 随仿真过程计算 | 本表不额外指定分析延迟 | 数据文件仍按保存间隔记录 |
| 流 6 组分分析 | X23–X28 | 6 分钟 | 6 分钟 | 刚获得的读数对应更早取得的样品 |
| 流 9 组分分析 | X29–X36 | 6 分钟 | 6 分钟 | 不能当成每 3 分钟都有一个新样品 |
| 流 11 组分分析 | X37–X41 | 15 分钟 | 15 分钟 | 可能连续多行维持同一组分读数 |
| 参考测试文件的保存 | 一整行 52 列 | 3 分钟 | 不等于各测点延迟 | 一行同时保存不代表测点同步采样 |

原始说明以 0.1 h / 0.25 h 表达分析仪周期及延迟。**3 分钟是文件记录间隔，不是所有传感器的真实刷新周期。**这个区别对后续时滞选择、格兰杰分析及“谁先变化”的解释有直接影响。

依据：[S03，Sampled Process Measurements](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。最后一句是本项目的方法使用注意事项，不是预设故障传播结论。

【继承的限定与来源】
【来源差异处理】
- ID：C09
- 问题：“所有测点每 3 分钟采样”的表述过度简化
- 本手册采用的表述：文件每 3 分钟保存，组分分析有 6/15 分钟周期与延迟
- 核对依据与状态：S03、S04；已补充时间语义

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · C09 · 分数 0.0937

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:507)

来源差异 C09：文件每 3 分钟保存，组分分析有 6/15 分钟周期与延迟

- ID：C09
- 问题：“所有测点每 3 分钟采样”的表述过度简化
- 本手册采用的表述：文件每 3 分钟保存，组分分析有 6/15 分钟周期与延迟
- 核对依据与状态：S03、S04；已补充时间语义

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · DATA-FILES · 分数 0.0686

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:279)

6.2 当前项目数据范围

当前已使用正常工况 `d00_te.dat` 和故障 7 的 `d07_te.dat`。本地检查结果均为 960 行、52 列，没有缺失值或无穷值；这只适用于当前两个文件，不代表全部 TEP 数据都没有异常值。

论文实验约定为每 3 分钟记录一次、48 小时测试、8 小时后注入故障；当前项目据此前 160 点为正常段，后续段作故障分析。该约定不能自动推广到其他仿真器、训练文件或重新生成的数据，换文件时需重新核对时间轴和注入点。

本地数据的下载地址、文件哈希及首次检查见 [data/README.md](/Users/rowen/Documents/高校/tep-fault-agent/data/README.md)。这里的故障目录覆盖 21 类，**不代表当前诊断功能已对 21 类逐一验证**。

依据：[S01，§2.4 的实验数据说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S04，文件结构说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)、本项目数据检查记录。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · EQUIP-REACTOR · 分数 0.0371

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:130)

4.1 反应器｜EQUIP-REACTOR

**功能与边界。**反应器是发生四条反应的设备，接收混合进料流 6，经流 7 向冷凝器排出物料。进料侧同时受到新鲜原料和循环物料的影响；仅看一条新鲜进料无法完整描述反应器入口组成。

**换热与内部操作。**反应放热，内部冷却束负责移热，搅拌器是原始模型的另一操纵对象。冷却水和反应物料隔着换热面交换热量，不能把冷却水入口当作进入反应器参与反应的进料。

**记录字段。**X6 为流 6 总流量；X7、X8、X9 分别是反应器压力、液位、温度。X21 是反应器冷却水出口温度；X51 是冷却水操纵通道。X23–X28 是入口流 6 的组分分析，并非反应器内部液相组分。搅拌器转速不在本项目 52 列中。

**与故障表的连接。**IDV(4)/(11) 改变冷却水入口温度，IDV(14) 对应冷却水阀粘滞，IDV(13) 改变反应动力学。这些物理位置相近但扰动类型不同；不能合并成“X9 温度故障”。

依据：[S01，§2.4、图 2.3、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量及扰动声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N13 · 那么十一呢？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "那么十一呢？",
  "normalized_query": "那么十一呢?",
  "retrieval_query": "IDV(11)是什么故障? IDV(11)",
  "entities": [
    {
      "kind": "fault",
      "number": 11,
      "canonical": "IDV(11)",
      "valid": true,
      "primary_unit": "FAULT-IDV11",
      "raw": "IDV(11)",
      "span": [
        0,
        7
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "FAULT-IDV11"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": true,
  "followup_version": "1.0.0",
  "previous_question": "IDV(10)是什么故障？",
  "resolved_query": "IDV(11)是什么故障?",
  "resolution_status": "resolved",
  "resolution_reason": "从上一轮继承 fault 类型及问法，仅替换主体编号",
  "clarification": null,
  "context_units": [
    "FAULT-IDV10"
  ]
}
```

上一问：IDV(10)是什么故障？。是否使用历史：True。实际检索问题：IDV(11)是什么故障? IDV(11)。

预期证据排名：`{"FAULT-IDV11": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV11 · 分数 0.3978

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:396)

7.11 IDV(11)：反应器冷却水入口温度随机变化｜FAULT-IDV11

- **扰动类型：**随机变化。
- **预设注入：**反应器冷却水入口温度随机变化。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X21 为出口温度，X51 为操纵量；X9 为反应器温度。
- **解释边界：**与 IDV(4) 不同之处在扰动随时间的形式。
- **来源：**[S03，Process Disturbances 的 IDV(11)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · FAULT-IDV10 · 分数 0.2043

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:387)

7.10 IDV(10)：C 进料温度随机变化｜FAULT-IDV10

- **扰动类型：**随机变化。
- **预设注入：**流 4 的进料温度随机变化，原始名称为 C Feed Temperature。
- **可观测性：**无直接记录：流 4 进料温度不在 52 列中。
- **关联字段：**X4 为流 4 流量；X45 为流 4 进料操纵量。
- **解释边界：**按原始代码采用流 4；论文表中的流 2 已登记为来源冲突。
- **来源：**[S03，Process Disturbances 的 IDV(10)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C03
- 问题：论文表 2-2 的 IDV(10) 写流 2
- 本手册采用的表述：流 4 进料温度随机变化
- 核对依据与状态：S03 的 IDV(10)，S04 的 d10；已记录纠正

排序依据：上一轮主体作为辅助对照；当前主体仍优先；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULT-IDV21 · 分数 0.4780

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486)

7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

- **扰动类型：**固定阀位（参考数据扩展）。
- **预设注入：**后续参考数据将本项定义为流 4 阀门位置保持常数。
- **可观测性：**X45 = XMV(4) 是对应进料操纵通道；X4 记录流 4 流量。
- **关联字段：**需结合具体生成器区分阀位固定值、控制命令和实际执行值。
- **解释边界：**不属于原始 1993 年 IDV(1)–(20) 表；固定阀位与 IDV(14)/(15) 的粘滞不能直接混用。
- **来源：**[S04，Fault Scenarios 的 d21](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · FAULTS-001 · 分数 0.4665

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300)

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · SCOPE-001 · 分数 0.4182

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

### N14 · 换成四十九

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "换成四十九",
  "normalized_query": "换成四十九",
  "retrieval_query": "X49的含义与单位是什么? X49",
  "entities": [
    {
      "kind": "variable",
      "number": 49,
      "canonical": "X49",
      "valid": true,
      "primary_unit": "VAR-X49",
      "raw": "X49",
      "span": [
        0,
        3
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "VAR-X49"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": true,
  "followup_version": "1.0.0",
  "previous_question": "X48的含义与单位是什么？",
  "resolved_query": "X49的含义与单位是什么?",
  "resolution_status": "resolved",
  "resolution_reason": "从上一轮继承 variable 类型及问法，仅替换主体编号",
  "clarification": null,
  "context_units": [
    "VAR-X48"
  ]
}
```

上一问：X48的含义与单位是什么？。是否使用历史：True。实际检索问题：X49的含义与单位是什么? X49。

预期证据排名：`{"VAR-X49": 1}`。null 表示无正分命中。

#### 第 1 名 · VAR-X49 · 分数 0.3545

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:254)

X49 / XMV(8)：汽提塔底产品排出操纵量；流 11

- 条目 ID：VAR-X49
- 项目字段：X49
- 原始标识：XMV(8)
- 含义与作用对象：汽提塔底产品排出操纵量；流 11
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · VAR-X48 · 分数 0.0743

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:253)

X48 / XMV(7)：分离器液相排出操纵量；流 10

- 条目 ID：VAR-X48
- 项目字段：X48
- 原始标识：XMV(7)
- 含义与作用对象：分离器液相排出操纵量；流 10
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

排序依据：上一轮主体作为辅助对照；当前主体仍优先；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · VARS-001 · 分数 0.1510

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:184)

5. 完整变量字典｜VARS-001

本节复用论文表 2-1 的 X1–X52 顺序，补齐原始标识、单位和测点范围；有冲突的中文名称见第 8 节。每行的 `VAR-Xnn` 是知识条目 ID，便于稳定引用。

**单位约定：**kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。kPa(g) 为表压。mol% 为摩尔百分数，不能当作质量百分数。液位 % 是模型的液位标度，不保证等于容器总体积百分比。操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【继承的限定与来源】
【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · EQUIP-STRIPPER · 分数 0.1123

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:172)

4.5 汽提塔｜EQUIP-STRIPPER

**功能与边界。**汽提塔接收分离器液相流 10，并使用流 4 的新鲜进料对其中残余反应物进行汽提。塔顶流 5 返回进料混合处，塔底流 11 输出产品混合物。流 4 虽常简称 C 进料，但其组分定义包含 A/C 混合物及 B。

**供热与产品。**汽提塔配置蒸汽供热及冷凝水侧。蒸汽是供热介质，不能与工艺产品物流合并。塔底产品含 G/H，后续把它们分离的精制系统不在 TE 基准内。

**记录字段。**X15、X16、X18 为塔液位、压力、温度；X17 为塔底流 11 的流量；X19 为蒸汽流量。X49 控制塔底产品排出，X50 为蒸汽阀操纵量。X37–X41 记录流 11 中 D/E/F/G/H 的摩尔百分数。

**常见混淆。**X22 不属于汽提塔；流 5 不是冷凝水；X37–X41 也不是“反应器组分”。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247、图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · SCOPE-001 · 分数 0.0987

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

### N15 · 该故障的预设扰动是什么？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "该故障的预设扰动是什么？",
  "normalized_query": "该故障的预设扰动是什么?",
  "retrieval_query": "IDV(12)的预设扰动是什么? IDV(12)",
  "entities": [
    {
      "kind": "fault",
      "number": 12,
      "canonical": "IDV(12)",
      "valid": true,
      "primary_unit": "FAULT-IDV12",
      "raw": "IDV(12)",
      "span": [
        0,
        7
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "FAULT-IDV12"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": true,
  "followup_version": "1.0.0",
  "previous_question": "IDV(12)是什么故障？",
  "resolved_query": "IDV(12)的预设扰动是什么?",
  "resolution_status": "resolved",
  "resolution_reason": "用上一轮唯一主体替换指代词，保留当前问法",
  "clarification": null,
  "context_units": []
}
```

上一问：IDV(12)是什么故障？。是否使用历史：True。实际检索问题：IDV(12)的预设扰动是什么? IDV(12)。

预期证据排名：`{"FAULT-IDV12": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV12 · 分数 0.3489

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:405)

7.12 IDV(12)：冷凝器冷却水入口温度随机变化｜FAULT-IDV12

- **扰动类型：**随机变化。
- **预设注入：**冷凝器冷却水入口温度随机变化。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X22 为出口温度，X52 为操纵量；X11 为分离器温度。
- **解释边界：**不能将入口温度扰动等同于 X52 阀门故障。
- **来源：**[S03，Process Disturbances 的 IDV(12)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · FAULT-IDV21 · 分数 0.4116

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486)

7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

- **扰动类型：**固定阀位（参考数据扩展）。
- **预设注入：**后续参考数据将本项定义为流 4 阀门位置保持常数。
- **可观测性：**X45 = XMV(4) 是对应进料操纵通道；X4 记录流 4 流量。
- **关联字段：**需结合具体生成器区分阀位固定值、控制命令和实际执行值。
- **解释边界：**不属于原始 1993 年 IDV(1)–(20) 表；固定阀位与 IDV(14)/(15) 的粘滞不能直接混用。
- **来源：**[S04，Fault Scenarios 的 d21](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULTS-001 · 分数 0.4091

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300)

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · SCOPE-001 · 分数 0.3279

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · VAR-X12 · 分数 0.2899

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:205)

X12 / XMEAS(12)：汽液分离器液位

- 条目 ID：VAR-X12
- 项目字段：X12
- 原始标识：XMEAS(12)
- 含义与测点：汽液分离器液位
- 单位：%

【继承的限定与来源】
【单位与来源】
液位 % 是模型的液位标度，不保证等于容器总体积百分比。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N16 · 这条流的去向呢？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "这条流的去向呢？",
  "normalized_query": "这条流的去向呢?",
  "retrieval_query": "流 6的去向呢? 流 6",
  "entities": [
    {
      "kind": "stream",
      "number": 6,
      "canonical": "流 6",
      "valid": true,
      "primary_unit": "STREAM-06",
      "raw": "流 6",
      "span": [
        0,
        3
      ]
    }
  ],
  "quantities": [],
  "intent": "process_topology",
  "intent_kinds": [
    "process_overview",
    "stream",
    "equipment"
  ],
  "primary_units": [
    "STREAM-06"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "询问进出口或物流连接，优先流程类资料",
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": true,
  "followup_version": "1.0.0",
  "previous_question": "流6是什么？",
  "resolved_query": "流 6的去向呢?",
  "resolution_status": "resolved",
  "resolution_reason": "用上一轮唯一主体替换指代词，保留当前问法",
  "clarification": null,
  "context_units": []
}
```

上一问：流6是什么？。是否使用历史：True。实际检索问题：流 6的去向呢? 流 6。

预期证据排名：`{"STREAM-06": 1}`。null 表示无正分命中。

#### 第 1 名 · STREAM-06 · 分数 0.0352

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:113)

TEP 流股 6：进料混合处 → 反应器

- 稳定 ID：STREAM-06
- 图中编号：6
- 上游 → 下游：进料混合处 → 反应器
- 物料及作用：新鲜原料和返回物流形成的总进料
- 本项目直接相关测量：X6 流量；X23–X28 的 A–F 组分

【继承的限定与来源】
【本节限定】
12/13 采用经典图 1 的公用工程编号；部分修订模型另有编号。X51/X52 是操纵量，没有提供以 m³/h 表示的独立冷却水流量测量列。汽提蒸汽/冷凝水在图上单独标注，本表不擅自赋予新的物料流号。

【本节限定】
依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，测量/操纵变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 2 名 · PROC-001 · 分数 0.0889

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:67)

3.1 从原料到产品，以及两条返回路径

TEP 的主设备为反应器、冷凝器、汽液分离器、循环压缩机和汽提塔。以下按物流讲解，**不是故障因果图**。

1. **原料补充与进料混合。**流 1 补充 A，流 2 补充 D，流 3 补充 E。这些原料与汽提塔顶返回的流 5、压缩机侧返回的循环流 8 汇合，形成流 6，进入反应器。流 6 是混合后的总进料，不能视为某一路新鲜原料。
2. **反应与移热。**反应器接收流 6，进行产品和副产物生成反应。内部冷却水回路承担移热。反应器物料通过流 7 离开并进入冷凝段；流 7 包含产品和未反应组分。
3. **冷却、冷凝与分相。**冷凝器先对反应器出料换热，使可凝组分形成液相。随后汽液分离器把气液两相分开。冷凝是热交换/相变环节，分离器是相分离及液体滞留环节，二者不可合并成一个变量名称。
4. **气相循环与排放。**分离器气相有两条去向：一部分经流 9 排出系统，另一部分经循环压缩机返回进料端，构成流 8。排放为循环系统提供物料出口；循环回收未反应组分。排放气并非只有 B 或 F，流 9 的分析仪记录 A–H 八个组分。
5. **液相汽提。**分离器液体由流 10 进入汽提塔。流 4 是含 A/C 的新鲜混合进料，它先进入汽提塔参与汽提，而不是从图上直接连到反应器。汽提塔还有蒸汽供热环节，塔顶物料通过流 5 返回反应器进料混合处。
6. **产品输出。**汽提塔底通过流 11 输出含 G/H 的产品混合物。它不是已经分成两路的纯 G、纯 H。后续产品精制不属于本基准的五个主设备。

这形成两条返回路径：**分离器气相 → 压缩机 → 进料混合处**，以及**分离器液相 → 汽提塔 → 塔顶返回进料混合处**。因此某条管线的结构上游，并不自动等同于统计诊断中的根源。

依据：[S01，图 2.3、§2.4](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)，对照 [S02，图 1、p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。设备和流股的文本连接为本手册依据上述图示整理。

【继承的限定与来源】
【来源差异处理】
- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 3 名 · EQUIP-REACTOR · 分数 0.0535

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:130)

4.1 反应器｜EQUIP-REACTOR

**功能与边界。**反应器是发生四条反应的设备，接收混合进料流 6，经流 7 向冷凝器排出物料。进料侧同时受到新鲜原料和循环物料的影响；仅看一条新鲜进料无法完整描述反应器入口组成。

**换热与内部操作。**反应放热，内部冷却束负责移热，搅拌器是原始模型的另一操纵对象。冷却水和反应物料隔着换热面交换热量，不能把冷却水入口当作进入反应器参与反应的进料。

**记录字段。**X6 为流 6 总流量；X7、X8、X9 分别是反应器压力、液位、温度。X21 是反应器冷却水出口温度；X51 是冷却水操纵通道。X23–X28 是入口流 6 的组分分析，并非反应器内部液相组分。搅拌器转速不在本项目 52 列中。

**与故障表的连接。**IDV(4)/(11) 改变冷却水入口温度，IDV(14) 对应冷却水阀粘滞，IDV(13) 改变反应动力学。这些物理位置相近但扰动类型不同；不能合并成“X9 温度故障”。

依据：[S01，§2.4、图 2.3、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量及扰动声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · EQUIP-STRIPPER · 分数 0.0272

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:172)

4.5 汽提塔｜EQUIP-STRIPPER

**功能与边界。**汽提塔接收分离器液相流 10，并使用流 4 的新鲜进料对其中残余反应物进行汽提。塔顶流 5 返回进料混合处，塔底流 11 输出产品混合物。流 4 虽常简称 C 进料，但其组分定义包含 A/C 混合物及 B。

**供热与产品。**汽提塔配置蒸汽供热及冷凝水侧。蒸汽是供热介质，不能与工艺产品物流合并。塔底产品含 G/H，后续把它们分离的精制系统不在 TE 基准内。

**记录字段。**X15、X16、X18 为塔液位、压力、温度；X17 为塔底流 11 的流量；X19 为蒸汽流量。X49 控制塔底产品排出，X50 为蒸汽阀操纵量。X37–X41 记录流 11 中 D/E/F/G/H 的摩尔百分数。

**常见混淆。**X22 不属于汽提塔；流 5 不是冷凝水；X37–X41 也不是“反应器组分”。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247、图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · EQUIP-SEPARATOR · 分数 0.0189

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:152)

4.3 汽液分离器｜EQUIP-SEPARATOR

**功能与边界。**接收冷凝后的反应器出料，形成气相和液相出口。气相进入循环与排放两条支路；液相流 10 进入汽提塔。分离器中有液体存量，因此液位与液相流出量是两个不同量。

**记录字段。**X11 温度、X12 液位、X13 压力描述分离器状态，X14 记录流 10 流量，X48 是该液体排出操纵通道。流 9 的排放量是 X10，操纵通道是 X47，气体组分是 X29–X36。

**作用说明。**气相循环回收物料；气相排放为惰性组分和副产物等提供排出通道。分离器不是 G/H 的最终精制设备；流 10 还需进入汽提塔，不能称作最终产品。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N17 · 那12呢？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "那12呢？",
  "normalized_query": "那12呢?",
  "retrieval_query": "XMV(12)是什么? XMV(12)",
  "entities": [
    {
      "kind": "xmv",
      "number": 12,
      "canonical": "XMV(12)",
      "valid": true,
      "primary_unit": null,
      "raw": "XMV(12)",
      "span": [
        0,
        7
      ]
    }
  ],
  "quantities": [],
  "intent": "data_schema",
  "intent_kinds": [
    "scope",
    "variable_conventions"
  ],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [
    "XMV(12) 是搅拌器操纵量，但未记录在52列文件中；不映射为X53"
  ],
  "reasons": [
    "询问数据列/操纵变量覆盖范围"
  ],
  "context_used": true,
  "followup_version": "1.0.0",
  "previous_question": "XMV(11)是什么？",
  "resolved_query": "XMV(12)是什么?",
  "resolution_status": "resolved",
  "resolution_reason": "从上一轮继承 xmv 类型及问法，仅替换主体编号",
  "clarification": null,
  "context_units": [
    "VAR-X52"
  ]
}
```

上一问：XMV(11)是什么？。是否使用历史：True。实际检索问题：XMV(12)是什么? XMV(12)。

预期证据排名：`{"SCOPE-001": 1}`。null 表示无正分命中。

#### 第 1 名 · SCOPE-001 · 分数 0.2141

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22)

1. 适用范围与术语｜SCOPE-001

- TE、TEP、Tennessee Eastman Process、田纳西伊斯曼过程：本文中指同一过程控制基准。
- 设备编号、物流编号、测量变量编号和故障编号是不同体系。“流 4”是物料通道，“X4”是该通道的进料流量记录，“IDV(4)”则是反应器冷却水入口温度扰动。
- `X1–X41 = XMEAS(1)–XMEAS(41)`；`X42–X52 = XMV(1)–XMV(11)`。Python 的列位置比 X 编号小 1。
- 原始模型有 12 个操纵变量；第 12 个是搅拌器转速。本项目的 52 列文件没有收录它，不能自行增加一个 X53 后假定与原文件一致。
- 原始故障表包含 IDV(1)–IDV(20)；本文另外记录参考数据版本中的 IDV(21)，并标明其版本来源。
- 图和物流编号采用经典 TE 版本。不同修订模型可能重编号、增加传感器、改变控制器；不能只凭“TEP”名称合并定义。

依据：[S01，§2.4、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 3–5/8](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，文件头接口说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)、[S04，File Format / Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 2 名 · VARS-001 · 分数 0.0596

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:184)

5. 完整变量字典｜VARS-001

本节复用论文表 2-1 的 X1–X52 顺序，补齐原始标识、单位和测点范围；有冲突的中文名称见第 8 节。每行的 `VAR-Xnn` 是知识条目 ID，便于稳定引用。

**单位约定：**kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。kPa(g) 为表压。mol% 为摩尔百分数，不能当作质量百分数。液位 % 是模型的液位标度，不保证等于容器总体积百分比。操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【继承的限定与来源】
【来源差异处理】
- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · VAR-X12 · 分数 0.3415

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:205)

X12 / XMEAS(12)：汽液分离器液位

- 条目 ID：VAR-X12
- 项目字段：X12
- 原始标识：XMEAS(12)
- 含义与测点：汽液分离器液位
- 单位：%

【继承的限定与来源】
【单位与来源】
液位 % 是模型的液位标度，不保证等于容器总体积百分比。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · FAULT-IDV12 · 分数 0.2658

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:405)

7.12 IDV(12)：冷凝器冷却水入口温度随机变化｜FAULT-IDV12

- **扰动类型：**随机变化。
- **预设注入：**冷凝器冷却水入口温度随机变化。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X22 为出口温度，X52 为操纵量；X11 为分离器温度。
- **解释边界：**不能将入口温度扰动等同于 X52 阀门故障。
- **来源：**[S03，Process Disturbances 的 IDV(12)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · C02 · 分数 0.2407

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:500)

来源差异 C02：冷凝器冷却水操纵量 XMV(11)

- ID：C02
- 问题：论文表 2-1 将 X52 写成压缩机冷却水流量
- 本手册采用的表述：冷凝器冷却水操纵量 XMV(11)
- 核对依据与状态：S03 的 XMV(11)；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### N18 · IDV(19)的确切物理起因有记载吗？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "IDV(19)的确切物理起因有记载吗？",
  "normalized_query": "IDV(19)的确切物理起因有记载吗?",
  "retrieval_query": "IDV(19)的确切物理起因有记载吗? IDV(19)",
  "entities": [
    {
      "kind": "fault",
      "number": 19,
      "canonical": "IDV(19)",
      "valid": true,
      "primary_unit": "FAULT-IDV19",
      "raw": "IDV(19)",
      "span": [
        0,
        7
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "FAULT-IDV19"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "IDV(19)的确切物理起因有记载吗？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{"FAULT-IDV19": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV19 · 分数 0.4192

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:468)

7.19 IDV(19)：未公开定义的预设故障 19｜FAULT-IDV19

- **扰动类型：**Unknown。
- **预设注入：**原始故障清单将本项标为 Unknown；本版本没有经核实的具体物理定义。
- **可观测性：**无法建立已确认的注入量—X 字段映射。
- **关联字段：**保留故障编号供检索和实验索引；不指定根源 X。
- **解释边界：**未知定义不表示没有故障，也不表示算法不能分析；推测必须作为实验结论另行保存。
- **来源：**[S03，Process Disturbances 的 IDV(19)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 2 名 · FAULT-IDV21 · 分数 0.4333

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486)

7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

- **扰动类型：**固定阀位（参考数据扩展）。
- **预设注入：**后续参考数据将本项定义为流 4 阀门位置保持常数。
- **可观测性：**X45 = XMV(4) 是对应进料操纵通道；X4 记录流 4 流量。
- **关联字段：**需结合具体生成器区分阀位固定值、控制命令和实际执行值。
- **解释边界：**不属于原始 1993 年 IDV(1)–(20) 表；固定阀位与 IDV(14)/(15) 的粘滞不能直接混用。
- **来源：**[S04，Fault Scenarios 的 d21](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULTS-001 · 分数 0.4216

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300)

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · VAR-X19 · 分数 0.3391

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:212)

X19 / XMEAS(19)：汽提塔蒸汽流量

- 条目 ID：VAR-X19
- 项目字段：X19
- 原始标识：XMEAS(19)
- 含义与测点：汽提塔蒸汽流量
- 单位：kg/h

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · C04 · 分数 0.3383

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:502)

来源差异 C04：IDV(16)–(20) 为 Unknown；21 按扩展数据说明

- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

### B01 · 那6呢？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "那6呢？",
  "normalized_query": "那6呢?",
  "retrieval_query": "",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": true,
  "issues": [
    "存在没有类型标识的数字；本阶段不根据历史猜测编号类型"
  ],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "那6呢？",
  "resolution_status": "needs_clarification",
  "resolution_reason": "缺少可用上一轮问题",
  "clarification": "这次指的是哪个故障、变量或流股？请补充具体编号。",
  "context_units": []
}
```

预期证据排名：`{}`。null 表示无正分命中。

### B02 · 它的单位呢？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "它的单位呢？",
  "normalized_query": "它的单位呢?",
  "retrieval_query": "",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "X2和X3分别是什么？",
  "resolved_query": "它的单位呢？",
  "resolution_status": "needs_clarification",
  "resolution_reason": "上一问没有唯一且有效的主体，不能安全继承",
  "clarification": "这次指的是哪个故障、变量或流股？请补充具体编号。",
  "context_units": []
}
```

上一问：X2和X3分别是什么？。是否使用历史：False。实际检索问题：待澄清，未检索。

预期证据排名：`{}`。null 表示无正分命中。

### B03 · 那99呢？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "那99呢？",
  "normalized_query": "那99呢?",
  "retrieval_query": "",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": true,
  "issues": [
    "存在没有类型标识的数字；本阶段不根据历史猜测编号类型"
  ],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "IDV(7)是什么？",
  "resolved_query": "那99呢？",
  "resolution_status": "needs_clarification",
  "resolution_reason": "继承类型后编号越界",
  "clarification": "按上一轮的 fault 类型，编号 99 超出当前手册范围；请核对编号或说明类型。",
  "context_units": []
}
```

上一问：IDV(7)是什么？。是否使用历史：False。实际检索问题：待澄清，未检索。

预期证据排名：`{}`。null 表示无正分命中。

### B04 · 今天杭州天气怎么样？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "今天杭州天气怎么样？",
  "normalized_query": "今天杭州天气怎么样?",
  "retrieval_query": "今天杭州天气怎么样?",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "今天杭州天气怎么样？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{}`。null 表示无正分命中。

### B05 · 帮我写一首关于春天的诗

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "帮我写一首关于春天的诗",
  "normalized_query": "帮我写一首关于春天的诗",
  "retrieval_query": "帮我写一首关于春天的诗",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": true,
  "issues": [
    "存在没有类型标识的数字；本阶段不根据历史猜测编号类型"
  ],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "帮我写一首关于春天的诗",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{}`。null 表示无正分命中。

### B06 · 怎样重置Windows登录密码？

规则解析：

```json
{
  "parser_version": "1.1.0",
  "original_query": "怎样重置Windows登录密码？",
  "normalized_query": "怎样重置Windows登录密码?",
  "retrieval_query": "怎样重置Windows登录密码?",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [],
  "context_used": false,
  "followup_version": "1.0.0",
  "previous_question": "",
  "resolved_query": "怎样重置Windows登录密码？",
  "resolution_status": "standalone",
  "resolution_reason": "当前问题独立解析",
  "clarification": null,
  "context_units": []
}
```

预期证据排名：`{}`。null 表示无正分命中。

#### 第 1 名 · EQUIP-CONDENSER · 分数 0.0663

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:142)

4.2 冷凝器｜EQUIP-CONDENSER

**功能与边界。**冷凝器接收流 7 的反应器出料，通过冷却使可凝部分形成液体，之后送往汽液分离器。冷凝器负责换热，分离器负责把形成的气液两相分开。

**公用工程。**其冷却水属于独立换热侧。X52 对应冷凝器冷却水操纵量；X22 的原始测量名称为“Separator Cooling Water Outlet Temperature”，本文称为“分离器冷却水出口温度（对应冷凝冷却系统）”，保留原名以便核对。它不是汽提塔冷却水，也不是压缩机冷却水。

**记录局限。**52 列没有直接记录这一冷却水入口温度。IDV(5)/(12) 的扰动定义不能直接等同于 X22，因为入口温度与出口温度是不同物理量；IDV(15) 则是该冷却水阀门粘滞。

依据：[S01，图 2.3](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1、表 4](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，XMEAS(22)、XMV(11)、IDV(5)/(12)/(15)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

【继承的限定与来源】
【来源差异处理】
- ID：C01
- 问题：论文表 2-1 将 X22 写成汽提塔冷却水出口温度
- 本手册采用的表述：分离器冷却水出口温度，对应冷凝冷却系统
- 核对依据与状态：S03 的 XMEAS(22)，S02 表 4；已记录纠正

【来源差异处理】
- ID：C02
- 问题：论文表 2-1 将 X52 写成压缩机冷却水流量
- 本手册采用的表述：冷凝器冷却水操纵量 XMV(11)
- 核对依据与状态：S03 的 XMV(11)；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · C04 · 分数 0.0418

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:502)

来源差异 C04：IDV(16)–(20) 为 Unknown；21 按扩展数据说明

- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 3 名 · FAULT-IDV17 · 分数 0.0361

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:450)

7.17 IDV(17)：未公开定义的预设故障 17｜FAULT-IDV17

- **扰动类型：**Unknown。
- **预设注入：**原始故障清单将本项标为 Unknown；本版本没有经核实的具体物理定义。
- **可观测性：**无法建立已确认的注入量—X 字段映射。
- **关联字段：**保留故障编号供检索和实验索引；不指定根源 X。
- **解释边界：**未知定义不表示没有故障，也不表示算法不能分析；推测必须作为实验结论另行保存。
- **来源：**[S03，Process Disturbances 的 IDV(17)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · FAULT-IDV19 · 分数 0.0361

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:468)

7.19 IDV(19)：未公开定义的预设故障 19｜FAULT-IDV19

- **扰动类型：**Unknown。
- **预设注入：**原始故障清单将本项标为 Unknown；本版本没有经核实的具体物理定义。
- **可观测性：**无法建立已确认的注入量—X 字段映射。
- **关联字段：**保留故障编号供检索和实验索引；不指定根源 X。
- **解释边界：**未知定义不表示没有故障，也不表示算法不能分析；推测必须作为实验结论另行保存。
- **来源：**[S03，Process Disturbances 的 IDV(19)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · FAULT-IDV18 · 分数 0.0361

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:459)

7.18 IDV(18)：未公开定义的预设故障 18｜FAULT-IDV18

- **扰动类型：**Unknown。
- **预设注入：**原始故障清单将本项标为 Unknown；本版本没有经核实的具体物理定义。
- **可观测性：**无法建立已确认的注入量—X 字段映射。
- **关联字段：**保留故障编号供检索和实验索引；不指定根源 X。
- **解释边界：**未知定义不表示没有故障，也不表示算法不能分析；推测必须作为实验结论另行保存。
- **来源：**[S03，Process Disturbances 的 IDV(18)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

## 评测边界

- 开发回归集18问，不是独立测试集
- 只评测检索证据，不评测答案正确性或抗注入能力
- 只使用显式提供的上一轮用户问题；复杂指代仍可能需要澄清
- 相关性标签为人工整理的候选证据，支持进一步复核
- 相似度不是正确概率
