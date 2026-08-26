#!/usr/bin/env python3
"""Generate a simple hardware identity hash.
This script is intentionally conservative and only uses non-sensitive system facts.
"""
import hashlib
import json
import platform
import uuid

def main():
    info = {
        "node": platform.node(),
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_build": platform.python_build(),
        "uuid": str(uuid.getnode())
    }
    s = json.dumps(info, sort_keys=True).encode('utf-8')
    h = hashlib.sha256(s).hexdigest()
    print(h)

if __name__ == '__main__':
    main()
