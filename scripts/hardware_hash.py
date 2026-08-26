import hashlib
import platform
import uuid

def collect_fingerprint():
    parts = [
        platform.system(),
        platform.release(),
        platform.machine(),
        platform.processor(),
        str(uuid.getnode())
    ]
    return "|".join(parts)

fp = collect_fingerprint()
hw_hash = hashlib.sha256(fp.encode("utf-8")).hexdigest()
print(hw_hash)
