#!/usr/bin/env python3
"""Propose governance adaptations from current intelligence and memory."""

import json
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    analytics = json.load(intel_file).get("analytics", {})
with Path("lineage/consciousness_memory.json").open(encoding="utf-8") as memory_file:
    events = json.load(memory_file).get("events", [])

try:
    health = float(analytics.get("epoch_health", 100))
except (TypeError, ValueError):
    health = 100

adaptations = []
if health < 60:
    adaptations.append("Strengthen governance tests.")
if len(events) > 10:
    adaptations.append("Expand sentinel responsibilities.")

Path("lineage/governance_adaptations.json").write_text(
    json.dumps({"adaptations": adaptations}, indent=2) + "\n",
    encoding="utf-8",
)
print("[Evolution] Governance adaptations proposed.")
