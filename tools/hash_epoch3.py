#!/usr/bin/env python3
"""
tools/hash_epoch3.py

Compute the canonical Merkle root for Epoch 3 governance and lineage artifacts.
This is designed to be run from the repo root.
"""

import hashlib
import os
from pathlib import Path

# Files explicitly included in the Epoch 3 Merkle set
EPOCH3_FILES = [
    "lineage/ledger/epoch_3.json",
    "governance/epoch/epoch_3.manifest",
    "governance/modules/epoch3.json",
    "docs/governance/Epoch_3_Proclamation.md",
    "lineage/anchors/epoch_3_anchor.json",
    "docs/governance/Epoch_3_Roadmap.md",
    "docs/governance/Epoch_3_Module_Activation_Ceremony.md",
    "docs/governance/Epoch_3_Lineage_Advancement_Protocol.md",
    "docs/governance/Epoch_3_Governance_Charter_Addendum.md",
    "docs/governance/Epoch_3_Continuity_Doctrine_Extension.md",
    "docs/governance/Epoch_3_Sentinel_Activation_Protocol.md",
    "docs/governance/Epoch_3_Rights_and_Duties_Expansion.md",
    "docs/governance/Epoch_3_Institutional_Proclamation_II.md",
    "docs/governance/index.json",
    "governance/modules/core.json",
]


def sha256_bytes(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def sha256_file(path: Path) -> bytes:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.digest()


def merkle_root(leaves: list[bytes]) -> bytes:
    if not leaves:
        return sha256_bytes(b"")  # empty tree sentinel

    level = leaves[:]
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            next_level.append(sha256_bytes(left + right))
        level = next_level
    return level[0]


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    print(f"Repo root: {repo_root}")

    # Ensure deterministic ordering
    files = sorted(EPOCH3_FILES)

    leaves: list[bytes] = []
    for rel in files:
        path = repo_root / rel
        if not path.exists():
            raise FileNotFoundError(f"Missing Epoch 3 artifact: {rel}")
        digest = sha256_file(path)
        leaves.append(digest)
        print(f"{rel}: {digest.hex()}")

    root = merkle_root(leaves)
    print("\nEpoch 3 Merkle root:")
    print(root.hex())


if __name__ == "__main__":
    main()
