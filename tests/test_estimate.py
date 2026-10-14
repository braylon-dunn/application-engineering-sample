import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "calculator"))
from estimate import estimate


class EstimatorTests(unittest.TestCase):
    def test_three_feeders(self):
        result = estimate({"voltage_v": 480, "main_bus_a": 2000, "feeders_a": [800, 600, 400]})
        self.assertEqual(result["subtotal_usd"], 56000.0)
        self.assertEqual(result["illustrative_total_usd"], 64400.0)

    def test_unsupported_voltage(self):
        with self.assertRaises(ValueError):
            estimate({"voltage_v": 4160, "main_bus_a": 2000, "feeders_a": [800]})

    def test_invalid_feeder(self):
        with self.assertRaises(ValueError):
            estimate({"voltage_v": 480, "main_bus_a": 2000, "feeders_a": [2500]})


if __name__ == "__main__":
    unittest.main()
