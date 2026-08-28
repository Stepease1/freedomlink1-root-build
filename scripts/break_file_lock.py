#!/usr/bin/env python3
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: break_file_lock.py <path>")
    sys.exit(2)

path = Path(sys.argv[1])

try:
    data = path.read_text(encoding="utf-8")
    path.write_text(data, encoding="utf-8")
    print(f"[LockBreaker] Rewrote {path} to break Windows file lock.")
except Exception as e:
    print(f"[LockBreaker] Failed: {e}")
    sys.exit(1)
