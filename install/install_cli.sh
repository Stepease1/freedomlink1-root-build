#!/bin/bash
set -e

echo "[CLI] Downloading Freedomlink1 CLI..."
curl -fsSL https://raw.githubusercontent.com/Freedomlink1/root-build/main/bin/freedomlink1-cli -o /usr/local/bin/freedomlink1 || {
    echo "Failed to download CLI to /usr/local/bin; will write to ./bin/freedomlink1 instead."
    mkdir -p "$(pwd)/bin"
    curl -fsSL https://raw.githubusercontent.com/Freedomlink1/root-build/main/bin/freedomlink1-cli -o "$(pwd)/bin/freedomlink1"
    chmod +x "$(pwd)/bin/freedomlink1"
    echo "[CLI] Installed at $(pwd)/bin/freedomlink1"
    exit 0
}

chmod +x /usr/local/bin/freedomlink1

echo "[CLI] Installed at /usr/local/bin/freedomlink1"
