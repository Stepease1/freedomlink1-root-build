#!/usr/bin/env python3
"""Remove the latest epoch after an explicitly authorized rollback."""

import json
import sys
from pathlib import Path


path = Path("lineage/epoch_ledger.json")
ledger = json.loads(path.read_text(encoding="utf-8"))
epochs = ledger.get("epochs", [])
if len(epochs) < 2:
    print("[Rollback] No previous epoch available; no rollback performed.")
    sys.exit(0)

removed = epochs.pop()
path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
print(f"[Rollback] Removed epoch {removed.get('epoch')}; restored epoch {epochs[-1].get('epoch')}.")
