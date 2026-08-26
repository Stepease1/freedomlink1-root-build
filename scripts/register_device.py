import json
import sys
from pathlib import Path

device_id = sys.argv[1]
hw_hash = sys.argv[2]

registry_path = Path("lineage/device_registry.json")

if registry_path.exists():
    with registry_path.open() as f:
        registry = json.load(f)
else:
    registry = {
        "project": "Freedomlink1",
        "version": "1.0.0",
        "registry_type": "device",
        "devices": []
    }

registry["devices"].append({
    "id": device_id,
    "hardware_hash": hw_hash,
    "status": "internal-pilot"
})

with registry_path.open("w") as f:
    json.dump(registry, f, indent=2)

print(f"Registered device {device_id} in {registry_path}")
