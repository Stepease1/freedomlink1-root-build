#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare current lineage snapshot with the last integrity snapshot.

Creates `lineage/last_integrity_snapshot.json` on first run.
"""

import json
from pathlib import Path
from datetime import datetime


def load(path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def main():
    lineage_dir = Path('lineage')
    lineage_dir.mkdir(parents=True, exist_ok=True)

    current = {
        "epoch": load(Path('lineage/epoch_ledger.json')),
        "modules": load(Path('lineage/module_registry.json')),
        "pocs": load(Path('lineage/poc_registry.json')),
    }

    prev_path = Path('lineage/last_integrity_snapshot.json')

    if not prev_path.exists():
        print('[Diff] No previous snapshot. Creating baseline.')
        prev_path.write_text(json.dumps(current, indent=2, ensure_ascii=False), encoding='utf-8')
        return 0

    prev = load(prev_path) or {}

    def diff(a, b):
        return a != b

    changes = {
        "epoch_changed": diff(current.get('epoch'), prev.get('epoch')),
        "modules_changed": diff(current.get('modules'), prev.get('modules')),
        "pocs_changed": diff(current.get('pocs'), prev.get('pocs')),
    }

    print('[Diff] Lineage Changes:')
    for k, v in changes.items():
        print(f'- {k}: {"YES" if v else "NO"}')

    # Save current snapshot for next run
    backup = prev_path.with_suffix('.bak.json')
    try:
        if prev_path.exists():
            backup.write_text(prev_path.read_text(encoding='utf-8'), encoding='utf-8')
    except Exception:
        pass

    prev_path.write_text(json.dumps(current, indent=2, ensure_ascii=False), encoding='utf-8')
    print('[Diff] Snapshot updated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
