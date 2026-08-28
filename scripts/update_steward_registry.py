#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the steward registry during succession ceremonies.

Usage: python3 scripts/update_steward_registry.py <name> <public_key> <fingerprint>
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def main(argv):
    if len(argv) < 4:
        print("Usage: update_steward_registry.py <name> <public_key> <fingerprint>")
        return 2

    name = argv[1]
    pubkey = argv[2]
    fingerprint = argv[3]

    path = Path("lineage/steward_registry.json")
    if not path.exists():
        print(f"[Steward] registry not found: {path}; creating new registry")
        registry = {"project": "Freedomlink1", "version": "1.0.0", "current_steward": None, "retired_stewards": []}
    else:
        try:
            registry = json.loads(path.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"[Steward] failed to read registry: {e}")
            return 3

    old = registry.get("current_steward")
    if old:
        registry.setdefault("retired_stewards", []).append(old)

    registry["current_steward"] = {
        "name": name,
        "role": "Sovereign Steward",
        "installed_at": datetime.utcnow().isoformat() + "Z",
        "key_fingerprint": fingerprint,
        "public_key": pubkey
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding='utf-8')

    print(f"[Steward] Installed new steward: {name}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
