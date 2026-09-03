#!/usr/bin/env python3
"""Run the independent governance tests and stop at the first failure."""

import subprocess
import sys


tests = [
    [sys.executable, "-m", "pytest", "tests/governance/test_lineage.py"],
    [sys.executable, "-m", "pytest", "tests/governance/test_modules.py"],
    [sys.executable, "-m", "pytest", "tests/governance/test_pocs.py"],
]

for test in tests:
    print(f"[FastFail] Running: {' '.join(test)}")
    result = subprocess.run(test)
    if result.returncode != 0:
        print("[FastFail] Failure detected. Stopping early.")
        sys.exit(result.returncode)

print("[FastFail] All governance tests passed.")
