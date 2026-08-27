#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the lineage/sentinel_registry.json status for a sentinel.

Usage: python3 scripts/update_sentinel_registry.py <SID> <status>
"""

import json
import sys
from pathlib import Path


def main(argv):
    if len(argv) < 3:
        print("Usage: update_sentinel_registry.py <SID> <status>")
        return 2

    sid = argv[1]
    status = argv[2]

    path = Path("lineage/sentinel_registry.json")
    if not path.exists():
        print(f"[Sentinel] registry not found: {path}")
        return 3

    try:
        registry = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"[Sentinel] failed to load registry: {e}")
        return 4

    found = False
    for s in registry.get("sentinels", []):
        if s.get("id") == sid:
            s["status"] = status
            found = True

    if not found:
        print(f"[Sentinel] {sid} not found; adding new entry")
        registry.setdefault("sentinels", []).append({
            "id": sid,
            "name": sid,
            "status": status,
            "scope": "unspecified"
        })

    path.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"[Sentinel] Updated {sid} → {status}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
