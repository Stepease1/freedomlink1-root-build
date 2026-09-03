#!/usr/bin/env python3
"""Update the current epoch's evolutionary meaning."""

import json
from pathlib import Path


path = Path("lineage/epoch_ledger.json")
with path.open(encoding="utf-8") as ledger_file:
    ledger = json.load(ledger_file)

epochs = ledger.get("epochs", [])
if not epochs:
    raise SystemExit("[Evolution] No epoch found.")

current = epochs[-1]
if current.get("epoch") == 2:
    current["metamorphosis"] = "Transitioning toward Institutionalization"

path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
print("[Evolution] Epoch metamorphosis updated.")
