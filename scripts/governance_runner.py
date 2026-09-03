#!/usr/bin/env python3
"""Run the complete governance verification sequence."""

import subprocess
import sys


steps = [
    ["bash", "install/smoke_test.sh"],
    [sys.executable, "-m", "pytest", "tests/governance/"],
    [sys.executable, "scripts/verify_lineage.py", "lineage/"],
    [sys.executable, "tools/module_verify_all.py"],
    [sys.executable, "tools/poc_verify_all.py"],
]

for step in steps:
    print(f"[Runner] Executing: {' '.join(step)}")
    subprocess.run(step, check=True)

print("[Runner] Governance checks complete.")
