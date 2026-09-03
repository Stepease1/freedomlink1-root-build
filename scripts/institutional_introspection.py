#!/usr/bin/env python3
"""Summarize intelligence state, autonomy activity, and stability."""

import json
from pathlib import Path


with Path("lineage/intelligence_ledger.json").open(encoding="utf-8") as intel_file:
    intelligence = json.load(intel_file).get("analytics", {})
with Path("lineage/autonomy_ledger.json").open(encoding="utf-8") as autonomy_file:
    autonomy_cycles = json.load(autonomy_file).get("autonomy_events", [])

summary = {
    "intelligence_state": intelligence,
    "autonomy_cycles": len(autonomy_cycles),
    "stability": "stable" if intelligence.get("drift_risk") == "low" else "unstable",
}

print("[Consciousness] Introspection Summary:")
print(json.dumps(summary, indent=2))
