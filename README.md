# GitHub Actions POC - Manual Trigger

![Manual Test Trigger](https://github.com/sreekanth-chaliyeduth/github-actions-poc/actions/workflows/manual_trigger.yml/badge.svg)

A simple Python test framework using **Playwright** and **Pytest**, designed to demonstrate **manual execution** of GitHub Actions workflows.

## Features
- **Manual Trigger**: Workflow configured with `workflow_dispatch` to be run manually from the GitHub UI.
- **Reporting**: Allure Reports integration.
- **Tools**: `pytest`, `playwright`, `make`.

## Quick Start

### Prerequisites
- Python 3.10+
- `make`

### Installation
```bash
make install
```

### Running Tests Locally
```bash
make test
```
*Results will be generated in `reports/allure-results`.*

### Viewing Reports
```bash
make report
```

### Clean Up
```bash
make clean
```

## How to Trigger Manually on GitHub

1.  Go to the [Actions Tab](../../actions/workflows/manual_trigger.yml).
2.  Select **Manual Test Trigger** from the sidebar.
3.  Click the **Run workflow** button.
4.  Leave branch as `main` and click the green **Run workflow** button.

## 🔒 Security Note
In a **public repository**:
- **Anyone** can view the code and the test results (Actions history).
- **ONLY** collaborators (people with write access) can **trigger** the workflow manually. 
- Random visitors **cannot** trigger this workflow.
