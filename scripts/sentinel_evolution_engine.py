#!/usr/bin/env python3
"""Evolve sentinel roles according to the current drift risk."""

import json
from pathlib import Path


sentinel_path = Path("lineage/sentinel_registry.json")
with sentinel_path.open(encoding="utf-8") as sentinels_file:
    registry = json.load(sentinels_file)
with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    risk = json.load(intel_file).get("analytics", {}).get("drift_risk", "low")

role = {
    "medium": "Enhanced Drift Monitoring",
    "high": "Critical Drift Intervention",
}.get(risk)
if role:
    for sentinel in registry.get("sentinels", []):
        sentinel["role"] = role

sentinel_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
print(f"[Evolution] Sentinel roles evolved for drift risk: {risk}.")
