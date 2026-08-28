#!/usr/bin/env python3
"""Generate a canonical fingerprint for a PEM public key.

Usage: python3 scripts/generate_key_fingerprint.py <public_key.pem>
Outputs SHA-256 hex digest of the public-key DER bytes.
"""

import sys
import hashlib
from pathlib import Path

try:
    from cryptography.hazmat.primitives import serialization
except Exception as e:
    print("[Fingerprint] cryptography package required: pip install cryptography")
    raise


def main(argv):
    if len(argv) < 2:
        print("Usage: generate_key_fingerprint.py <public_key.pem>")
        return 2

    key_path = Path(argv[1])
    if not key_path.exists():
        print(f"[Fingerprint] File not found: {key_path}")
        return 3

    data = key_path.read_bytes()
    try:
        pub = serialization.load_pem_public_key(data)
    except Exception as e:
        print(f"[Fingerprint] Failed to load public key: {e}")
        return 4

    try:
        der = pub.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    except Exception as e:
        print(f"[Fingerprint] Failed to export DER: {e}")
        return 5

    fingerprint = hashlib.sha256(der).hexdigest()
    print(f"[Fingerprint] Sovereign Key Fingerprint: {fingerprint}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
