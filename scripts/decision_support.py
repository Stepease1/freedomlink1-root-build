#!/usr/bin/env python3
"""Generate governance recommendations from identity and epoch state."""

import json
from pathlib import Path


with Path("lineage/identity_ledger.json").open(encoding="utf-8") as identity_file:
    identity = json.load(identity_file).get("identity", {})
with Path("lineage/epoch_ledger.json").open(encoding="utf-8") as ledger_file:
    epochs = json.load(ledger_file).get("epochs", [])

if not epochs:
    print("[DecisionSupport] No current epoch available.")
    raise SystemExit(1)

current = epochs[-1]
recommendations = []
if identity.get("sentinel_count", 0) < 3:
    recommendations.append("Activate additional sentinel.")
if current.get("advanced_at") is None:
    recommendations.append("Consider advancing epoch.")
if not current.get("modules_activated"):
    recommendations.append("Activate a module to strengthen lineage.")

print("[DecisionSupport] Recommendations:")
for recommendation in recommendations:
    print(f"- {recommendation}")
