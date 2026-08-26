import sys
import json
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

merkle_root_path = Path(sys.argv[1])
proof_master_path = Path(sys.argv[2])

with merkle_root_path.open() as f:
    merkle_root = f.read().strip()

with proof_master_path.open() as f:
    proof_master = json.load(f)

signature_hex = proof_master["sovereign_signature"]
public_key_pem = proof_master["steward_public_key"]

signature = bytes.fromhex(signature_hex)
public_key = serialization.load_pem_public_key(public_key_pem.encode("utf-8"))

public_key.verify(
    signature,
    merkle_root.encode("utf-8"),
    padding.PKCS1v15(),
    hashes.SHA256()
)

print("Sovereign signature verification: PASS")
