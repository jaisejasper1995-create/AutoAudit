
"""Generate structured JSON evidence from AutoAudit results."""

import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def generate_report(results, output_dir="reports"):
    """Validate results and save a unique evidence report."""

    if not isinstance(results, list) or not results:
        raise ValueError("Results must be a nonempty list")

    required = {
        "url",
        "timestamp",
        "expected_status",
        "actual_status",
        "response_time_ms",
        "result",
        "error",
    }

    for index, item in enumerate(results):
        if not isinstance(item, dict):
            raise ValueError(f"Result {index} is not an object")

        if not required.issubset(item):
            raise ValueError(f"Result {index} missing required fields")

        if item["result"] not in ("PASS", "FAIL"):
            raise ValueError(f"Result {index} has invalid status")

    passed = sum(item["result"] == "PASS" for item in results)
    failed = len(results) - passed

    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%S%fZ") + "_" + uuid4().hex[:8]

    report = {
        "schema_version": "1.0",
        "run_id": run_id,
        "generated_at": now.isoformat(),
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": failed,
        },
        "checks": results,
    }

    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    destination = directory / f"autoaudit_{run_id}.json"

    # Exclusive creation prevents accidental overwriting.
    with destination.open("x", encoding="utf-8") as file:
        json.dump(report, file, indent=2)
        file.write("\n")

    return destination
