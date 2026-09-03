#!/usr/bin/env python3
"""Build the Epoch 2 SHA-256 manifest for sovereign artifacts."""

import hashlib
import json
from pathlib import Path


FILES = [
    "docs/constitution.html",
    "lineage/epoch_ledger.json",
    "lineage/module_registry.json",
    "lineage/poc_registry.json",
    "governance/identity_manifest.json",
    "governance/continuity_protocol.md",
    "governance/recovery_plan.md",
]


def main() -> None:
    manifest = {}
    for file_name in FILES:
        path = Path(file_name)
        if not path.is_file():
            raise FileNotFoundError(file_name)
        manifest[file_name] = hashlib.sha256(path.read_bytes()).hexdigest()

    payload = json.dumps(manifest, indent=2) + "\n"
    Path("hash_manifest.json").write_text(payload, encoding="utf-8")
    Path("artifacts/hash-manifest.json").write_text(payload, encoding="utf-8")
    print("[Manifest] Hash manifest finalized.")


if __name__ == "__main__":
    main()