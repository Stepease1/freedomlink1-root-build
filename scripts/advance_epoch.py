#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advance the epoch ledger by one epoch.

Usage: python3 scripts/advance_epoch.py
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def main():
    path = Path("lineage/epoch_ledger.json")
    if not path.exists():
        print(f"[Epoch] ledger not found: {path}")
        return 2

    try:
        ledger = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"[Epoch] failed to read ledger: {e}")
        return 3

    epochs = ledger.setdefault("epochs", [])
    if not epochs:
        print("[Epoch] no epochs present; initializing epoch 1")
        epochs.append({
            "epoch": 1,
            "started_at": datetime.utcnow().isoformat() + "Z",
            "advanced_at": None,
            "modules_activated": [],
            "pocs_graduated": [],
            "sentinels_active": [],
            "sovereign_signature": "pending"
        })

    current_epoch = epochs[-1].get("epoch", 1)
    new_epoch = current_epoch + 1

    # mark advanced_at for the previous epoch
    epochs[-1]["advanced_at"] = datetime.utcnow().isoformat() + "Z"

    # append new epoch
    epochs.append({
        "epoch": new_epoch,
        "started_at": datetime.utcnow().isoformat() + "Z",
        "advanced_at": None,
        "modules_activated": [],
        "pocs_graduated": [],
        "sentinels_active": ["GS-01", "GS-02", "GS-03"],
        "sovereign_signature": "pending"
    })

    path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding='utf-8')

    print(f"[Epoch] Advanced to epoch {new_epoch}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
