#!/bin/bash
set -e

echo "[Node] Installing Freedomlink1 node..."

NODE_DIR="$HOME/freedomlink1-node"
mkdir -p "$NODE_DIR"

echo "[Node] Downloading node binary..."
curl -fsSL https://raw.githubusercontent.com/Freedomlink1/root-build/main/bin/freedomlink1-node -o "$NODE_DIR/freedomlink1-node"
chmod +x "$NODE_DIR/freedomlink1-node"

echo "[Node] Downloading config..."
curl -fsSL https://raw.githubusercontent.com/Freedomlink1/root-build/main/config/genesis.json -o "$NODE_DIR/genesis.json"
curl -fsSL https://raw.githubusercontent.com/Freedomlink1/root-build/main/config/node-config.toml -o "$NODE_DIR/node-config.toml"

echo "[Node] Starting node in background..."
nohup "$NODE_DIR/freedomlink1-node" --config "$NODE_DIR/node-config.toml" > "$NODE_DIR/node.log" 2>&1 &

echo "[Node] Node started. Logs: $NODE_DIR/node.log"
