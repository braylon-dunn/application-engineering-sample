"""Illustrative budgetary estimating tool; not an electrical design or quotation engine."""
import json
import sys
from pathlib import Path

BASE_SECTION = 12000.0
MAIN_BREAKER_ALLOWANCE = 18000.0
FEEDER_ALLOWANCE = 7500.0
METERING_ALLOWANCE = 3500.0


def estimate(request):
    voltage = request.get("voltage_v")
    main = request.get("main_bus_a")
    feeders = request.get("feeders_a")
    if voltage != 480:
        raise ValueError("Illustrative model supports 480 V only")
    if not isinstance(main, int) or isinstance(main, bool) or main <= 0:
        raise ValueError("main_bus_a must be a positive integer")
    if not isinstance(feeders, list) or not feeders or any(not isinstance(x, int) or isinstance(x, bool) or x <= 0 for x in feeders):
        raise ValueError("feeders_a must be a nonempty list of positive integers")
    if any(x > main for x in feeders):
        raise ValueError("Feeder rating exceeds main bus rating; engineering review required")
    count = len(feeders)
    subtotal = BASE_SECTION + MAIN_BREAKER_ALLOWANCE + count * FEEDER_ALLOWANCE + METERING_ALLOWANCE
    contingency = round(subtotal * 0.15, 2)
    return {
        "status": "ILLUSTRATIVE ONLY - NOT A QUOTE OR DESIGN",
        "voltage_v": voltage,
        "main_bus_a": main,
        "feeder_count": count,
        "feeder_ratings_a": feeders,
        "base_and_main_allowance_usd": BASE_SECTION + MAIN_BREAKER_ALLOWANCE,
        "feeders_allowance_usd": count * FEEDER_ALLOWANCE,
        "metering_allowance_usd": METERING_ALLOWANCE,
        "subtotal_usd": subtotal,
        "contingency_15pct_usd": contingency,
        "illustrative_total_usd": round(subtotal + contingency, 2),
        "required_reviews": ["OEM pricing", "available fault current", "interrupting ratings", "protection coordination", "arc-flash assessment", "site layout"],
    }


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python calculator/estimate.py calculator/sample-request.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(estimate(data), indent=2))


if __name__ == "__main__":
    main()
