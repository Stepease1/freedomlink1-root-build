# Freedomlink1 Installer (Genesis Internal Pilot)

This installer suite bootstraps a Freedomlink1 internal pilot node, CLI, and verification environment with a single command.

## Quick start

```bash
curl -fsSL https://raw.githubusercontent.com/Freedomlink1/root-build/main/install/install.sh | bash
```

## What the installer does

- Installs the **Freedomlink1 CLI**
- Verifies Root Build artifacts (hashes, Merkle root, sovereign signature)
- Registers the device in the **Device Registry**
- Installs and starts a **Freedomlink1 node**
- Runs the **POC verification suite**

## Scripts

- `install/install.sh` — main entrypoint
- `install/install_cli.sh` — CLI installer
- `install/verify.sh` — Root Build verification
- `install/register_device.sh` — device sovereignty registration
- `install/install_node.sh` — node installation and startup
- `install/run_poc_tests.sh` — POC verification runner

## Lineage integration
Installer actions update:

- `lineage/device_registry.json`
- `lineage/poc_registry.json` (via tests)
- `lineage/module_registry.json` (indirectly, via promotion workflows)

This makes every installation auditable and part of the Freedomlink1 sovereign lineage.
