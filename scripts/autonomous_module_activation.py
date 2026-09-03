#!/usr/bin/env python3
"""Activate GIM-01 when intelligence recommends module activation."""

import json
import subprocess
import sys
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    recommendations = json.load(intel_file).get("analytics", {}).get("recommendations", [])

should_activate = any("activate a module" in str(item).lower() for item in recommendations)
if should_activate:
    print("[Autonomy] Recommendation detected: activating module GIM-01.")
    subprocess.run([sys.executable, "scripts/update_module_registry.py", "GIM-01"], check=True)
else:
    print("[Autonomy] No module activation required.")
