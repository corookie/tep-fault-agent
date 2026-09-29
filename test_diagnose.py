"""用已知单向关系的合成序列检查诊断方向。"""

import unittest

import numpy as np

from diagnose import diagnose, lagged_samples


class DiagnosisTests(unittest.TestCase):
    def test_lagged_features_use_past_values_only(self) -> None:
        values = np.arange(35, dtype=float).reshape(5, 7)
        features, targets = lagged_samples(values, lag=2)
        np.testing.assert_array_equal(features[0, :7], values[1])
        np.testing.assert_array_equal(features[0, 7:], values[0])
        np.testing.assert_array_equal(targets[0], values[2])

    def test_recovers_known_direction(self) -> None:
        rng = np.random.default_rng(7)
        values = np.zeros((150, 7))
        for t in range(1, len(values)):
            values[t, 0] = 0.6 * values[t - 1, 0] + rng.normal(scale=0.5)
            values[t, 1] = (
                0.35 * values[t - 1, 1]
                + 1.8 * values[t - 1, 0]
                + rng.normal(scale=0.3)
            )
            values[t, 2:] = 0.4 * values[t - 1, 2:] + rng.normal(size=5)

        result = diagnose(values, lag=1)
        known_edge = next(
            edge
            for edge in result["edges"]
            if edge["source"] == "X4" and edge["target"] == "X7"
        )
        self.assertTrue(known_edge["selected"])
        self.assertGreater(known_edge["improvement"], 0)


if __name__ == "__main__":
    unittest.main()
