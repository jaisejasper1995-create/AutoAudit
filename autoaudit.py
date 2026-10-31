import urllib.request
import urllib.error
import time
import json
from datetime import datetime, timezone


def test_website(url, expected_status=200):
    """Test website availability and response time."""

    print(f"\nAutoAudit: Testing {url}")

    start_time = time.perf_counter()

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "AutoAudit/1.0"}
        )

        with urllib.request.urlopen(
            request, timeout=10
        ) as response:
            status_code = response.status

        error = None

    except urllib.error.HTTPError as exc:
        status_code = exc.code
        error = str(exc)

    except (urllib.error.URLError, TimeoutError) as exc:
        status_code = None
        error = str(exc)

    elapsed_ms = round(
        (time.perf_counter() - start_time) * 1000, 2
    )

    passed = status_code == expected_status

    result = {
        "url": url,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "expected_status": expected_status,
        "actual_status": status_code,
        "response_time_ms": elapsed_ms,
        "result": "PASS" if passed else "FAIL",
        "error": error
    }

    print(json.dumps(result, indent=2))
    return result



if __name__ == "__main__":
    import sys

    result = test_website("https://example.com")

    if result["result"] == "FAIL":
        print("AutoAudit detected a failed check.")
        sys.exit(1)

    print("AutoAudit check passed.")
    sys.exit(0)

  
