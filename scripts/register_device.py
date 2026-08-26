#!/usr/bin/env python3
"""Register a device into lineage/device_registry.json
Usage: register_device.py DEVICE_ID HW_HASH
"""
import sys
import json
import os
from datetime import datetime


def main():
    if len(sys.argv) < 3:
        print("Usage: register_device.py DEVICE_ID HW_HASH", file=sys.stderr)
        sys.exit(2)
    device_id = sys.argv[1]
    hw_hash = sys.argv[2]

    registry_dir = os.path.join(os.getcwd(), 'lineage')
    os.makedirs(registry_dir, exist_ok=True)
    registry_file = os.path.join(registry_dir, 'device_registry.json')

    entry = {
        "device_id": device_id,
        "hw_hash": hw_hash,
        "registered_at": datetime.utcnow().isoformat() + 'Z'
    }

    if os.path.exists(registry_file):
        with open(registry_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception:
                data = {"devices": []}
    else:
        data = {"devices": []}

    data.setdefault('devices', []).append(entry)

    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, sort_keys=True)

    print(json.dumps(entry))


if __name__ == '__main__':
    main()
