#!/usr/bin/env python3
"""Build a deterministic Merkle root from the current hash manifest."""

import hashlib
import json
import sys
from pathlib import Path


def merkle_root(hashes: list[str]) -> str:
    if not hashes:
        raise ValueError("manifest contains no hashes")
    level = hashes[:]
    while len(level) > 1:
        next_level = []
        for index in range(0, len(level), 2):
            pair = level[index:index + 2]
            if len(pair) == 1:
                pair.append(pair[0])
            next_level.append(hashlib.sha256("".join(pair).encode("utf-8")).hexdigest())
        level = next_level
    return level[0]


def main() -> int:
    manifest_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("hash_manifest.json")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("merkle_root.txt")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = manifest.get("files", manifest)
    root = merkle_root([entries[name] for name in sorted(entries)])
    output_path.write_text(root + "\n", encoding="utf-8")
    print(f"[Merkle] Root generated: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
