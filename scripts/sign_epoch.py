#!/usr/bin/env python3
"""Build Epoch 2 integrity artifacts and record the renewal event."""

import subprocess
import sys


steps = [
    [sys.executable, "scripts/build_hash_manifest.py"],
    [sys.executable, "scripts/build_merkle_tree.py"],
    [sys.executable, "scripts/update_logbook.py", "Epoch 2 Sovereign Signature"],
]

for step in steps:
    print(f"[Sign] {' '.join(step)}")
    subprocess.run(step, check=True)

print("[Sign] Epoch 2 sovereign signature complete.")