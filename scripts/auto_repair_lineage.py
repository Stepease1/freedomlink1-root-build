#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Attempt to repair malformed or missing lineage JSON files.

This script is safe to run: it will create minimal structures when files are
missing or corrupted.
"""

import json
from pathlib import Path


def repair(path: Path, key: str):
    try:
        text = path.read_text(encoding='utf-8')
        data = json.loads(text)
        if key not in data:
            print(f"[Repair] {path} missing key {key}. Rebuilding minimal structure.")
            data[key] = []
    except Exception:
        print(f"[Repair] {path} corrupted or missing. Rebuilding minimal structure.")
        data = {key: []}

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"[Repair] Repaired {path}")


def main():
    repair(Path('lineage/epoch_ledger.json'), 'epochs')
    repair(Path('lineage/module_registry.json'), 'modules')
    repair(Path('lineage/poc_registry.json'), 'pocs')
    print('[Repair] Lineage auto-repair complete.')


if __name__ == '__main__':
    main()
