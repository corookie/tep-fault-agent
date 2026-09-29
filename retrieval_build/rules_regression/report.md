# TEP 编号与意图规则检索报告

本轮检索110个新片段，不调用聊天模型。这里的“完整”指预先登记的证据组全部命中，不表示回答已经正确。

评测集：query-rules-regression-v1；时间：2026-09-27T02:10:26.144873+00:00。

## 总体结果

| 返回数量（不设0.16阈值） | 至少命中一组证据 | 所有必要证据齐全 |
| --- | ---: | ---: |
| 前 1 块 | 8/9 | 7/9 |
| 前 3 块 | 9/9 | 9/9 |
| 前 5 块 | 9/9 | 9/9 |
| 前 10 块 | 9/9 | 9/9 |

前三块再按原始相似度≥0.16筛选：证据完整 5/9；无关问题拒绝 3/3。

阈值0的列表仅供诊断排序，零分片段不返回；它不是经过校准的上线配置。关键词索引使用标题、实体和正文，去掉链接地址以避免路径文字干扰。

## 逐题结果

| 问题 | 前5块证据完整 | 前3名 | 未命中的证据组 |
| --- | --- | --- | --- |
| R01：能解释一下第十五个故障吗？ | 是 | FAULT-IDV15 (0.373)；FAULT-IDV21 (0.395)；FAULTS-001 (0.371) | — |
| R02：xmeas(4) 和 XMV（4）各自指什么？ | 是 | VAR-X04 (0.354)；VAR-X45 (0.313)；FAULT-IDV04 (0.202) | — |
| R03：流股四先送到哪个设备？ | 是 | STREAM-04 (0.065)；FAULT-IDV01 (0.165)；FAULT-IDV10 (0.133) | — |
| R04：我们验证过全部21种故障了吗？ | 是 | DATA-FILES (0.065)；LIMITS-001 (0.048)；FAULT-IDV17 (0.023) | — |
| R05：ＩＤＶ（９）定义是什么？ | 是 | FAULT-IDV09 (0.381)；FAULT-IDV21 (0.361)；FAULTS-001 (0.358) | — |
| R06：为什么X29到X36的组分总和要注意噪声？ | 是 | DATA-002 (0.053)；VAR-X36 (0.271)；VAR-X35 (0.250) | — |
| R07：循环压缩机和汽提塔是怎么连接的？ | 是 | PROC-001 (0.164)；EQUIP-COMPRESSOR (0.217)；STREAM-08 (0.083) | — |
| R08：A进料丢失对应哪个故障？ | 是 | C01 (0.084)；VAR-X22 (0.079)；FAULT-IDV06 (0.063) | — |
| R09：XMV(12)为什么不在数据文件里？ | 是 | SCOPE-001 (0.196)；VARS-001 (0.059)；VAR-X12 (0.303) | — |
| RN01：IDV(99)是什么 | 无关问题 | 无 | — |
| RN02：流99是什么 | 无关问题 | 无 | — |
| RN03：这21个软件都测试过了吗 | 无关问题 | VAR-X21 (0.128)；FAULT-IDV21 (0.052)；C04 (0.050) | — |

## 每题命中文本与来源

### R01 · 能解释一下第十五个故障吗？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "能解释一下第十五个故障吗？",
  "normalized_query": "能解释一下第十五个故障吗?",
  "retrieval_query": "能解释一下第十五个故障吗? IDV(15)",
  "entities": [
    {
      "kind": "fault",
      "number": 15,
      "canonical": "IDV(15)",
      "valid": true,
      "primary_unit": "FAULT-IDV15",
      "raw": "第十五个故障",
      "span": [
        5,
        11
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
  "context_used": false
}
```

预期证据排名：`{"FAULT-IDV15": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV15 · 分数 0.3734

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

#### 第 2 名 · FAULT-IDV21 · 分数 0.3950

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

#### 第 3 名 · FAULTS-001 · 分数 0.3706

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

#### 第 4 名 · VAR-X15 · 分数 0.2923

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

#### 第 5 名 · SCOPE-001 · 分数 0.2915

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

### R02 · xmeas(4) 和 XMV（4）各自指什么？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "xmeas(4) 和 XMV（4）各自指什么？",
  "normalized_query": "xmeas(4) 和 XMV(4)各自指什么?",
  "retrieval_query": "xmeas(4) 和 XMV(4)各自指什么? XMEAS(4) XMV(4)",
  "entities": [
    {
      "kind": "xmeas",
      "number": 4,
      "canonical": "XMEAS(4)",
      "valid": true,
      "primary_unit": "VAR-X04",
      "raw": "xmeas(4)",
      "span": [
        0,
        8
      ]
    },
    {
      "kind": "xmv",
      "number": 4,
      "canonical": "XMV(4)",
      "valid": true,
      "primary_unit": "VAR-X45",
      "raw": "XMV(4)",
      "span": [
        11,
        17
      ]
    }
  ],
  "quantities": [],
  "intent": "entity_lookup",
  "intent_kinds": [],
  "primary_units": [
    "VAR-X04",
    "VAR-X45"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false
}
```

预期证据排名：`{"VAR-X04": 1, "VAR-X45": 2}`。null 表示无正分命中。

#### 第 1 名 · VAR-X04 · 分数 0.3538

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:197)

X4 / XMEAS(4)：A/C 混合进料总流量；流 4

- 条目 ID：VAR-X04
- 项目字段：X4
- 原始标识：XMEAS(4)
- 含义与测点：A/C 混合进料总流量；流 4
- 单位：kscmh

【继承的限定与来源】
【单位与来源】
kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

排序依据：编号主体精确匹配；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · VAR-X45 · 分数 0.3129

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:250)

X45 / XMV(4)：A/C 进料操纵量；流 4

- 条目 ID：VAR-X45
- 项目字段：X45
- 原始标识：XMV(4)
- 含义与作用对象：A/C 进料操纵量；流 4
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

#### 第 3 名 · FAULT-IDV04 · 分数 0.2017

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:333)

7.4 IDV(4)：反应器冷却水入口温度变化｜FAULT-IDV04

- **扰动类型：**阶跃。
- **预设注入：**反应器冷却水入口温度改变。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X21 为冷却水出口温度，X51 为冷却水操纵量；X9 为反应器温度。
- **解释边界：**不能把出口温度 X21 当作入口温度的同义字段。
- **来源：**[S03，Process Disturbances 的 IDV(4)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · VAR-X41 · 分数 0.1996

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

#### 第 5 名 · VAR-X40 · 分数 0.1961

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:240)

X40 / XMEAS(40)：塔底产品中 G；流 11

- 条目 ID：VAR-X40
- 项目字段：X40
- 原始标识：XMEAS(40)
- 含义与测点：塔底产品中 G；流 11
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

### R03 · 流股四先送到哪个设备？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "流股四先送到哪个设备？",
  "normalized_query": "流股四先送到哪个设备?",
  "retrieval_query": "流股四先送到哪个设备? 流 4",
  "entities": [
    {
      "kind": "stream",
      "number": 4,
      "canonical": "流 4",
      "valid": true,
      "primary_unit": "STREAM-04",
      "raw": "流股四",
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
    "STREAM-04"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false
}
```

预期证据排名：`{"STREAM-04": 1}`。null 表示无正分命中。

#### 第 1 名 · STREAM-04 · 分数 0.0654

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:111)

TEP 流股 4：A/C 原料边界 → 汽提塔

- 稳定 ID：STREAM-04
- 图中编号：4
- 上游 → 下游：A/C 原料边界 → 汽提塔
- 物料及作用：含 A、C 和 B 的进料，参与汽提
- 本项目直接相关测量：X4 总流量；没有流 4 组分/温度/总管压力直接记录

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

#### 第 2 名 · FAULT-IDV01 · 分数 0.1649

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:306)

7.1 IDV(1)：流 4 的 A/C 比例变化｜FAULT-IDV01

- **扰动类型：**阶跃。
- **预设注入：**流 4 的 A/C 比例改变，B 组分保持不变。
- **可观测性：**无直接记录：52 列不含流 4 的 A/C 比例。
- **关联字段：**X4 是流 4 总流量；X23、X25 是下游流 6 的 A、C 组分。
- **解释边界：**流 6 的组分不能直接改名为流 4 的注入组分。
- **来源：**[S03，Process Disturbances 的 IDV(1)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · FAULT-IDV10 · 分数 0.1330

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

#### 第 4 名 · FAULT-IDV02 · 分数 0.1114

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:315)

7.2 IDV(2)：流 4 的 B 组分变化｜FAULT-IDV02

- **扰动类型：**阶跃。
- **预设注入：**流 4 的 B 组分改变，A/C 比例保持不变。
- **可观测性：**无直接记录：52 列不含流 4 的 B 组分。
- **关联字段：**X24 是下游流 6 的 B，X30 是排放流 9 的 B。
- **解释边界：**不能把 X24 或 X30 固定标为本故障的标准根源。
- **来源：**[S03，Process Disturbances 的 IDV(2)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · FAULT-IDV07 · 分数 0.1097

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:360)

7.7 IDV(7)：C 进料总管压力损失｜FAULT-IDV07

- **扰动类型：**阶跃。
- **预设注入：**流 4 的进料总管压力下降，供料可用性降低。
- **可观测性：**无直接记录：52 列没有该总管压力。
- **关联字段：**X4 为流 4 流量，X45 为流 4 进料操纵量。
- **解释边界：**X4 不是压力；流 4 不应按简称 C 进料理解为纯 C。
- **来源：**[S03，Process Disturbances 的 IDV(7)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### R04 · 我们验证过全部21种故障了吗？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "我们验证过全部21种故障了吗？",
  "normalized_query": "我们验证过全部21种故障了吗?",
  "retrieval_query": "我们验证过全部 故障了吗?",
  "entities": [],
  "quantities": [
    {
      "text": "21种",
      "number": 21,
      "unit": "种",
      "span": [
        7,
        10
      ]
    }
  ],
  "intent": "validation_scope",
  "intent_kinds": [
    "dataset_scope"
  ],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "询问已做实验/验证的范围，优先数据范围说明"
  ],
  "context_used": false
}
```

预期证据排名：`{"DATA-FILES": 1}`。null 表示无正分命中。

#### 第 1 名 · DATA-FILES · 分数 0.0653

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:279)

6.2 当前项目数据范围

当前已使用正常工况 `d00_te.dat` 和故障 7 的 `d07_te.dat`。本地检查结果均为 960 行、52 列，没有缺失值或无穷值；这只适用于当前两个文件，不代表全部 TEP 数据都没有异常值。

论文实验约定为每 3 分钟记录一次、48 小时测试、8 小时后注入故障；当前项目据此前 160 点为正常段，后续段作故障分析。该约定不能自动推广到其他仿真器、训练文件或重新生成的数据，换文件时需重新核对时间轴和注入点。

本地数据的下载地址、文件哈希及首次检查见 [data/README.md](/Users/rowen/Documents/高校/tep-fault-agent/data/README.md)。这里的故障目录覆盖 21 类，**不代表当前诊断功能已对 21 类逐一验证**。

依据：[S01，§2.4 的实验数据说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S04，文件结构说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)、本项目数据检查记录。

排序依据：意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 2 名 · LIMITS-001 · 分数 0.0481

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:510)

本知识库的未知项与适用边界

**当前保留的未知：**IDV(16)–(20) 的可靠物理解释；当前数据生成器完整控制回路及参数是否与其他公开版本一致；未测入口量的真实时间曲线；全部 21 类诊断结果；各故障的可信动态传播路径。这些内容不能靠语言模型补齐。

**不纳入本版的内容：**各操作模式的全套稳态表、设备尺寸/物性常数、控制器整定和全套停机阈值。它们适合后续仿真或控制问答专题，不能从当前两份样本数据推断。若用户问到，应检索相应原始章节后再建立独立、带版本的条目。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：

#### 第 3 名 · FAULT-IDV17 · 分数 0.0232

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

#### 第 4 名 · FAULT-IDV19 · 分数 0.0232

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

#### 第 5 名 · FAULT-IDV18 · 分数 0.0232

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

### R05 · ＩＤＶ（９）定义是什么？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "ＩＤＶ（９）定义是什么？",
  "normalized_query": "IDV(9)定义是什么?",
  "retrieval_query": "IDV(9)定义是什么? IDV(9)",
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
  "context_used": false
}
```

预期证据排名：`{"FAULT-IDV09": 1}`。null 表示无正分命中。

#### 第 1 名 · FAULT-IDV09 · 分数 0.3805

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

#### 第 2 名 · FAULT-IDV21 · 分数 0.3605

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

#### 第 3 名 · FAULTS-001 · 分数 0.3581

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

#### 第 4 名 · SCOPE-001 · 分数 0.2661

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

#### 第 5 名 · VAR-X09 · 分数 0.2655

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

### R06 · 为什么X29到X36的组分总和要注意噪声？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "为什么X29到X36的组分总和要注意噪声？",
  "normalized_query": "为什么X29到X36的组分总和要注意噪声?",
  "retrieval_query": "为什么X29到X36的组分总和要注意噪声? X29 X30 X31 X32 X33 X34 X35 X36",
  "entities": [
    {
      "kind": "variable",
      "number": 29,
      "canonical": "X29",
      "valid": true,
      "primary_unit": "VAR-X29",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 30,
      "canonical": "X30",
      "valid": true,
      "primary_unit": "VAR-X30",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 31,
      "canonical": "X31",
      "valid": true,
      "primary_unit": "VAR-X31",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 32,
      "canonical": "X32",
      "valid": true,
      "primary_unit": "VAR-X32",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 33,
      "canonical": "X33",
      "valid": true,
      "primary_unit": "VAR-X33",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 34,
      "canonical": "X34",
      "valid": true,
      "primary_unit": "VAR-X34",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 35,
      "canonical": "X35",
      "valid": true,
      "primary_unit": "VAR-X35",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    },
    {
      "kind": "variable",
      "number": 36,
      "canonical": "X36",
      "valid": true,
      "primary_unit": "VAR-X36",
      "raw": "X29到X36",
      "span": [
        3,
        10
      ]
    }
  ],
  "quantities": [],
  "intent": "composition_sum",
  "intent_kinds": [
    "editorial_guidance"
  ],
  "primary_units": [
    "VAR-X29",
    "VAR-X30",
    "VAR-X31",
    "VAR-X32",
    "VAR-X33",
    "VAR-X34",
    "VAR-X35",
    "VAR-X36"
  ],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "组分变量的求和/归一化问题，优先数据解释，再保留变量定义",
    "仅按片段unit_id识别主体，不把正文或entities中提到的编号当作主体"
  ],
  "context_used": false
}
```

预期证据排名：`{"DATA-002": 1}`。null 表示无正分命中。

#### 第 1 名 · DATA-002 · 分数 0.0534

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

排序依据：组分求和解释；优先级 3；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 2 名 · VAR-X36 · 分数 0.2707

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:236)

X36 / XMEAS(36)：排放气中 H；流 9

- 条目 ID：VAR-X36
- 项目字段：X36
- 原始标识：XMEAS(36)
- 含义与测点：排放气中 H；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：编号主体；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · VAR-X35 · 分数 0.2503

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:235)

X35 / XMEAS(35)：排放气中 G；流 9

- 条目 ID：VAR-X35
- 项目字段：X35
- 原始标识：XMEAS(35)
- 含义与测点：排放气中 G；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：编号主体；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · VAR-X32 · 分数 0.2491

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:232)

X32 / XMEAS(32)：排放气中 D；流 9

- 条目 ID：VAR-X32
- 项目字段：X32
- 原始标识：XMEAS(32)
- 含义与测点：排放气中 D；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：编号主体；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 5 名 · VAR-X34 · 分数 0.2486

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:234)

X34 / XMEAS(34)：排放气中 F；流 9

- 条目 ID：VAR-X34
- 项目字段：X34
- 原始标识：XMEAS(34)
- 含义与测点：排放气中 F；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

排序依据：编号主体；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### R07 · 循环压缩机和汽提塔是怎么连接的？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "循环压缩机和汽提塔是怎么连接的？",
  "normalized_query": "循环压缩机和汽提塔是怎么连接的?",
  "retrieval_query": "循环压缩机和汽提塔是怎么连接的?",
  "entities": [],
  "quantities": [],
  "intent": "process_topology",
  "intent_kinds": [
    "process_overview",
    "stream",
    "equipment"
  ],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [
    "询问进出口或物流连接，优先流程类资料"
  ],
  "context_used": false
}
```

预期证据排名：`{"PROC-001": 1}`。null 表示无正分命中。

#### 第 1 名 · PROC-001 · 分数 0.1642

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

排序依据：流程意图匹配；优先级 2；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 2 名 · EQUIP-COMPRESSOR · 分数 0.2173

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:162)

4.4 循环压缩机｜EQUIP-COMPRESSOR

**功能与边界。**循环压缩机处理分离器未凝气相循环支路，使循环物流经流 8 返回进料侧。经典图中还画有压缩机旁路/回流阀，因此“压缩机循环阀”不能简单画成串在流 8 上的普通进料阀。

**记录字段。**X5 是流 8 循环流量，X20 是压缩机功率，X46 = XMV(5) 是压缩机循环阀操纵量。功率单位 kW，既不是压力，也不是累计耗电量 kWh。

**知识边界。**这些变量说明部件、测点和执行通道关系，不能据此预先规定 X46 增加时所有工况下 X5 都按同一方向变化。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，XMEAS(5)/(20)、XMV(5)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：流程意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · STREAM-08 · 分数 0.0834

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

排序依据：流程意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 4 名 · STREAM-05 · 分数 0.0523

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:112)

TEP 流股 5：汽提塔顶 → 进料混合处

- 稳定 ID：STREAM-05
- 图中编号：5
- 上游 → 下游：汽提塔顶 → 进料混合处
- 物料及作用：汽提塔顶返回物料
- 本项目直接相关测量：没有独立流量列

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

排序依据：流程意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)

#### 第 5 名 · EQUIP-STRIPPER · 分数 0.0425

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:172)

4.5 汽提塔｜EQUIP-STRIPPER

**功能与边界。**汽提塔接收分离器液相流 10，并使用流 4 的新鲜进料对其中残余反应物进行汽提。塔顶流 5 返回进料混合处，塔底流 11 输出产品混合物。流 4 虽常简称 C 进料，但其组分定义包含 A/C 混合物及 B。

**供热与产品。**汽提塔配置蒸汽供热及冷凝水侧。蒸汽是供热介质，不能与工艺产品物流合并。塔底产品含 G/H，后续把它们分离的精制系统不在 TE 基准内。

**记录字段。**X15、X16、X18 为塔液位、压力、温度；X17 为塔底流 11 的流量；X19 为蒸汽流量。X49 控制塔底产品排出，X50 为蒸汽阀操纵量。X37–X41 记录流 11 中 D/E/F/G/H 的摩尔百分数。

**常见混淆。**X22 不属于汽提塔；流 5 不是冷凝水；X37–X41 也不是“反应器组分”。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247、图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

排序依据：流程意图匹配；优先级 1；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### R08 · A进料丢失对应哪个故障？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "A进料丢失对应哪个故障？",
  "normalized_query": "A进料丢失对应哪个故障?",
  "retrieval_query": "A进料丢失对应哪个故障?",
  "entities": [],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [],
  "context_used": false
}
```

预期证据排名：`{"FAULT-IDV06": 3}`。null 表示无正分命中。

#### 第 1 名 · C01 · 分数 0.0835

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:499)

来源差异 C01：分离器冷却水出口温度，对应冷凝冷却系统

- ID：C01
- 问题：论文表 2-1 将 X22 写成汽提塔冷却水出口温度
- 本手册采用的表述：分离器冷却水出口温度，对应冷凝冷却系统
- 核对依据与状态：S03 的 XMEAS(22)，S02 表 4；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 2 名 · VAR-X22 · 分数 0.0792

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

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 3 名 · FAULT-IDV06 · 分数 0.0629

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:351)

7.6 IDV(6)：A 进料损失｜FAULT-IDV06

- **扰动类型：**阶跃。
- **预设注入：**流 1 的 A 进料供应损失。
- **可观测性：**X1 直接记录受影响的流 1 流量；供应损失原因未由独立传感器记录。
- **关联字段：**X44 为 A 进料操纵量。
- **解释边界：**进料损失不等于已证明阀门损坏。
- **来源：**[S03，Process Disturbances 的 IDV(6)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

#### 第 4 名 · FAULT-IDV17 · 分数 0.0617

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

#### 第 5 名 · FAULT-IDV19 · 分数 0.0617

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

### R09 · XMV(12)为什么不在数据文件里？

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "XMV(12)为什么不在数据文件里？",
  "normalized_query": "XMV(12)为什么不在数据文件里?",
  "retrieval_query": "XMV(12)为什么不在数据文件里? XMV(12)",
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
  "context_used": false
}
```

预期证据排名：`{"SCOPE-001": 1}`。null 表示无正分命中。

#### 第 1 名 · SCOPE-001 · 分数 0.1964

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

#### 第 2 名 · VARS-001 · 分数 0.0588

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

#### 第 3 名 · VAR-X12 · 分数 0.3027

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

#### 第 4 名 · FAULT-IDV12 · 分数 0.2389

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

#### 第 5 名 · C02 · 分数 0.2123

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:500)

来源差异 C02：冷凝器冷却水操纵量 XMV(11)

- ID：C02
- 问题：论文表 2-1 将 X52 写成压缩机冷却水流量
- 本手册采用的表述：冷凝器冷却水操纵量 XMV(11)
- 核对依据与状态：S03 的 XMV(11)；已记录纠正

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

### RN01 · IDV(99)是什么

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "IDV(99)是什么",
  "normalized_query": "IDV(99)是什么",
  "retrieval_query": "IDV(99)是什么",
  "entities": [
    {
      "kind": "fault",
      "number": 99,
      "canonical": "IDV(99)",
      "valid": false,
      "primary_unit": null,
      "raw": "IDV(99)",
      "span": [
        0,
        7
      ]
    }
  ],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [
    "IDV(99) 超出本手册编号范围或区间无效"
  ],
  "reasons": [],
  "context_used": false
}
```

预期证据排名：`{}`。null 表示无正分命中。

### RN02 · 流99是什么

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "流99是什么",
  "normalized_query": "流99是什么",
  "retrieval_query": "流99是什么",
  "entities": [
    {
      "kind": "stream",
      "number": 99,
      "canonical": "流 99",
      "valid": false,
      "primary_unit": null,
      "raw": "流99",
      "span": [
        0,
        3
      ]
    }
  ],
  "quantities": [],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [
    "流99 超出本手册编号范围或区间无效"
  ],
  "reasons": [],
  "context_used": false
}
```

预期证据排名：`{}`。null 表示无正分命中。

### RN03 · 这21个软件都测试过了吗

规则解析：

```json
{
  "parser_version": "1.0.0",
  "original_query": "这21个软件都测试过了吗",
  "normalized_query": "这21个软件都测试过了吗",
  "retrieval_query": "这21个软件都测试过了吗",
  "entities": [],
  "quantities": [
    {
      "text": "21个",
      "number": 21,
      "unit": "个",
      "span": [
        1,
        4
      ]
    }
  ],
  "intent": "general",
  "intent_kinds": [],
  "primary_units": [],
  "ambiguous_number": false,
  "issues": [],
  "reasons": [],
  "context_used": false
}
```

预期证据排名：`{}`。null 表示无正分命中。

#### 第 1 名 · VAR-X21 · 分数 0.1278

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

#### 第 2 名 · FAULT-IDV21 · 分数 0.0516

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

#### 第 3 名 · C04 · 分数 0.0500

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:502)

来源差异 C04：IDV(16)–(20) 为 Unknown；21 按扩展数据说明

- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 4 名 · DATA-FILES · 分数 0.0311

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:279)

6.2 当前项目数据范围

当前已使用正常工况 `d00_te.dat` 和故障 7 的 `d07_te.dat`。本地检查结果均为 960 行、52 列，没有缺失值或无穷值；这只适用于当前两个文件，不代表全部 TEP 数据都没有异常值。

论文实验约定为每 3 分钟记录一次、48 小时测试、8 小时后注入故障；当前项目据此前 160 点为正常段，后续段作故障分析。该约定不能自动推广到其他仿真器、训练文件或重新生成的数据，换文件时需重新核对时间轴和注入点。

本地数据的下载地址、文件哈希及首次检查见 [data/README.md](/Users/rowen/Documents/高校/tep-fault-agent/data/README.md)。这里的故障目录覆盖 21 类，**不代表当前诊断功能已对 21 类逐一验证**。

依据：[S01，§2.4 的实验数据说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S04，文件结构说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)、本项目数据检查记录。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)

#### 第 5 名 · FAULT-IDV04 · 分数 0.0259

[原文位置](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:333)

7.4 IDV(4)：反应器冷却水入口温度变化｜FAULT-IDV04

- **扰动类型：**阶跃。
- **预设注入：**反应器冷却水入口温度改变。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X21 为冷却水出口温度，X51 为冷却水操纵量；X9 为反应器温度。
- **解释边界：**不能把出口温度 X21 当作入口温度的同义字段。
- **来源：**[S03，Process Disturbances 的 IDV(4)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

排序依据：文本匹配；优先级 0；分数仍为文本余弦相似度。

来源：[S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)；[S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)

## 评测边界

- 开发回归集9问，不是独立测试集
- 只评测检索证据，不评测答案正确性或抗注入能力
- 不使用追问历史；Q15保留短问法以暴露该限制
- 相关性标签为人工整理的候选证据，支持进一步复核
- 相似度不是正确概率
