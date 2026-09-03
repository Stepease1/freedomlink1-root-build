#!/usr/bin/env python3
"""Advance the epoch only on an explicit intelligence recommendation."""

import json
import subprocess
import sys
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    recommendations = json.load(intel_file).get("analytics", {}).get("recommendations", [])

should_advance = any("advance the epoch" in str(item).lower() for item in recommendations)
if should_advance:
    print("[Autonomy] Recommendation detected: advancing epoch.")
    subprocess.run([sys.executable, "scripts/advance_epoch.py"], check=True)
else:
    print("[Autonomy] No epoch advancement required.")
