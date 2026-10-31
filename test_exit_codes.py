
"""Verify exit codes from the real AutoAudit entry point."""

import runpy
import sys
import unittest
from unittest.mock import patch


class TestExitCodes(unittest.TestCase):

    def run_main(self, simulated_status):
        """Run autoaudit.py as __main__ with a mocked HTTP status."""

        with patch("urllib.request.urlopen") as mock:
            mock.return_value.__enter__.return_value.status = (
                simulated_status
            )

            with patch.object(sys, "argv", ["autoaudit.py"]):
                with self.assertRaises(SystemExit) as caught:
                    runpy.run_path(
                        "autoaudit.py",
                        run_name="__main__"
                    )

        return caught.exception.code

    def test_success_exit_code(self):
        """HTTP 200 must return exit code 0."""
        code = self.run_main(200)
        self.assertEqual(code, 0)

    def test_failure_exit_code(self):
        """HTTP 404 must return exit code 1."""
        code = self.run_main(404)
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
