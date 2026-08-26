#!/usr/bin/env python3
import json
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: verify_lineage.py <lineage_dir>", file=sys.stderr)
    sys.exit(2)

lineage_dir = Path(sys.argv[1])

def check_file(path, key):
    if not path.exists():
        print(f"[Lineage] Missing {path}, skipping {key} check.")
        return False
    with path.open() as f:
        data = json.load(f)
    if key not in data:
        print(f"[Lineage] {path} missing key: {key}")
        return False
    return True

epoch_ok = check_file(lineage_dir / "epoch_ledger.json", "epochs")
module_ok = check_file(lineage_dir / "module_registry.json", "modules")
poc_ok = check_file(lineage_dir / "poc_registry.json", "pocs")

if epoch_ok and module_ok and poc_ok:
    print("[Lineage] Lineage structure verified.")
else:
    print("[Lineage] Lineage verification incomplete (see messages above).")
