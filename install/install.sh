#!/bin/bash
set -e

echo "=== Freedomlink1 Installer (Genesis Epoch) ==="

# Step 1 — Install CLI
bash "$(dirname "$0")/install_cli.sh"

# Step 2 — Verify artifacts
bash "$(dirname "$0")/verify.sh"

# Step 3 — Register device
bash "$(dirname "$0")/register_device.sh"

# Step 4 — Install node binaries (placeholder)
bash "$(dirname "$0")/install_node.sh"

# Step 5 — Run POC tests
bash "$(dirname "$0")/run_poc_tests.sh"

echo "=== Installation Complete ==="
echo "Your device is now part of the Freedomlink1 internal pilot."
