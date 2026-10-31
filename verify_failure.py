
"""Verify AutoAudit returns a failure exit code."""

import sys
from unittest.mock import patch
from autoaudit import test_website


def main():
    with patch("autoaudit.urllib.request.urlopen") as mock:
        mock.return_value.__enter__.return_value.status = 404

        result = test_website(
            "https://example.com",
            expected_status=200
        )

    if result["result"] == "FAIL":
        print("EXPECTED FAILURE DETECTED")
        sys.exit(1)

    print("ERROR: Failure was not detected")
    sys.exit(0)


if __name__ == "__main__":
    main()
