"""第一步：只检查 TEP 文件结构，不做故障诊断。"""

from pathlib import Path

import numpy as np
import pandas as pd


DATA_DIR = Path(__file__).parent / "data" / "raw"
COLUMNS = [f"X{i}" for i in range(1, 53)]


def load_data(filename: str) -> pd.DataFrame:
    """TEP .dat 文件用空白分隔，原文件没有列名。"""
    frame = pd.read_csv(DATA_DIR / filename, sep=r"\s+", header=None)
    if frame.shape[1] != len(COLUMNS):
        raise ValueError(f"{filename}: 预期 52 列，实际 {frame.shape[1]} 列")
    frame.columns = COLUMNS
    return frame


def describe_data(name: str, frame: pd.DataFrame) -> None:
    numeric = frame.to_numpy(dtype=float)
    print(f"{name}: {frame.shape[0]} 行 × {frame.shape[1]} 列")
    print(f"  缺失值: {frame.isna().sum().sum()}; 非有限值: {(~np.isfinite(numeric)).sum()}")
    print(f"  前四列: {', '.join(frame.columns[:4])}; 最后一列: {frame.columns[-1]}")


if __name__ == "__main__":
    normal = load_data("d00_te.dat")
    fault_7 = load_data("d07_te.dat")
    describe_data("正常工况", normal)
    describe_data("IDV(7)", fault_7)

    # 论文描述故障在前 160 个正常样本之后注入。这里先比较两个时段，
    # 只看观察到的变化，不把均值差直接解释为物理根因。
    print("IDV(7) 关键变量的时段均值：")
    for column in ("X4", "X45"):
        before = fault_7.loc[:159, column].mean()
        immediate = fault_7.loc[160:169, column].mean()
        after = fault_7.loc[160:319, column].mean()
        print(
            f"  {column}: 前 160 点 {before:.3f}；"
            f"故障后前 10 点 {immediate:.3f}；故障后前 160 点 {after:.3f}"
        )
