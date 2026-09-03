#!/usr/bin/env python3
"""Interpret the meaning of the current lineage epoch."""

import json
from pathlib import Path


meaning = {
    1: "Genesis - foundational identity and governance established.",
    2: "Expansion - intelligence and autonomy activated.",
    3: "Institutionalization - multi-module growth and sentinel evolution.",
    4: "Sovereign Maturity - full constitutional self-governance.",
}

with Path("lineage/epoch_ledger.json").open(encoding="utf-8") as ledger_file:
    epochs = json.load(ledger_file).get("epochs", [])

if not epochs:
    raise SystemExit("[Consciousness] No epoch found.")

epoch = epochs[-1].get("epoch")
print("[Consciousness] Epoch Meaning:")
print(meaning.get(epoch, "Unknown epoch meaning."))
