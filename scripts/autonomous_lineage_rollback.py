#!/usr/bin/env python3
"""Roll back lineage only when intelligence records anomalies."""

import json
import subprocess
import sys
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    anomalies = json.load(intel_file).get("analytics", {}).get("anomalies", [])

if anomalies:
    print("[Autonomy] Critical anomalies detected. Initiating rollback.")
    subprocess.run([sys.executable, "scripts/rollback_epoch.py"], check=True)
else:
    print("[Autonomy] No rollback required.")
