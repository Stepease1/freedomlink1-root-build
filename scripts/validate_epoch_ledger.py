#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate the structure of lineage/epoch_ledger.json.

Exits 0 on success, non-zero on failure. Designed to be run in CI.
"""

import json
import sys
from pathlib import Path


REQUIRED_EPOCH_KEYS = {
    "epoch",
    "started_at",
    "advanced_at",
    "modules_activated",
    "pocs_graduated",
    "sentinels_active",
    "sovereign_signature",
}


def fail(msg: str):
    print("[Validate] ERROR:", msg)
    sys.exit(2)


def main():
    path = Path('lineage/epoch_ledger.json')
    if not path.exists():
        fail(f"Missing {path}")

    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        fail(f"Invalid JSON: {e}")

    if not isinstance(data, dict):
        fail("Top-level JSON is not an object")

    for key in ('project', 'version', 'current_epoch', 'epochs'):
        if key not in data:
            fail(f"Missing top-level key: {key}")

    current_epoch = data.get("current_epoch")
    if not isinstance(current_epoch, int) or isinstance(current_epoch, bool):
        fail("'current_epoch' must be an integer")

    epochs = data.get('epochs')
    if not isinstance(epochs, list) or not epochs:
        fail("'epochs' must be a non-empty list")

    epoch_numbers = []
    for idx, e in enumerate(epochs):
        if not isinstance(e, dict):
            fail(f"Epoch entry {idx} is not an object")
        missing = REQUIRED_EPOCH_KEYS - set(e.keys())
        if missing:
            fail(f"Epoch {idx} missing keys: {sorted(list(missing))}")
        if not isinstance(e["epoch"], int) or isinstance(e["epoch"], bool):
            fail(f"Epoch entry {idx} has a non-integer epoch number")
        epoch_numbers.append(e["epoch"])

    if len(epoch_numbers) != len(set(epoch_numbers)):
        fail("Epoch numbers must be unique")
    if not any(epoch["epoch"] == current_epoch for epoch in epochs):
        fail("'current_epoch' must identify an entry in 'epochs'")

    active_epochs = [epoch["epoch"] for epoch in epochs if epoch.get("status") == "active"]
    if active_epochs != [current_epoch]:
        fail(f"Exactly the current epoch must have status 'active'; found {active_epochs}")

    print("[Validate] epoch_ledger.json structure: OK")
    return 0


if __name__ == '__main__':
    sys.exit(main())
