#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

registry_path = Path("lineage/module_registry.json")

if not registry_path.exists():
    print("[Modules] No module_registry.json, skipping.")
    raise SystemExit(0)

with registry_path.open() as f:
    registry = json.load(f)

for m in registry.get("modules", []):
    mid = m.get("id")
    if not mid:
        continue
    print(f"[Modules] Verifying {mid}...")
    subprocess.run(["python3", "tools/module_verify.py", mid], check=False)

print("[Modules] Module verification run complete.")
