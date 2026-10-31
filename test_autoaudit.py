
import unittest
from unittest.mock import patch
from autoaudit import test_website


class TestAutoAudit(unittest.TestCase):

    def test_successful_response(self):
        """HTTP 200 should PASS."""

        with patch("autoaudit.urllib.request.urlopen") as mock:
            mock.return_value.__enter__.return_value.status = 200

            result = test_website(
                "https://example.com",
                expected_status=200
            )

        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["actual_status"], 200)

    def test_unexpected_response(self):
        """HTTP 404 should FAIL when 200 is expected."""

        with patch("autoaudit.urllib.request.urlopen") as mock:
            mock.return_value.__enter__.return_value.status = 404

            result = test_website(
                "https://example.com",
                expected_status=200
            )

        self.assertEqual(result["result"], "FAIL")
        self.assertEqual(result["actual_status"], 404)


if __name__ == "__main__":
    unittest.main()
