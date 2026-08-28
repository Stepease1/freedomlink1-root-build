#!/usr/bin/env python3
"""Run a sequence of governance checks locally.

This script is safe to run locally and prints clear status lines. It executes
the validator, integrity monitor, lineage diff, and (optionally) pytest.
"""

import subprocess
import sys
from pathlib import Path


SCRIPTS = [
    ("Validate epoch ledger", Path("scripts/validate_epoch_ledger.py")),
    ("Integrity monitor", Path("scripts/integrity_monitor.py")),
    ("Lineage diff", Path("scripts/lineage_diff.py")),
]


def run(cmd):
    print(f"\n>>> Running: {' '.join(cmd)}")
    try:
        r = subprocess.run(cmd, check=False)
        print(f"Return code: {r.returncode}")
        return r.returncode
    except FileNotFoundError:
        print("Command not found: ", cmd[0])
        return 127


def main():
    failures = 0

    for name, path in SCRIPTS:
        if not path.exists():
            print(f"[Skip] {name}: {path} not found")
            continue
        code = run([sys.executable, str(path)])
        if code != 0:
            print(f"[FAIL] {name} (exit {code})")
            failures += 1
        else:
            print(f"[OK] {name}")

    # Optionally run pytest if tests exist and pytest is available
    if Path("tests").exists():
        try:
            import importlib
            spec = importlib.util.find_spec("pytest")
            if spec is None:
                print("[Skip] pytest not installed; skipping test run")
            else:
                code = run([sys.executable, "-m", "pytest", "-q"]) 
                if code != 0:
                    failures += 1
        except Exception:
            print("[Skip] Unable to determine pytest availability; skipping tests")

    if failures:
        print(f"\nGovernance checks completed: {failures} failure(s)")
        return 2
    print("\nGovernance checks completed: all OK")
    return 0


if __name__ == '__main__':
    sys.exit(main())
