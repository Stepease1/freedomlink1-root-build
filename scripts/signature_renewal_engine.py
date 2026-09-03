#!/usr/bin/env python3
"""Rebuild the Merkle artifact and record a signature renewal event."""

import subprocess
import sys


steps = [
    [sys.executable, "scripts/build_merkle_tree.py", "hash_manifest.json", "merkle_root.txt"],
    [sys.executable, "scripts/update_logbook.py", "Signature Renewal"],
]

for step in steps:
    print(f"[Renewal] {' '.join(step)}")
    subprocess.run(step, check=True)

print("[Renewal] Sovereign signature renewal complete.")
