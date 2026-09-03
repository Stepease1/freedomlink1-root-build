#!/usr/bin/env python3
"""Estimate lineage drift risk from epoch-to-epoch changes."""

import json
from pathlib import Path


with Path("lineage/epoch_ledger.json").open(encoding="utf-8") as ledger_file:
    epochs = json.load(ledger_file).get("epochs", [])

drift_risk = "low"
if len(epochs) > 1:
    last = epochs[-1]
    previous = epochs[-2]
    if last.get("modules_activated") != previous.get("modules_activated"):
        drift_risk = "medium"
    if last.get("pocs_graduated") != previous.get("pocs_graduated"):
        drift_risk = "medium"
    if last.get("sentinels_active") != previous.get("sentinels_active"):
        drift_risk = "high"

print(f"[DriftForecast] Drift Risk: {drift_risk}")
