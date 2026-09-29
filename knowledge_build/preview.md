# TEP 切分结果预览

共 **110 个 chunk**。下方每个编号条目对应 JSONL 中的一条记录。

切分不调用大模型、不改写领域事实；表格行按原表头展开。正文下方保留了继承的单位、边界与来源。

类型统计：适用范围 1、组分与反应 1、工艺总览 1、物料流 11、冷却水回路 2、设备 5、变量约定 1、变量 52、采样与延迟 1、数据范围 1、数据处理说明 1、故障解释约定 1、故障 21、知识边界 1、来源差异 10。

字符数（不是 token）：{'min': 123, 'median': 503, 'max': 1615}。

## 先看三个实际样例

### 样例：X4 / XMEAS(4)：A/C 混合进料总流量；流 4

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

编号：`TEP-KB-001:VAR-X04:v1.0.0:1.0.0`

关联实体：STREAM-04, VAR-X04, X4, XMEAS(4)

来源：S01, S02, S03

### 样例：7.7 IDV(7)：C 进料总管压力损失｜FAULT-IDV07

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

编号：`TEP-KB-001:FAULT-IDV07:v1.0.0:1.0.0`

关联实体：FAULT-IDV07, IDV(7), STREAM-04, X4, X45

来源：S01, S03

### 样例：X22 / XMEAS(22)：分离器冷却水出口温度；对应冷凝冷却系统

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

编号：`TEP-KB-001:VAR-X22:v1.0.0:1.0.0`

关联实体：VAR-X22, X22, XMEAS(22)

来源：S01, S02, S03

## 全部切分结果

### 001 · 1. 适用范围与术语｜SCOPE-001

`TEP-KB-001:SCOPE-001:v1.0.0:1.0.0` · 1070 字符 · scope

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:22) · 原文行 22–29

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，§2.4、表 2-1/2-2
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1、表 3–5/8
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头接口说明
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：S04，File Format / Fault Scenarios

---

### 002 · 2. 组分与反应｜CHEM-001

`TEP-KB-001:CHEM-001:v1.0.0:1.0.0` · 997 字符 · chemistry

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:33) · 原文行 33–61

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，§2.4 反应式与组分描述
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，pp.245、247

---

### 003 · 3.1 从原料到产品，以及两条返回路径

`TEP-KB-001:PROC-001:v1.0.0:1.0.0` · 1100 字符 · process_overview

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:67) · 原文行 67–78

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、§2.4
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1、p.247
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 004 · TEP 流股 1：A 原料边界 → 进料混合处

`TEP-KB-001:STREAM-01:v1.0.0:1.0.0` · 614 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:108) · 原文行 108–108

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 005 · TEP 流股 2：D 原料边界 → 进料混合处

`TEP-KB-001:STREAM-02:v1.0.0:1.0.0` · 614 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:109) · 原文行 109–109

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 006 · TEP 流股 3：E 原料边界 → 进料混合处

`TEP-KB-001:STREAM-03:v1.0.0:1.0.0` · 614 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:110) · 原文行 110–110

TEP 流股 3：E 原料边界 → 进料混合处

- 稳定 ID：STREAM-03
- 图中编号：3
- 上游 → 下游：E 原料边界 → 进料混合处
- 物料及作用：E 新鲜进料
- 本项目直接相关测量：X3 流量

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 007 · TEP 流股 4：A/C 原料边界 → 汽提塔

`TEP-KB-001:STREAM-04:v1.0.0:1.0.0` · 648 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:111) · 原文行 111–111

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 008 · TEP 流股 5：汽提塔顶 → 进料混合处

`TEP-KB-001:STREAM-05:v1.0.0:1.0.0` · 614 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:112) · 原文行 112–112

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 009 · TEP 流股 6：进料混合处 → 反应器

`TEP-KB-001:STREAM-06:v1.0.0:1.0.0` · 634 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:113) · 原文行 113–113

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 010 · TEP 流股 7：反应器 → 冷凝器 → 分离器

`TEP-KB-001:STREAM-07:v1.0.0:1.0.0` · 633 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:114) · 原文行 114–114

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 011 · TEP 流股 8：分离器气相经压缩机循环支路 → 进料混合处

`TEP-KB-001:STREAM-08:v1.0.0:1.0.0` · 626 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:115) · 原文行 115–115

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 012 · TEP 流股 9：分离器气相排放支路 → 系统外

`TEP-KB-001:STREAM-09:v1.0.0:1.0.0` · 632 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:116) · 原文行 116–116

TEP 流股 9：分离器气相排放支路 → 系统外

- 稳定 ID：STREAM-09
- 图中编号：9
- 上游 → 下游：分离器气相排放支路 → 系统外
- 物料及作用：排放气体
- 本项目直接相关测量：X10 流量；X29–X36 的 A–H 组分

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 013 · TEP 流股 10：分离器液相 → 汽提塔

`TEP-KB-001:STREAM-10:v1.0.0:1.0.0` · 617 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:117) · 原文行 117–117

TEP 流股 10：分离器液相 → 汽提塔

- 稳定 ID：STREAM-10
- 图中编号：10
- 上游 → 下游：分离器液相 → 汽提塔
- 物料及作用：冷凝液及其中残余组分
- 本项目直接相关测量：X14 体积流量

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 014 · TEP 流股 11：汽提塔底 → 基准边界外

`TEP-KB-001:STREAM-11:v1.0.0:1.0.0` · 638 字符 · stream

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:118) · 原文行 118–118

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 015 · TEP 流股 12：冷却水公用工程 ↔ 反应器冷却束

`TEP-KB-001:UTILITY-12:v1.0.0:1.0.0` · 638 字符 · utility

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:119) · 原文行 119–119

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 016 · TEP 流股 13：冷却水公用工程 ↔ 冷凝器

`TEP-KB-001:UTILITY-13:v1.0.0:1.0.0` · 633 字符 · utility

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:120) · 原文行 120–120

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，测量/操纵变量声明
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 017 · 4.1 反应器｜EQUIP-REACTOR

`TEP-KB-001:EQUIP-REACTOR:v1.0.0:1.0.0` · 690 字符 · equipment

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:130) · 原文行 130–138

4.1 反应器｜EQUIP-REACTOR

**功能与边界。**反应器是发生四条反应的设备，接收混合进料流 6，经流 7 向冷凝器排出物料。进料侧同时受到新鲜原料和循环物料的影响；仅看一条新鲜进料无法完整描述反应器入口组成。

**换热与内部操作。**反应放热，内部冷却束负责移热，搅拌器是原始模型的另一操纵对象。冷却水和反应物料隔着换热面交换热量，不能把冷却水入口当作进入反应器参与反应的进料。

**记录字段。**X6 为流 6 总流量；X7、X8、X9 分别是反应器压力、液位、温度。X21 是反应器冷却水出口温度；X51 是冷却水操纵通道。X23–X28 是入口流 6 的组分分析，并非反应器内部液相组分。搅拌器转速不在本项目 52 列中。

**与故障表的连接。**IDV(4)/(11) 改变冷却水入口温度，IDV(14) 对应冷却水阀粘滞，IDV(13) 改变反应动力学。这些物理位置相近但扰动类型不同；不能合并成“X9 温度故障”。

依据：[S01，§2.4、图 2.3、表 2-1/2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量及扰动声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，§2.4、图 2.3、表 2-1/2-2
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，p.247
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，变量及扰动声明

---

### 018 · 4.2 冷凝器｜EQUIP-CONDENSER

`TEP-KB-001:EQUIP-CONDENSER:v1.0.0:1.0.0` · 868 字符 · equipment

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:142) · 原文行 142–148

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1、表 4
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，XMEAS(22)、XMV(11)、IDV(5)/(12)/(15)

---

### 019 · 4.3 汽液分离器｜EQUIP-SEPARATOR

`TEP-KB-001:EQUIP-SEPARATOR:v1.0.0:1.0.0` · 553 字符 · equipment

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:152) · 原文行 152–158

4.3 汽液分离器｜EQUIP-SEPARATOR

**功能与边界。**接收冷凝后的反应器出料，形成气相和液相出口。气相进入循环与排放两条支路；液相流 10 进入汽提塔。分离器中有液体存量，因此液位与液相流出量是两个不同量。

**记录字段。**X11 温度、X12 液位、X13 压力描述分离器状态，X14 记录流 10 流量，X48 是该液体排出操纵通道。流 9 的排放量是 X10，操纵通道是 X47，气体组分是 X29–X36。

**作用说明。**气相循环回收物料；气相排放为惰性组分和副产物等提供排出通道。分离器不是 G/H 的最终精制设备；流 10 还需进入汽提塔，不能称作最终产品。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，p.247
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，变量声明

---

### 020 · 4.4 循环压缩机｜EQUIP-COMPRESSOR

`TEP-KB-001:EQUIP-COMPRESSOR:v1.0.0:1.0.0` · 537 字符 · equipment

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:162) · 原文行 162–168

4.4 循环压缩机｜EQUIP-COMPRESSOR

**功能与边界。**循环压缩机处理分离器未凝气相循环支路，使循环物流经流 8 返回进料侧。经典图中还画有压缩机旁路/回流阀，因此“压缩机循环阀”不能简单画成串在流 8 上的普通进料阀。

**记录字段。**X5 是流 8 循环流量，X20 是压缩机功率，X46 = XMV(5) 是压缩机循环阀操纵量。功率单位 kW，既不是压力，也不是累计耗电量 kWh。

**知识边界。**这些变量说明部件、测点和执行通道关系，不能据此预先规定 X46 增加时所有工况下 X5 都按同一方向变化。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，XMEAS(5)/(20)、XMV(5)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，XMEAS(5)/(20)、XMV(5)

---

### 021 · 4.5 汽提塔｜EQUIP-STRIPPER

`TEP-KB-001:EQUIP-STRIPPER:v1.0.0:1.0.0` · 643 字符 · equipment

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:172) · 原文行 172–180

4.5 汽提塔｜EQUIP-STRIPPER

**功能与边界。**汽提塔接收分离器液相流 10，并使用流 4 的新鲜进料对其中残余反应物进行汽提。塔顶流 5 返回进料混合处，塔底流 11 输出产品混合物。流 4 虽常简称 C 进料，但其组分定义包含 A/C 混合物及 B。

**供热与产品。**汽提塔配置蒸汽供热及冷凝水侧。蒸汽是供热介质，不能与工艺产品物流合并。塔底产品含 G/H，后续把它们分离的精制系统不在 TE 基准内。

**记录字段。**X15、X16、X18 为塔液位、压力、温度；X17 为塔底流 11 的流量；X19 为蒸汽流量。X49 控制塔底产品排出，X50 为蒸汽阀操纵量。X37–X41 记录流 11 中 D/E/F/G/H 的摩尔百分数。

**常见混淆。**X22 不属于汽提塔；流 5 不是冷凝水；X37–X41 也不是“反应器组分”。

依据：[S01，图 2.3、表 2-1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S02，p.247、图 1](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)、[S03，变量声明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，图 2.3、表 2-1
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，p.247、图 1
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，变量声明

---

### 022 · 5. 完整变量字典｜VARS-001

`TEP-KB-001:VARS-001:v1.0.0:1.0.0` · 684 字符 · variable_conventions

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:184) · 原文行 184–188

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 023 · X1 / XMEAS(1)：A 进料流量；流 1

`TEP-KB-001:VAR-X01:v1.0.0:1.0.0` · 440 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:194) · 原文行 194–194

X1 / XMEAS(1)：A 进料流量；流 1

- 条目 ID：VAR-X01
- 项目字段：X1
- 原始标识：XMEAS(1)
- 含义与测点：A 进料流量；流 1
- 单位：kscmh

【继承的限定与来源】
【单位与来源】
kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 024 · X2 / XMEAS(2)：D 进料流量；流 2

`TEP-KB-001:VAR-X02:v1.0.0:1.0.0` · 462 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:195) · 原文行 195–195

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 025 · X3 / XMEAS(3)：E 进料流量；流 3

`TEP-KB-001:VAR-X03:v1.0.0:1.0.0` · 462 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:196) · 原文行 196–196

X3 / XMEAS(3)：E 进料流量；流 3

- 条目 ID：VAR-X03
- 项目字段：X3
- 原始标识：XMEAS(3)
- 含义与测点：E 进料流量；流 3
- 单位：kg/h

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 026 · X4 / XMEAS(4)：A/C 混合进料总流量；流 4

`TEP-KB-001:VAR-X04:v1.0.0:1.0.0` · 450 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:197) · 原文行 197–197

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 027 · X5 / XMEAS(5)：循环气流量；流 8

`TEP-KB-001:VAR-X05:v1.0.0:1.0.0` · 438 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:198) · 原文行 198–198

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 028 · X6 / XMEAS(6)：反应器总进料流量；流 6

`TEP-KB-001:VAR-X06:v1.0.0:1.0.0` · 444 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:199) · 原文行 199–199

X6 / XMEAS(6)：反应器总进料流量；流 6

- 条目 ID：VAR-X06
- 项目字段：X6
- 原始标识：XMEAS(6)
- 含义与测点：反应器总进料流量；流 6
- 单位：kscmh

【继承的限定与来源】
【单位与来源】
kscmh 表示千标准立方米/小时；本手册未补造“标准状态”的温压定义。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 029 · X7 / XMEAS(7)：反应器压力

`TEP-KB-001:VAR-X07:v1.0.0:1.0.0` · 406 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:200) · 原文行 200–200

X7 / XMEAS(7)：反应器压力

- 条目 ID：VAR-X07
- 项目字段：X7
- 原始标识：XMEAS(7)
- 含义与测点：反应器压力
- 单位：kPa(g)

【继承的限定与来源】
【单位与来源】
kPa(g) 为表压。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 030 · X8 / XMEAS(8)：反应器液位

`TEP-KB-001:VAR-X08:v1.0.0:1.0.0` · 418 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:201) · 原文行 201–201

X8 / XMEAS(8)：反应器液位

- 条目 ID：VAR-X08
- 项目字段：X8
- 原始标识：XMEAS(8)
- 含义与测点：反应器液位
- 单位：%

【继承的限定与来源】
【单位与来源】
液位 % 是模型的液位标度，不保证等于容器总体积百分比。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 031 · X9 / XMEAS(9)：反应器温度

`TEP-KB-001:VAR-X09:v1.0.0:1.0.0` · 381 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:202) · 原文行 202–202

X9 / XMEAS(9)：反应器温度

- 条目 ID：VAR-X09
- 项目字段：X9
- 原始标识：XMEAS(9)
- 含义与测点：反应器温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 032 · X10 / XMEAS(10)：排放流量；流 9

`TEP-KB-001:VAR-X10:v1.0.0:1.0.0` · 440 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:203) · 原文行 203–203

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 033 · X11 / XMEAS(11)：汽液分离器温度

`TEP-KB-001:VAR-X11:v1.0.0:1.0.0` · 389 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:204) · 原文行 204–204

X11 / XMEAS(11)：汽液分离器温度

- 条目 ID：VAR-X11
- 项目字段：X11
- 原始标识：XMEAS(11)
- 含义与测点：汽液分离器温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 034 · X12 / XMEAS(12)：汽液分离器液位

`TEP-KB-001:VAR-X12:v1.0.0:1.0.0` · 426 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:205) · 原文行 205–205

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 035 · X13 / XMEAS(13)：汽液分离器压力

`TEP-KB-001:VAR-X13:v1.0.0:1.0.0` · 414 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:206) · 原文行 206–206

X13 / XMEAS(13)：汽液分离器压力

- 条目 ID：VAR-X13
- 项目字段：X13
- 原始标识：XMEAS(13)
- 含义与测点：汽液分离器压力
- 单位：kPa(g)

【继承的限定与来源】
【单位与来源】
kPa(g) 为表压。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 036 · X14 / XMEAS(14)：分离器液相出口流量；流 10

`TEP-KB-001:VAR-X14:v1.0.0:1.0.0` · 474 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:207) · 原文行 207–207

X14 / XMEAS(14)：分离器液相出口流量；流 10

- 条目 ID：VAR-X14
- 项目字段：X14
- 原始标识：XMEAS(14)
- 含义与测点：分离器液相出口流量；流 10
- 单位：m³/h

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 037 · X15 / XMEAS(15)：汽提塔液位

`TEP-KB-001:VAR-X15:v1.0.0:1.0.0` · 422 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:208) · 原文行 208–208

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 038 · X16 / XMEAS(16)：汽提塔压力

`TEP-KB-001:VAR-X16:v1.0.0:1.0.0` · 410 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:209) · 原文行 209–209

X16 / XMEAS(16)：汽提塔压力

- 条目 ID：VAR-X16
- 项目字段：X16
- 原始标识：XMEAS(16)
- 含义与测点：汽提塔压力
- 单位：kPa(g)

【继承的限定与来源】
【单位与来源】
kPa(g) 为表压。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 039 · X17 / XMEAS(17)：汽提塔底产品流量；流 11

`TEP-KB-001:VAR-X17:v1.0.0:1.0.0` · 472 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:210) · 原文行 210–210

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 040 · X18 / XMEAS(18)：汽提塔温度

`TEP-KB-001:VAR-X18:v1.0.0:1.0.0` · 385 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:211) · 原文行 211–211

X18 / XMEAS(18)：汽提塔温度

- 条目 ID：VAR-X18
- 项目字段：X18
- 原始标识：XMEAS(18)
- 含义与测点：汽提塔温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 041 · X19 / XMEAS(19)：汽提塔蒸汽流量

`TEP-KB-001:VAR-X19:v1.0.0:1.0.0` · 460 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:212) · 原文行 212–212

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 042 · X20 / XMEAS(20)：压缩机功率

`TEP-KB-001:VAR-X20:v1.0.0:1.0.0` · 385 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:213) · 原文行 213–213

X20 / XMEAS(20)：压缩机功率

- 条目 ID：VAR-X20
- 项目字段：X20
- 原始标识：XMEAS(20)
- 含义与测点：压缩机功率
- 单位：kW

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 043 · X21 / XMEAS(21)：反应器冷却水出口温度

`TEP-KB-001:VAR-X21:v1.0.0:1.0.0` · 395 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:214) · 原文行 214–214

X21 / XMEAS(21)：反应器冷却水出口温度

- 条目 ID：VAR-X21
- 项目字段：X21
- 原始标识：XMEAS(21)
- 含义与测点：反应器冷却水出口温度
- 单位：°C

【继承的限定与来源】
【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 044 · X22 / XMEAS(22)：分离器冷却水出口温度；对应冷凝冷却系统

`TEP-KB-001:VAR-X22:v1.0.0:1.0.0` · 535 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:215) · 原文行 215–215

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 045 · X23 / XMEAS(23)：反应器进料中 A；流 6

`TEP-KB-001:VAR-X23:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:223) · 原文行 223–223

X23 / XMEAS(23)：反应器进料中 A；流 6

- 条目 ID：VAR-X23
- 项目字段：X23
- 原始标识：XMEAS(23)
- 含义与测点：反应器进料中 A；流 6
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 046 · X24 / XMEAS(24)：反应器进料中 B；流 6

`TEP-KB-001:VAR-X24:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:224) · 原文行 224–224

X24 / XMEAS(24)：反应器进料中 B；流 6

- 条目 ID：VAR-X24
- 项目字段：X24
- 原始标识：XMEAS(24)
- 含义与测点：反应器进料中 B；流 6
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 047 · X25 / XMEAS(25)：反应器进料中 C；流 6

`TEP-KB-001:VAR-X25:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:225) · 原文行 225–225

X25 / XMEAS(25)：反应器进料中 C；流 6

- 条目 ID：VAR-X25
- 项目字段：X25
- 原始标识：XMEAS(25)
- 含义与测点：反应器进料中 C；流 6
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 048 · X26 / XMEAS(26)：反应器进料中 D；流 6

`TEP-KB-001:VAR-X26:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:226) · 原文行 226–226

X26 / XMEAS(26)：反应器进料中 D；流 6

- 条目 ID：VAR-X26
- 项目字段：X26
- 原始标识：XMEAS(26)
- 含义与测点：反应器进料中 D；流 6
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 049 · X27 / XMEAS(27)：反应器进料中 E；流 6

`TEP-KB-001:VAR-X27:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:227) · 原文行 227–227

X27 / XMEAS(27)：反应器进料中 E；流 6

- 条目 ID：VAR-X27
- 项目字段：X27
- 原始标识：XMEAS(27)
- 含义与测点：反应器进料中 E；流 6
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 050 · X28 / XMEAS(28)：反应器进料中 F；流 6

`TEP-KB-001:VAR-X28:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:228) · 原文行 228–228

X28 / XMEAS(28)：反应器进料中 F；流 6

- 条目 ID：VAR-X28
- 项目字段：X28
- 原始标识：XMEAS(28)
- 含义与测点：反应器进料中 F；流 6
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 051 · X29 / XMEAS(29)：排放气中 A；流 9

`TEP-KB-001:VAR-X29:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:229) · 原文行 229–229

X29 / XMEAS(29)：排放气中 A；流 9

- 条目 ID：VAR-X29
- 项目字段：X29
- 原始标识：XMEAS(29)
- 含义与测点：排放气中 A；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 052 · X30 / XMEAS(30)：排放气中 B；流 9

`TEP-KB-001:VAR-X30:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:230) · 原文行 230–230

X30 / XMEAS(30)：排放气中 B；流 9

- 条目 ID：VAR-X30
- 项目字段：X30
- 原始标识：XMEAS(30)
- 含义与测点：排放气中 B；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 053 · X31 / XMEAS(31)：排放气中 C；流 9

`TEP-KB-001:VAR-X31:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:231) · 原文行 231–231

X31 / XMEAS(31)：排放气中 C；流 9

- 条目 ID：VAR-X31
- 项目字段：X31
- 原始标识：XMEAS(31)
- 含义与测点：排放气中 C；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 054 · X32 / XMEAS(32)：排放气中 D；流 9

`TEP-KB-001:VAR-X32:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:232) · 原文行 232–232

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 055 · X33 / XMEAS(33)：排放气中 E；流 9

`TEP-KB-001:VAR-X33:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:233) · 原文行 233–233

X33 / XMEAS(33)：排放气中 E；流 9

- 条目 ID：VAR-X33
- 项目字段：X33
- 原始标识：XMEAS(33)
- 含义与测点：排放气中 E；流 9
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 056 · X34 / XMEAS(34)：排放气中 F；流 9

`TEP-KB-001:VAR-X34:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:234) · 原文行 234–234

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 057 · X35 / XMEAS(35)：排放气中 G；流 9

`TEP-KB-001:VAR-X35:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:235) · 原文行 235–235

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 058 · X36 / XMEAS(36)：排放气中 H；流 9

`TEP-KB-001:VAR-X36:v1.0.0:1.0.0` · 497 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:236) · 原文行 236–236

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 059 · X37 / XMEAS(37)：塔底产品中 D；流 11

`TEP-KB-001:VAR-X37:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:237) · 原文行 237–237

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 060 · X38 / XMEAS(38)：塔底产品中 E；流 11

`TEP-KB-001:VAR-X38:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:238) · 原文行 238–238

X38 / XMEAS(38)：塔底产品中 E；流 11

- 条目 ID：VAR-X38
- 项目字段：X38
- 原始标识：XMEAS(38)
- 含义与测点：塔底产品中 E；流 11
- 单位：mol%

【继承的限定与来源】
【单位与来源】
mol% 为摩尔百分数，不能当作质量百分数。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
同一组分在不同流股中有不同变量。例如 X24 与 X30 都测 B，前者在流 6，后者在流 9；它们不是可互换的别名。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 061 · X39 / XMEAS(39)：塔底产品中 F；流 11

`TEP-KB-001:VAR-X39:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:239) · 原文行 239–239

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 062 · X40 / XMEAS(40)：塔底产品中 G；流 11

`TEP-KB-001:VAR-X40:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:240) · 原文行 240–240

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 063 · X41 / XMEAS(41)：塔底产品中 H；流 11

`TEP-KB-001:VAR-X41:v1.0.0:1.0.0` · 501 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:241) · 原文行 241–241

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 064 · X42 / XMV(1)：D 进料操纵量；流 2

`TEP-KB-001:VAR-X42:v1.0.0:1.0.0` · 656 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:247) · 原文行 247–247

X42 / XMV(1)：D 进料操纵量；流 2

- 条目 ID：VAR-X42
- 项目字段：X42
- 原始标识：XMV(1)
- 含义与作用对象：D 进料操纵量；流 2
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 065 · X43 / XMV(2)：E 进料操纵量；流 3

`TEP-KB-001:VAR-X43:v1.0.0:1.0.0` · 656 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:248) · 原文行 248–248

X43 / XMV(2)：E 进料操纵量；流 3

- 条目 ID：VAR-X43
- 项目字段：X43
- 原始标识：XMV(2)
- 含义与作用对象：E 进料操纵量；流 3
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 066 · X44 / XMV(3)：A 进料操纵量；流 1

`TEP-KB-001:VAR-X44:v1.0.0:1.0.0` · 656 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:249) · 原文行 249–249

X44 / XMV(3)：A 进料操纵量；流 1

- 条目 ID：VAR-X44
- 项目字段：X44
- 原始标识：XMV(3)
- 含义与作用对象：A 进料操纵量；流 1
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 067 · X45 / XMV(4)：A/C 进料操纵量；流 4

`TEP-KB-001:VAR-X45:v1.0.0:1.0.0` · 660 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:250) · 原文行 250–250

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 068 · X46 / XMV(5)：压缩机循环／旁路阀操纵量

`TEP-KB-001:VAR-X46:v1.0.0:1.0.0` · 658 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:251) · 原文行 251–251

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 069 · X47 / XMV(6)：排放阀操纵量；流 9

`TEP-KB-001:VAR-X47:v1.0.0:1.0.0` · 654 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:252) · 原文行 252–252

X47 / XMV(6)：排放阀操纵量；流 9

- 条目 ID：VAR-X47
- 项目字段：X47
- 原始标识：XMV(6)
- 含义与作用对象：排放阀操纵量；流 9
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 070 · X48 / XMV(7)：分离器液相排出操纵量；流 10

`TEP-KB-001:VAR-X48:v1.0.0:1.0.0` · 664 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:253) · 原文行 253–253

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 071 · X49 / XMV(8)：汽提塔底产品排出操纵量；流 11

`TEP-KB-001:VAR-X49:v1.0.0:1.0.0` · 666 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:254) · 原文行 254–254

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 072 · X50 / XMV(9)：汽提塔蒸汽阀操纵量

`TEP-KB-001:VAR-X50:v1.0.0:1.0.0` · 652 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:255) · 原文行 255–255

X50 / XMV(9)：汽提塔蒸汽阀操纵量

- 条目 ID：VAR-X50
- 项目字段：X50
- 原始标识：XMV(9)
- 含义与作用对象：汽提塔蒸汽阀操纵量
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 073 · X51 / XMV(10)：反应器冷却水操纵量

`TEP-KB-001:VAR-X51:v1.0.0:1.0.0` · 654 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:256) · 原文行 256–256

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 074 · X52 / XMV(11)：冷凝器冷却水操纵量

`TEP-KB-001:VAR-X52:v1.0.0:1.0.0` · 762 字符 · variable

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:257) · 原文行 257–257

X52 / XMV(11)：冷凝器冷却水操纵量

- 条目 ID：VAR-X52
- 项目字段：X52
- 原始标识：XMV(11)
- 含义与作用对象：冷凝器冷却水操纵量
- 单位：%（归一化设置）

【继承的限定与来源】
【单位与来源】
操纵量 % 是 XMV 的归一化设置，不能直接按 m³/h 或 kg/h 解释；也不代表独立传感器测得的真实阀芯位置。

【单位与来源】
变量表来源：[S01，表 2-1，印刷页 22](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)与 [S03，文件头三个变量区段](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；XMV 归一化定义核对 [S02，表 3 下方说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)。

【本节限定】
原始模型允许传入超出 0–100 的 XMV 值，但内部作用值会被约束。因此 0–100 是规定的操纵范围，不能仅凭文件中某个原始 XMV 超界就断言文件损坏；应核对生成器是否输出了限幅前的命令。[S02，表 3 说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s02)

【来源差异处理】
- ID：C02
- 问题：论文表 2-1 将 X52 写成压缩机冷却水流量
- 本手册采用的表述：冷凝器冷却水操纵量 XMV(11)
- 核对依据与状态：S03 的 XMV(11)；已记录纠正

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明；S02，表 3 说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段

---

### 075 · 6.1 文件记录间隔与分析仪延迟

`TEP-KB-001:DATA-TIMING:v1.0.0:1.0.0` · 830 字符 · sampling

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:265) · 原文行 265–275

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

来源元数据：

- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Sampled Process Measurements
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：S04，File Format

---

### 076 · 6.2 当前项目数据范围

`TEP-KB-001:DATA-FILES:v1.0.0:1.0.0` · 553 字符 · dataset_scope

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:279) · 原文行 279–285

6.2 当前项目数据范围

当前已使用正常工况 `d00_te.dat` 和故障 7 的 `d07_te.dat`。本地检查结果均为 960 行、52 列，没有缺失值或无穷值；这只适用于当前两个文件，不代表全部 TEP 数据都没有异常值。

论文实验约定为每 3 分钟记录一次、48 小时测试、8 小时后注入故障；当前项目据此前 160 点为正常段，后续段作故障分析。该约定不能自动推广到其他仿真器、训练文件或重新生成的数据，换文件时需重新核对时间轴和注入点。

本地数据的下载地址、文件哈希及首次检查见 [data/README.md](/Users/rowen/Documents/高校/tep-fault-agent/data/README.md)。这里的故障目录覆盖 21 类，**不代表当前诊断功能已对 21 类逐一验证**。

依据：[S01，§2.4 的实验数据说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S04，文件结构说明](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)、本项目数据检查记录。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，§2.4 的实验数据说明
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：S04，文件结构说明

---

### 077 · 6.3 数据清洗时不要误删的现象｜DATA-002

`TEP-KB-001:DATA-002:v1.0.0:1.0.0` · 1615 字符 · editorial_guidance

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:289) · 原文行 289–296

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-1，印刷页 22
- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：S02，表 3 下方说明
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，文件头三个变量区段；S03，Sampled Process Measurements
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：S04，File Format

---

### 078 · 7. 预设故障目录与可观测边界｜FAULTS-001

`TEP-KB-001:FAULTS-001:v1.0.0:1.0.0` · 588 字符 · fault_conventions

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:300) · 原文行 300–302

7. 预设故障目录与可观测边界｜FAULTS-001

本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

IDV(1)–(20) 的定义依据 [S01 表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)、[S03 Process Disturbances](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)，按原始代码纠正流股编号；IDV(21) 单独依据 [S04 Fault Scenarios](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s04)。每条保留完整限定，便于后续独立切片。

【继承的限定与来源】
【来源差异处理】
- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01 表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03 Process Disturbances
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：S04 Fault Scenarios

---

### 079 · 7.1 IDV(1)：流 4 的 A/C 比例变化｜FAULT-IDV01

`TEP-KB-001:FAULT-IDV01:v1.0.0:1.0.0` · 524 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:306) · 原文行 306–311

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(1)

---

### 080 · 7.2 IDV(2)：流 4 的 B 组分变化｜FAULT-IDV02

`TEP-KB-001:FAULT-IDV02:v1.0.0:1.0.0` · 517 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:315) · 原文行 315–320

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(2)

---

### 081 · 7.3 IDV(3)：D 进料温度变化｜FAULT-IDV03

`TEP-KB-001:FAULT-IDV03:v1.0.0:1.0.0` · 609 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:324) · 原文行 324–329

7.3 IDV(3)：D 进料温度变化｜FAULT-IDV03

- **扰动类型：**阶跃。
- **预设注入：**流 2 的 D 进料温度改变。
- **可观测性：**无直接记录：流 2 温度不在 52 列中。
- **关联字段：**X2 是流 2 流量，X42 是 D 进料操纵量。
- **解释边界：**X2 测流量，不测温度；此处是流 2。
- **来源：**[S03，Process Disturbances 的 IDV(3)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C05
- 问题：Ricker 网页将 IDV(3) 一处写成 stream 3
- 本手册采用的表述：D 进料温度，流 2
- 核对依据与状态：S03 的 IDV(3)、S01 表 2-2；保留网页错误记录

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(3)

---

### 082 · 7.4 IDV(4)：反应器冷却水入口温度变化｜FAULT-IDV04

`TEP-KB-001:FAULT-IDV04:v1.0.0:1.0.0` · 504 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:333) · 原文行 333–338

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(4)

---

### 083 · 7.5 IDV(5)：冷凝器冷却水入口温度变化｜FAULT-IDV05

`TEP-KB-001:FAULT-IDV05:v1.0.0:1.0.0` · 501 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:342) · 原文行 342–347

7.5 IDV(5)：冷凝器冷却水入口温度变化｜FAULT-IDV05

- **扰动类型：**阶跃。
- **预设注入：**冷凝器冷却水入口温度改变。
- **可观测性：**无直接记录：入口温度不在 52 列中。
- **关联字段：**X22 为相应冷却水出口温度，X52 为冷却水操纵量；X11 为分离器温度。
- **解释边界：**本故障是入口温度扰动，不是阀门粘滞。
- **来源：**[S03，Process Disturbances 的 IDV(5)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(5)

---

### 084 · 7.6 IDV(6)：A 进料损失｜FAULT-IDV06

`TEP-KB-001:FAULT-IDV06:v1.0.0:1.0.0` · 485 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:351) · 原文行 351–356

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(6)

---

### 085 · 7.7 IDV(7)：C 进料总管压力损失｜FAULT-IDV07

`TEP-KB-001:FAULT-IDV07:v1.0.0:1.0.0` · 506 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:360) · 原文行 360–365

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(7)

---

### 086 · 7.8 IDV(8)：流 4 的 A/B/C 组分随机变化｜FAULT-IDV08

`TEP-KB-001:FAULT-IDV08:v1.0.0:1.0.0` · 513 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:369) · 原文行 369–374

7.8 IDV(8)：流 4 的 A/B/C 组分随机变化｜FAULT-IDV08

- **扰动类型：**随机变化。
- **预设注入：**流 4 的 A、B、C 进料组分发生随机变化。
- **可观测性：**无直接记录：流 4 组分不在 52 列中。
- **关联字段：**X23–X25 为下游流 6 的 A、B、C 组分。
- **解释边界：**不能把随机组分扰动简化为一个固定 X 编号。
- **来源：**[S03，Process Disturbances 的 IDV(8)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(8)

---

### 087 · 7.9 IDV(9)：D 进料温度随机变化｜FAULT-IDV09

`TEP-KB-001:FAULT-IDV09:v1.0.0:1.0.0` · 501 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:378) · 原文行 378–383

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(9)

---

### 088 · 7.10 IDV(10)：C 进料温度随机变化｜FAULT-IDV10

`TEP-KB-001:FAULT-IDV10:v1.0.0:1.0.0` · 644 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:387) · 原文行 387–392

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(10)
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 089 · 7.11 IDV(11)：反应器冷却水入口温度随机变化｜FAULT-IDV11

`TEP-KB-001:FAULT-IDV11:v1.0.0:1.0.0` · 506 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:396) · 原文行 396–401

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(11)

---

### 090 · 7.12 IDV(12)：冷凝器冷却水入口温度随机变化｜FAULT-IDV12

`TEP-KB-001:FAULT-IDV12:v1.0.0:1.0.0` · 506 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:405) · 原文行 405–410

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(12)

---

### 091 · 7.13 IDV(13)：反应动力学漂移｜FAULT-IDV13

`TEP-KB-001:FAULT-IDV13:v1.0.0:1.0.0` · 500 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:414) · 原文行 414–419

7.13 IDV(13)：反应动力学漂移｜FAULT-IDV13

- **扰动类型：**缓慢漂移。
- **预设注入：**反应动力学发生缓慢变化。
- **可观测性：**无直接记录：动力学参数不在 52 列中。
- **关联字段：**可按反应器及组分分析字段组织后续诊断，但没有预设单一根源列。
- **解释边界：**本目录不补造具体反应速率常数、变化幅度或传播路径。
- **来源：**[S03，Process Disturbances 的 IDV(13)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(13)

---

### 092 · 7.14 IDV(14)：反应器冷却水阀门粘滞｜FAULT-IDV14

`TEP-KB-001:FAULT-IDV14:v1.0.0:1.0.0` · 503 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:423) · 原文行 423–428

7.14 IDV(14)：反应器冷却水阀门粘滞｜FAULT-IDV14

- **扰动类型：**阀门粘滞。
- **预设注入：**反应器冷却水阀门出现粘滞。
- **可观测性：**X51 = XMV(10) 是对应操纵通道；并非另有一个实际阀位测量。
- **关联字段：**X21 为冷却水出口温度，X9 为反应器温度。
- **解释边界：**命令变化不证明实际阀门已经跟随。
- **来源：**[S03，Process Disturbances 的 IDV(14)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(14)

---

### 093 · 7.15 IDV(15)：冷凝器冷却水阀门粘滞｜FAULT-IDV15

`TEP-KB-001:FAULT-IDV15:v1.0.0:1.0.0` · 507 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:432) · 原文行 432–437

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(15)

---

### 094 · 7.16 IDV(16)：未公开定义的预设故障 16｜FAULT-IDV16

`TEP-KB-001:FAULT-IDV16:v1.0.0:1.0.0` · 674 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:441) · 原文行 441–446

7.16 IDV(16)：未公开定义的预设故障 16｜FAULT-IDV16

- **扰动类型：**Unknown。
- **预设注入：**原始故障清单将本项标为 Unknown；本版本没有经核实的具体物理定义。
- **可观测性：**无法建立已确认的注入量—X 字段映射。
- **关联字段：**保留故障编号供检索和实验索引；不指定根源 X。
- **解释边界：**未知定义不表示没有故障，也不表示算法不能分析；推测必须作为实验结论另行保存。
- **来源：**[S03，Process Disturbances 的 IDV(16)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(16)
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 095 · 7.17 IDV(17)：未公开定义的预设故障 17｜FAULT-IDV17

`TEP-KB-001:FAULT-IDV17:v1.0.0:1.0.0` · 674 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:450) · 原文行 450–455

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(17)
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 096 · 7.18 IDV(18)：未公开定义的预设故障 18｜FAULT-IDV18

`TEP-KB-001:FAULT-IDV18:v1.0.0:1.0.0` · 674 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:459) · 原文行 459–464

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(18)
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 097 · 7.19 IDV(19)：未公开定义的预设故障 19｜FAULT-IDV19

`TEP-KB-001:FAULT-IDV19:v1.0.0:1.0.0` · 674 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:468) · 原文行 468–473

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(19)
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 098 · 7.20 IDV(20)：未公开定义的预设故障 20｜FAULT-IDV20

`TEP-KB-001:FAULT-IDV20:v1.0.0:1.0.0` · 674 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:477) · 原文行 477–482

7.20 IDV(20)：未公开定义的预设故障 20｜FAULT-IDV20

- **扰动类型：**Unknown。
- **预设注入：**原始故障清单将本项标为 Unknown；本版本没有经核实的具体物理定义。
- **可观测性：**无法建立已确认的注入量—X 字段映射。
- **关联字段：**保留故障编号供检索和实验索引；不指定根源 X。
- **解释边界：**未知定义不表示没有故障，也不表示算法不能分析；推测必须作为实验结论另行保存。
- **来源：**[S03，Process Disturbances 的 IDV(20)](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s03)；中文对照 [S01，表 2-2](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md#src-s01)。

【继承的限定与来源】
【故障解释边界】
本节的“故障根源”仅指仿真设定中被改变的物理量或部件。**注入量、测量量、操纵命令、诊断结果四者必须分开。**关联字段用于把描述连到变量字典，不表示这些字段必然异常或按列举顺序传播。

【来源差异处理】
- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：S01，表 2-2
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：S03，Process Disturbances 的 IDV(20)
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 099 · 7.21 IDV(21)：流 4 阀门位置固定｜FAULT-IDV21

`TEP-KB-001:FAULT-IDV21:v1.0.0:1.0.0` · 608 字符 · fault

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:486) · 原文行 486–491

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

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：§2.4; PDF pages 32–35; printed pages 20–23
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：S04，Fault Scenarios 的 d21

---

### 100 · 本知识库的未知项与适用边界

`TEP-KB-001:LIMITS-001:v1.0.0:1.0.0` · 237 字符 · limitations

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:510) · 原文行 510–512

本知识库的未知项与适用边界

**当前保留的未知：**IDV(16)–(20) 的可靠物理解释；当前数据生成器完整控制回路及参数是否与其他公开版本一致；未测入口量的真实时间曲线；全部 21 类诊断结果；各故障的可信动态传播路径。这些内容不能靠语言模型补齐。

**不纳入本版的内容：**各操作模式的全套稳态表、设备尺寸/物性常数、控制器整定和全套停机阈值。它们适合后续仿真或控制问答专题，不能从当前两份样本数据推断。若用户问到，应检索相应原始章节后再建立独立、带版本的条目。

来源元数据：

- 本手册编辑整理的范围或方法说明；通过原文定位追溯，不冒充外部文献结论。

---

### 101 · 来源差异 C01：分离器冷却水出口温度，对应冷凝冷却系统

`TEP-KB-001:C01:v1.0.0:1.0.0` · 141 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:499) · 原文行 499–499

来源差异 C01：分离器冷却水出口温度，对应冷凝冷却系统

- ID：C01
- 问题：论文表 2-1 将 X22 写成汽提塔冷却水出口温度
- 本手册采用的表述：分离器冷却水出口温度，对应冷凝冷却系统
- 核对依据与状态：S03 的 XMEAS(22)，S02 表 4；已记录纠正

来源元数据：

- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：pp.245–250; Figure 1; Tables 3–5,8
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences

---

### 102 · 来源差异 C02：冷凝器冷却水操纵量 XMV(11)

`TEP-KB-001:C02:v1.0.0:1.0.0` · 125 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:500) · 原文行 500–500

来源差异 C02：冷凝器冷却水操纵量 XMV(11)

- ID：C02
- 问题：论文表 2-1 将 X52 写成压缩机冷却水流量
- 本手册采用的表述：冷凝器冷却水操纵量 XMV(11)
- 核对依据与状态：S03 的 XMV(11)；已记录纠正

来源元数据：

- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences

---

### 103 · 来源差异 C03：流 4 进料温度随机变化

`TEP-KB-001:C03:v1.0.0:1.0.0` · 123 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:501) · 原文行 501–501

来源差异 C03：流 4 进料温度随机变化

- ID：C03
- 问题：论文表 2-2 的 IDV(10) 写流 2
- 本手册采用的表述：流 4 进料温度随机变化
- 核对依据与状态：S03 的 IDV(10)，S04 的 d10；已记录纠正

来源元数据：

- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 104 · 来源差异 C04：IDV(16)–(20) 为 Unknown；21 按扩展数据说明

`TEP-KB-001:C04:v1.0.0:1.0.0` · 169 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:502) · 原文行 502–502

来源差异 C04：IDV(16)–(20) 为 Unknown；21 按扩展数据说明

- ID：C04
- 问题：论文正文统称 IDV(16)–(21) 未知，但表中定义了 21
- 本手册采用的表述：IDV(16)–(20) 为 Unknown；21 按扩展数据说明
- 核对依据与状态：S01 表 2-2、S03、S04；按版本拆分

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：§2.4; PDF pages 32–35; printed pages 20–23
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 105 · 来源差异 C05：D 进料温度，流 2

`TEP-KB-001:C05:v1.0.0:1.0.0` · 130 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:503) · 原文行 503–503

来源差异 C05：D 进料温度，流 2

- ID：C05
- 问题：Ricker 网页将 IDV(3) 一处写成 stream 3
- 本手册采用的表述：D 进料温度，流 2
- 核对依据与状态：S03 的 IDV(3)、S01 表 2-2；保留网页错误记录

来源元数据：

- [S01](/Users/rowen/Desktop/rowenList/个人信息/研究生课题和项目/论文/毕业论文余国源-送审版.pdf)：§2.4; PDF pages 32–35; printed pages 20–23
- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences

---

### 106 · 来源差异 C06：B 是惰性组分；催化剂另行描述

`TEP-KB-001:C06:v1.0.0:1.0.0` · 127 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:504) · 原文行 504–504

来源差异 C06：B 是惰性组分；催化剂另行描述

- ID：C06
- 问题：论文反应式箭头上的 B 标注可能被误读为催化剂
- 本手册采用的表述：B 是惰性组分；催化剂另行描述
- 核对依据与状态：S02 pp.245、247；不继承有歧义的箭头标注

来源元数据：

- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：pp.245–250; Figure 1; Tables 3–5,8

---

### 107 · 来源差异 C07：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录

`TEP-KB-001:C07:v1.0.0:1.0.0` · 154 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:505) · 原文行 505–505

来源差异 C07：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录

- ID：C07
- 问题：原模型有 12 个 XMV，数据只有 52 列
- 本手册采用的表述：41 个 XMEAS + 前 11 个 XMV；搅拌器未收录
- 核对依据与状态：S03、S04；数据模式差异，不是缺失一行字典

来源元数据：

- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 108 · 来源差异 C08：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号

`TEP-KB-001:C08:v1.0.0:1.0.0` · 148 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:506) · 原文行 506–506

来源差异 C08：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号

- ID：C08
- 问题：部分修订结构模型将反应器出料编号为 13
- 本手册采用的表述：本文经典图中反应器出料为 7，13 是冷凝冷却水侧编号
- 核对依据与状态：S02 图 1；S06 只作版本差异线索，不混用编号

来源元数据：

- [S02](https://users.abo.fi/~khaggblo/RS/Downs.pdf)：pp.245–250; Figure 1; Tables 3–5,8
- [S06](https://zenodo.org/records/5171645/files/TE_Structural_Model_Vs00.pdf)：Appendix A

---

### 109 · 来源差异 C09：文件每 3 分钟保存，组分分析有 6/15 分钟周期与延迟

`TEP-KB-001:C09:v1.0.0:1.0.0` · 142 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:507) · 原文行 507–507

来源差异 C09：文件每 3 分钟保存，组分分析有 6/15 分钟周期与延迟

- ID：C09
- 问题：“所有测点每 3 分钟采样”的表述过度简化
- 本手册采用的表述：文件每 3 分钟保存，组分分析有 6/15 分钟周期与延迟
- 核对依据与状态：S03、S04；已补充时间语义

来源元数据：

- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences
- [S04](https://github.com/jkitchin/tennessee-eastman-profbraatz/blob/9a6c8e5fcef4a2850778704e7793c87b0a187005/data/README.md)：File Format; Fault Scenarios

---

### 110 · 来源差异 C10：本手册不沿用必须组合运行的限制

`TEP-KB-001:C10:v1.0.0:1.0.0` · 142 字符 · source_correction

[定位手册原文](/Users/rowen/Documents/高校/tep-fault-agent/TEP_SOURCE_MAP.md:508) · 原文行 508–508

来源差异 C10：本手册不沿用必须组合运行的限制

- ID：C10
- 问题：原论文称部分后续扰动需配合其他扰动使用；代码说明已修订
- 本手册采用的表述：本手册不沿用必须组合运行的限制
- 核对依据与状态：S03 文件头 Differences 第 3 项；具体运行仍以生成器为准

来源元数据：

- [S03](https://github.com/camaramm/tennessee-eastman-profBraatz/blob/0643318858ce7c87292bd59820b459e12a13d009/teprob.f)：Header: variable declarations, disturbances and code/paper differences

---
