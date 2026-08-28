# Governance Runner

This document describes how to run the repository's governance checks locally.

Quick commands

- Run the Python runner:

```
python scripts/run_governance_checks.py
```

- Run the shell runner (POSIX/bash):

```
bash scripts/run_governance_checks.sh
```

Run components individually

- Validate epoch ledger: `python scripts/validate_epoch_ledger.py`
- Run integrity monitor: `python scripts/integrity_monitor.py`
- Run lineage diff: `python scripts/lineage_diff.py`

VS Code `tasks.json` (recommended)

Use the following `tasks.json` content to bind a build task that runs the project's smoke tests and governance pytest suite:

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Governance Checks",
      "type": "shell",
      "command": "bash install/smoke_test.sh && pytest tests/governance/",
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    }
  ]
}
```

Notes

- The runners skip steps when required tools or files are missing (e.g., `pytest`).
- On Windows use the Python runner for best compatibility.
