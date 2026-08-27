#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retire a module by updating the registry and archiving its artifact.

Usage: python3 scripts/retire_module.py <module_id>
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def main(argv):
    if len(argv) < 2:
        print("Usage: retire_module.py <module_id>")
        return 1

    module_id = argv[1]

    registry_path = Path("lineage/module_registry.json")
    if not registry_path.exists():
        print(f"[Retire] registry not found: {registry_path}")
        return 2

    archive_dir = Path("archive/modules")
    archive_dir.mkdir(parents=True, exist_ok=True)

    with registry_path.open("r", encoding="utf-8") as f:
        registry = json.load(f)

    modules = registry.get("modules", [])
    module = next((m for m in modules if m.get("id") == module_id), None)
    if not module:
        print(f"[Retire] Module {module_id} not found.")
        return 3

    module["status"] = "retired"
    module["retired_at"] = datetime.utcnow().isoformat() + "Z"

    artifact_path = Path(f"artifacts/{module_id}.json")
    if artifact_path.exists():
        archive_path = archive_dir / f"{module_id}.json"
        archive_path.write_bytes(artifact_path.read_bytes())
        print(f"[Retire] Archived artifact to {archive_path}")
    else:
        print(f"[Retire] No artifact found at {artifact_path}; skipping archive.")

    with registry_path.open("w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print(f"[Retire] Updated {registry_path} for {module_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
