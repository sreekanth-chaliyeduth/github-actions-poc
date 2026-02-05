# GitHub Actions POC - Manual Trigger

![Automated Tests](https://github.com/sreekanth-chaliyeduth/github-actions-poc/actions/workflows/automated_tests.yml/badge.svg)

A simple Python test framework using **Playwright** and **Pytest**, designed to demonstrate **manual execution** of GitHub Actions workflows.

## Features
- **Triggers**: Manual (`workflow_dispatch`), Scheduled (Daily), and PR-based.
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

## 🤖 Automated Triggers & Control
You can control when the tests run using **Repository Variables** (Settings > Secrets and variables > Actions > Variables).

| Trigger Type | Description | How to Disable |
| :--- | :--- | :--- |
| **Manual** | Triggers via the "Run workflow" button. | Cannot be disabled (always available). |
| **Daily Schedule** | Runs at **1:35 PM IST** (08:05 UTC). | Create Variable `ENABLE_SCHEDULE` = `false` |
| **Pull Request** | Runs on PRs to `main`. | Create Variable `ENABLE_PR_CHECKS` = `false` |

> **Note**: If the variable does not exist, the trigger defaults to **ON**. To disable, you must explicitly create the variable and set it to `false`.

## 📊 Allure Report & History
Tests reports are automatically published to **GitHub Pages**.
- **Report URL**: `https://sreekanth-chaliyeduth.github.io/github-actions-poc/`
- **History**: The report includes a trend graph showing the history of previous test runs. This is handled by determining the difference between the current run and the previous report stored in the `gh-pages` branch.

**Setup Note**:
After the first successful run, go to `Settings` -> `Pages` in your repository and ensure the source is set to **Deploy from a branch** and select `gh-pages` / `/ (root)`.

## 🔒 Security Note
In a **public repository**:
- **Anyone** can view the code and the test results (Actions history).
- **ONLY** collaborators (people with write access) can **trigger** the workflow manually. 
- Random visitors **cannot** trigger this workflow.
