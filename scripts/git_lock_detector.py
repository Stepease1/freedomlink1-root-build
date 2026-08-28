#!/usr/bin/env python3
import os
from pathlib import Path

lock = Path(".git/index.lock")

if lock.exists():
    print("[Git] LOCK DETECTED: .git/index.lock")
    print("[Git] Delete it to continue.")
else:
    print("[Git] No lock present. Git is clear.")
