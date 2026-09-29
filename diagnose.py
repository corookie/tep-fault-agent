"""TEP IDV(7) 的最小核岭回归格兰杰诊断流程。"""

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.stats import binomtest
from sklearn.kernel_ridge import KernelRidge
from sklearn.preprocessing import StandardScaler

from inspect_data import load_data


VARIABLES = ("X4", "X7", "X13", "X16", "X20", "X45", "X46")


def lagged_samples(values: np.ndarray, lag: int) -> tuple[np.ndarray, np.ndarray]:
    """用 t-1 ... t-lag 的全部变量预测 t 时刻的全部变量。"""
    if lag < 1 or len(values) <= lag:
        raise ValueError("时滞必须大于零，样本数必须大于时滞")
    features = np.stack(
        [values[t - lag : t][::-1].reshape(-1) for t in range(lag, len(values))]
    )
    targets = values[lag:]
    return features, targets


def benjamini_hochberg(p_values: list[float]) -> list[float]:
    """同一张变量关系图中，对多次检验做探索性 FDR 校正。"""
    p = np.asarray(p_values)
    order = np.argsort(p)
    adjusted = np.empty(len(p))
    ranked = p[order] * len(p) / np.arange(1, len(p) + 1)
    adjusted[order] = np.minimum.accumulate(ranked[::-1])[::-1].clip(0, 1)
    return adjusted.tolist()


def diagnose(values: np.ndarray, lag: int = 3, alpha: float = 1.0) -> dict:
    if values.ndim != 2 or values.shape[1] != len(VARIABLES):
        raise ValueError(f"输入必须有 {len(VARIABLES)} 列，并按 VARIABLES 顺序排列")
    if not np.isfinite(values).all():
        raise ValueError("数据有缺失值或无穷值；请先检查数据")

    features, targets = lagged_samples(values, lag)
    train_end = int(len(features) * 0.7)
    test_start = train_end + lag  # 留出一个滞后长度的间隔，避免邻近窗口重叠
    if train_end < 10 or len(features) - test_start < 10:
        raise ValueError("训练或测试样本太少；请增加 --samples 或减少 --lag")

    scaler = StandardScaler().fit(features[:train_end])
    train_x = scaler.transform(features[:train_end])
    test_x = scaler.transform(features[test_start:])
    gamma = 1.0 / train_x.shape[1]  # 完整/缺省模型共用同一个 RBF 核宽度
    edges = []

    for target_index, target_name in enumerate(VARIABLES):
        train_y = targets[:train_end, target_index]
        test_y = targets[test_start:, target_index]
        y_mean = train_y.mean()
        y_scale = train_y.std() or 1.0
        train_y = (train_y - y_mean) / y_scale
        test_y = (test_y - y_mean) / y_scale

        full = KernelRidge(alpha=alpha, kernel="rbf", gamma=gamma)
        # 数值库可能在矩阵计算时报告浮点警告；下方仍检查预测是否有限。
        with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
            full.fit(train_x, train_y)
            full_prediction = full.predict(test_x)
        if not np.isfinite(full_prediction).all():
            raise ArithmeticError("完整模型的预测出现非有限值")
        full_error = np.abs(test_y - full_prediction)

        for source_index, source_name in enumerate(VARIABLES):
            if source_index == target_index:
                continue
            # 每个变量都有 lag 个历史位置；去掉源变量的全部历史位置。
            keep = [
                column
                for column in range(train_x.shape[1])
                if column % len(VARIABLES) != source_index
            ]
            restricted = KernelRidge(alpha=alpha, kernel="rbf", gamma=gamma)
            with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
                restricted.fit(train_x[:, keep], train_y)
                restricted_prediction = restricted.predict(test_x[:, keep])
            if not np.isfinite(restricted_prediction).all():
                raise ArithmeticError("缺省模型的预测出现非有限值")
            restricted_error = np.abs(test_y - restricted_prediction)

            improvement = restricted_error - full_error
            nonzero = improvement[np.abs(improvement) > 1e-12]
            positives = int((nonzero > 0).sum())
            p_value = (
                binomtest(positives, len(nonzero), 0.5, alternative="greater").pvalue
                if len(nonzero)
                else 1.0
            )
            edges.append(
                {
                    "source": source_name,
                    "target": target_name,
                    "improvement": float(improvement.mean() / (restricted_error.mean() + 1e-12)),
                    "positive_tests": positives,
                    "test_count": int(len(nonzero)),
                    "p_value": float(p_value),
                }
            )

    for edge, q_value in zip(edges, benjamini_hochberg([e["p_value"] for e in edges])):
        edge["q_value"] = q_value
        edge["selected"] = edge["improvement"] > 0 and q_value < 0.10

    rankings = []
    for variable in VARIABLES:
        outgoing = [e for e in edges if e["source"] == variable and e["selected"]]
        incoming = [e for e in edges if e["target"] == variable and e["selected"]]
        rankings.append(
            {
                "variable": variable,
                "outgoing": len(outgoing),
                "incoming": len(incoming),
                "score": len(outgoing) - len(incoming),
            }
        )
    rankings.sort(key=lambda item: (item["score"], item["outgoing"]), reverse=True)
    top_score = rankings[0]["score"]
    candidates = [item["variable"] for item in rankings if item["score"] == top_score] if top_score > 0 else []

    return {
        "method": "KRR Granger, chronological holdout, one-sided sign test",
        "variables": VARIABLES,
        "lag": lag,
        "alpha": alpha,
        "gamma": gamma,
        "train_rows": train_end,
        "test_rows": len(features) - test_start,
        "edges": edges,
        "rankings": rankings,
        "candidates": candidates,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default="d07_te.dat", help="data/raw 下的 TEP 文件名")
    parser.add_argument("--start", type=int, default=160, help="从第几个零基行号开始取数据")
    parser.add_argument("--samples", type=int, default=100, help="分析多少个连续采样点")
    parser.add_argument("--lag", type=int, default=3, help="使用多少个历史采样点")
    parser.add_argument("--alpha", type=float, default=1.0, help="核岭回归正则化参数")
    args = parser.parse_args()
    if args.start < 0 or args.samples < 1 or args.alpha <= 0:
        parser.error("start >= 0、samples >= 1、alpha > 0")

    frame = load_data(args.file)
    window = frame.iloc[args.start : args.start + args.samples]
    if len(window) != args.samples:
        parser.error("所需时间窗超过文件末尾")
    result = diagnose(window.loc[:, VARIABLES].to_numpy(dtype=float), args.lag, args.alpha)
    result["data_file"] = args.file
    result["first_sample"] = args.start + 1
    result["sample_count"] = args.samples

    destination = Path(__file__).parent / "results" / "idv7_krr.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")

    print(f"分析第 {args.start + 1}–{args.start + args.samples} 个采样点")
    print(f"训练 {result['train_rows']} 行，测试 {result['test_rows']} 行，时滞 {args.lag}")
    print("变量排名（出边数 - 入边数；仅计 q < 0.10 的探索性关系）：")
    for item in result["rankings"]:
        print(f"  {item['variable']}: {item['outgoing']} - {item['incoming']} = {item['score']}")
    print("候选变量：" + ("、".join(result["candidates"]) if result["candidates"] else "证据不足"))
    selected = [edge for edge in result["edges"] if edge["selected"]]
    print(f"选出的关系: {len(selected)} 条；明细已保存到 {destination}")
    for edge in sorted(selected, key=lambda e: e["q_value"]):
        print(
            f"  {edge['source']} → {edge['target']}: "
            f"相对误差改善 {edge['improvement']:.1%}, q={edge['q_value']:.3g}"
        )
    print("说明：这是探索性时序预测关系；测试点可能相关，排名不能单独证明物理故障根因。")


if __name__ == "__main__":
    main()
