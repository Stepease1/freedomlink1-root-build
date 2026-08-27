#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rotate the omni proof master by archiving the existing file.

This script moves `artifacts/omni_proof_master.json` to
`lineage/retired_keys/omni_proof_master_retired_<timestamp>.json`.

It is intentionally conservative: it only archives the existing proof master
and instructs the operator to update the active proof master manually.
"""

import json
from pathlib import Path
from datetime import datetime
import sys


def main():
    old_master_path = Path("artifacts/omni_proof_master.json")
    if not old_master_path.exists():
        print(f"[Key Rotation] No {old_master_path} found; nothing to rotate.")
        return 0

    retired_dir = Path("lineage/retired_keys")
    retired_dir.mkdir(parents=True, exist_ok=True)

    try:
        with old_master_path.open("r", encoding="utf-8") as f:
            master = json.load(f)
    except Exception as e:
        print(f"[Key Rotation] Failed to read {old_master_path}: {e}")
        return 2

    timestamp = datetime.utcnow().isoformat().replace(":", "-")
    retired_path = retired_dir / f"omni_proof_master_retired_{timestamp}.json"

    retired_path.write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[Key Rotation] Retired old proof master to {retired_path}")
    print("[Key Rotation] Now update artifacts/omni_proof_master.json with new key + signature manually.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
