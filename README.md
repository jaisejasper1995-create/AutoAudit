
# AutoAudit

Automated Software Quality Assurance & Testing

**"I test the claim — not just the demo."**

## Overview

AutoAudit is a Python-based software quality assurance tool that automates website availability checks, HTTP status validation, and structured JSON evidence reporting.

The goal is to identify failures, collect evidence, and generate reliable testing reports.

## Verified Capabilities

- Website availability checks
- HTTP status code validation
- Response time measurement
- Automated PASS/FAIL reporting
- JSON evidence generation with timestamps and unique run IDs
- GitHub Actions automated testing and evidence artifact uploads

## Planned Features (Not Yet Verified)

- Broader API response testing
- Persistent test history
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

**Release Candidate: v1.0.0**

- Milestone 5: VERIFIED PASS
- Automated tests: 8 PASS
- Clean-install verification: PASS (Windows, Python 3)
- GitHub Actions validation: PASS (previously verified run)
- JSON evidence generation: VERIFIED
- MIT License: VERIFIED
- Release publication: PENDING

AutoAudit is undergoing final release verification. The project is not considered officially released until the v1.0.0 GitHub release is published and verified.




## Quality Standards

Every feature must be tested before being marked complete.

Failures must be documented, investigated, and corrected without hiding evidence.

## Project Purpose

Build a complete, verifiable software QA application while demonstrating practical Python development, debugging, automated testing, and GitHub version control.


## Installation and Usage

AutoAudit requires Python 3 and Git.

### 1. Clone the repository

```cmd
git clone https://github.com/jaisejasper1995-create/AutoAudit.git
cd AutoAudit
```

### 2. Run the automated tests

```cmd
python -m unittest discover -v
```

The verified baseline contains 8 automated tests.

### 3. Run AutoAudit

```cmd
python autoaudit.py
```

AutoAudit performs its configured validation checks and displays the result in the terminal.

### 4. Inspect JSON evidence

After execution, check the generated reports:

```cmd
dir reports
type reports\*.json
```

Evidence reports include run identifiers, timestamps, validation results, and PASS/FAIL summaries.

### Verification Environment

The release candidate was tested using a fresh Git clone on Windows with Python 3. Automated tests and the default execution completed successfully.

See the Verification Evidence and Verification Limitations sections above for the recorded results and boundaries of testing.
