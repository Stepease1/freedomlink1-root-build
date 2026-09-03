#!/usr/bin/env python3
"""Generate a constitutional stability assessment."""

import json
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    analytics = json.load(intel_file).get("analytics", {})
try:
    health = float(analytics.get("epoch_health", 100))
except (TypeError, ValueError):
    health = 100

adaptation = "Constitution requires reinforcement." if health < 50 else "Constitution stable."
Path("governance/constitution_adaptation.md").write_text(adaptation + "\n", encoding="utf-8")
print("[Evolution] Constitutional adaptation generated.")
