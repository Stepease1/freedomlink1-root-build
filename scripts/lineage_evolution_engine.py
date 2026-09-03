#!/usr/bin/env python3
"""Update lineage evolution state from institutional memory."""

import json
from pathlib import Path


with Path("lineage/consciousness_memory.json").open(encoding="utf-8") as memory_file:
    events = json.load(memory_file).get("events", [])
path = Path("lineage/epoch_ledger.json")
with path.open(encoding="utf-8") as ledger_file:
    ledger = json.load(ledger_file)

if len(events) > 5:
    ledger["evolution_state"] = "Adaptive Growth"

path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
print("[Evolution] Lineage evolution state updated.")
