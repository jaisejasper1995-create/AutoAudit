
# AutoAudit

Automated Software Quality Assurance & Testing

**"I test the claim — not just the demo."**

## Overview

AutoAudit is a Python-based software testing tool designed to automate repetitive website and API validation tasks.

The goal is to identify failures, collect evidence, and generate reliable testing reports.

## Planned Features

- Website availability checks
- HTTP status code validation
- API response testing
- Response time measurement
- Automated PASS/FAIL reporting
- Test history and evidence collection
- HTML reporting dashboard

## Technology

- Python 3
- Git and GitHub
- Automated testing frameworks


## Development Status

### Milestone 5 — Automated JSON Evidence Reporting

Status: VERIFIED PASS (November 1, 2026)

AutoAudit generates structured JSON evidence for website validation checks.

Verified capabilities:
- HTTP status validation
- PASS/FAIL classification
- Response-time recording
- UTC timestamps and unique run IDs
- Automated JSON report generation
- Summary counts for passed and failed checks
- GitHub Actions artifact uploads
- Downloadable evidence reports

### Verification Evidence

- 8 automated unit tests passed.
- GitHub Actions validation completed successfully.
- 3 JSON evidence reports inspected.
- 2 reports recorded PASS.
- 1 report recorded FAIL for an HTTP 404 response when HTTP 200 was expected.
- Report summaries matched their recorded checks.
- GitHub Actions successfully uploaded the evidence artifact.

### Verification Limitations

Live HTTP responses were not independently reproduced during the final evidence inspection.

### Project Status

Milestone 5: VERIFIED PASS

Next: Release-readiness review, documentation cleanup, and clean-install verification.




## Quality Standards

Every feature must be tested before being marked complete.

Failures must be documented, investigated, and corrected without hiding evidence.

## Project Purpose

Build a complete, verifiable software QA application while demonstrating practical Python development, debugging, automated testing, and GitHub version control.
