#!/usr/bin/env python3
"""Activate a module in the lineage module registry."""

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: update_module_registry.py <module-id>", file=sys.stderr)
        return 2

    module_id = sys.argv[1]
    path = Path("lineage/module_registry.json")
    registry = json.loads(path.read_text(encoding="utf-8"))
    modules = registry.setdefault("modules", [])

    for module in modules:
        if module.get("id") == module_id:
            module["status"] = "active"
            break
    else:
        modules.append({
            "id": module_id,
            "name": module_id,
            "status": "active",
            "epoch": 2,
            "hash": "pending",
        })

    path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    print(f"[Module] Activated: {module_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())