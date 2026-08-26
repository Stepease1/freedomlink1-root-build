---
title: Freedomlink1 Device System Architecture Codex
layout: default
permalink: /freedomlink1/device-architecture-codex
---

# Freedomlink1 Device System Architecture Codex
## Sovereign Board, Device Identity, and Lineage Integration

### Overview
The Device System Architecture Codex defines how hardware, firmware, protocol, and governance align within Freedomlink1.

This codex describes:
- the Sovereign Board architecture  
- Rootstone-I integration  
- lineage partitioning  
- identity and attestation flows  
- security and boot state

---

## System components

### Sovereign Board
The Sovereign Board hosts:
- Rootstone-I processor  
- secure enclave vaults  
- ceremony sensors  
- lineage storage partitions  
- communication buses (SBUS, IBUS, LBUS, Sensor Bus)

### Device identity
Device identity is derived from:
- Stone identity  
- Device identity  
- certificate hashes  
- firmware lineage

Identity is anchored in Rootstone-I and recorded in the Merkle Forest.

### Lineage partition
The lineage partition stores:
- root hashes  
- ceremony artifacts  
- device lifecycle records  
- firmware lineage proofs

This partition is immutable and only updated via sealed ceremony events.

---

## Security model

### Secure boot
- Rootstone-I enforces secure boot  
- Boot state is recorded in `CSR_BOOT_STATE`  
- Firmware lineage is verified before execution

### Tamper detection
- Sensor Bus monitors environmental and physical state  
- Tamper events update `CSR_TAMPER_STATE`  
- Tamper lock can trigger ceremony health state changes

### Enclave integrity
- `CSR_ENCLAVE_STATE` enforces enclave policy  
- Private keys and seals are protected inside EV0  
- No debug or DMA access to enclave secrets

---

## Protocol alignment

Freedomlink1 protocol documents reference the device architecture for:
- root artifact creation  
- ceremony engine triggers  
- attestation bundles  
- hardware-backed lineage

The device is designed to ensure that governance actions are always anchored in hardware truth.
