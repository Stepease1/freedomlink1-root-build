#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

registry_path = Path("lineage/poc_registry.json")

if not registry_path.exists():
    print("[POC] No poc_registry.json, skipping.")
    raise SystemExit(0)

with registry_path.open() as f:
    registry = json.load(f)

for p in registry.get("pocs", []):
    pid = p.get("id")
    if not pid:
        continue
    print(f"[POC] Verifying {pid}...")
    subprocess.run(["python3", "tools/poc_verify.py", pid], check=False)

print("[POC] POC verification run complete.")
