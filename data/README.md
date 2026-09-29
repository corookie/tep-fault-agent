# 本阶段使用的数据

来源：[Braatz 研究组 TEP 仿真数据公开镜像](https://github.com/camaramm/tennessee-eastman-profBraatz)。该仓库说明了数据对应的原始仿真程序、52 个变量的顺序和测试文件格式。只取两个文件用于第一阶段：

| 本地文件 | 含义 | SHA-256 |
| --- | --- | --- |
| `raw/d00_te.dat` | 正常工况测试数据 | `57d56da4199e3d73582855d810be1d13d931386fd728bf1694798c7b0a03678c` |
| `raw/d07_te.dat` | 故障 IDV(7) 测试数据 | `e01b7c81daf9fccc4495cbde5658296918276b3c078044893f6e945dd91d3446` |

原始下载地址分别为：

- https://raw.githubusercontent.com/camaramm/tennessee-eastman-profBraatz/master/d00_te.dat
- https://raw.githubusercontent.com/camaramm/tennessee-eastman-profBraatz/master/d07_te.dat

文件以空白字符分隔，没有表头。每行是一个采样时刻；前 41 列为测量变量 XMEAS(1–41)，后 11 列为操纵变量 XMV(1–11)。在本项目中把它们依次记作 X1–X52，因此 X4 对应第 4 列（Python 列位置为 3），X45 对应第 45 列（Python 列位置为 44）。采样间隔为 3 分钟。论文中使用的测试序列在前 160 个采样点正常运行，之后注入故障；是否与具体文件吻合仍须通过图形和数据检查。

这是一份仿真数据。若后续改用论文原始实验文件，应重新核对来源、变量顺序、采样间隔与故障时刻，不能直接沿用当前结论。

首次检查结果：两个文件都是 960 行 × 52 列，没有缺失值或无穷值。IDV(7) 中，X4 前 160 点均值约 9.348，故障后前 10 点约 8.493，故障后前 160 点却约 9.372；只比较长时段均值会掩盖刚发生的下跌。X45 则从前 160 点均值约 61.248 上升到故障后前 10 点约 69.543。下一阶段需要画时间曲线核对变化过程。
