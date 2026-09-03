#!/usr/bin/env python3
"""Calculate a simple health score for the current epoch."""

import json
from pathlib import Path


with Path("lineage/epoch_ledger.json").open(encoding="utf-8") as ledger_file:
    epochs = json.load(ledger_file).get("epochs", [])

if not epochs:
    print("[EpochHealth] No epochs found.")
    raise SystemExit(1)

current = epochs[-1]
score = 100
if current.get("advanced_at") is None:
    score -= 10
if not current.get("modules_activated"):
    score -= 10
if not current.get("pocs_graduated"):
    score -= 10
if len(current.get("sentinels_active", [])) < 3:
    score -= 20

print(f"[EpochHealth] Epoch {current.get('epoch')} Health Score: {score}/100")
