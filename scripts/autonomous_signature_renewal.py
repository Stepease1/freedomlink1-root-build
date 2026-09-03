#!/usr/bin/env python3
"""Renew sovereign integrity artifacts when anomalies are recorded."""

import json
import subprocess
import sys
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    anomalies = json.load(intel_file).get("analytics", {}).get("anomalies", [])

if anomalies:
    print("[Autonomy] Integrity anomalies detected. Renewing sovereign signature.")
    subprocess.run([sys.executable, "scripts/sign_epoch.py"], check=True)
else:
    print("[Autonomy] No anomalies detected. Signature renewal not required.")
