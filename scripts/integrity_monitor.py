#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple Root Build integrity checks for local and CI use.

Prints status lines and exits with non-zero if a baseline check fails.
"""

import json
import sys
from pathlib import Path


def check(path: Path, key: str):
    if not path.exists():
        return f"Missing {path}"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return f"Invalid JSON {path}: {e}"
    if key not in data:
        return f"{path} missing key {key}"
    return "OK"


def main():
    results = {
        "epoch_ledger": check(Path("lineage/epoch_ledger.json"), "epochs"),
        "module_registry": check(Path("lineage/module_registry.json"), "modules"),
        "poc_registry": check(Path("lineage/poc_registry.json"), "pocs"),
    }

    for name, status in results.items():
        print(f"[Integrity] {name}: {status}")

    if all(v == "OK" for v in results.values()):
        print("[Integrity] Root Build integrity baseline: OK")
        return 0
    else:
        print("[Integrity] Root Build integrity baseline: ATTENTION REQUIRED")
        return 4


if __name__ == "__main__":
    sys.exit(main())
