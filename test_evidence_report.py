
"""Regression tests for AutoAudit JSON evidence reports."""

import json
import tempfile
import unittest
from pathlib import Path

from evidence_report import generate_report


class TestEvidenceReport(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)

        self.results = [
            {
                "url": "https://example.com",
                "timestamp": "2026-11-01T12:00:00+00:00",
                "expected_status": 200,
                "actual_status": 200,
                "response_time_ms": 15.5,
                "result": "PASS",
                "error": None,
            },
            {
                "url": "https://example.com/missing",
                "timestamp": "2026-11-01T12:00:01+00:00",
                "expected_status": 200,
                "actual_status": 404,
                "response_time_ms": 18.2,
                "result": "FAIL",
                "error": None,
            },
        ]

    def test_report_saved_with_correct_counts(self):
        path = generate_report(
            self.results, output_dir=self.temp.name
        )

        self.assertTrue(path.is_file())

        with path.open(encoding="utf-8") as file:
            report = json.load(file)

        self.assertEqual(report["schema_version"], "1.0")
        self.assertEqual(report["summary"]["total"], 2)
        self.assertEqual(report["summary"]["passed"], 1)
        self.assertEqual(report["summary"]["failed"], 1)
        self.assertEqual(report["checks"], self.results)
        self.assertTrue(report["run_id"])
        self.assertTrue(report["generated_at"])

    def test_unique_reports_do_not_overwrite(self):
        first = generate_report(
            self.results, output_dir=self.temp.name
        )
        second = generate_report(
            self.results, output_dir=self.temp.name
        )

        self.assertNotEqual(first, second)
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())

        self.assertEqual(
            len(list(Path(self.temp.name).glob("*.json"))),
            2,
        )

    def test_empty_results_rejected(self):
        with self.assertRaises(ValueError):
            generate_report([], output_dir=self.temp.name)

    def test_invalid_result_rejected(self):
        invalid = [dict(self.results[0])]
        invalid[0]["result"] = "UNKNOWN"

        with self.assertRaises(ValueError):
            generate_report(
                invalid, output_dir=self.temp.name
            )


if __name__ == "__main__":
    unittest.main()
