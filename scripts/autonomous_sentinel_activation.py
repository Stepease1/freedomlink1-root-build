#!/usr/bin/env python3
"""Activate GS-03 autonomously when drift risk is high."""

import json
import subprocess
import sys
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    risk = json.load(intel_file).get("analytics", {}).get("drift_risk")

if risk == "high":
    print("[Autonomy] High drift detected. Activating Sentinel GS-03.")
    subprocess.run([sys.executable, "scripts/activate_sentinel.py", "GS-03"], check=True)
else:
    print("[Autonomy] Drift not high. No autonomous activation required.")
