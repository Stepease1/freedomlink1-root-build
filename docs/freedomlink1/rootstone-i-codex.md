---
title: Freedomlink1 Rootstone-I Hardware Codex
layout: default
permalink: /freedomlink1/rootstone-i-codex
---

# Freedomlink1 Rootstone-I Hardware Codex
## Sovereign Processor, Ceremony Engine, and Lineage Root

### Overview
Rootstone-I is the canonical sovereign processor for Freedomlink1. It is the hardware root of trust for ceremony, seal formation, attestation, and lineage enforcement.

Rootstone-I is defined by:
- a ceremony-aligned microarchitecture  
- immutable fuse and enclave subsystems  
- a CSR register map for identity, seal, epoch, cycle, and security state  
- a bus architecture that prioritizes seal operations and lineage integrity

---

## Core subsystems

### SC0 — Sovereign Core
- Pipeline stages: FETCH → DECODE → PREIMAGE → ENCLAVE CALL → SIGN → WRITEBACK
- Executes seal, attestation, identity, ceremony, CSR, and fuse instructions

### SE0 — Seal Engine
- Executes `SEAL.BLOCK`, `SEAL.DEVICE`, `SEAL.EPOCH`, `SEAL.CYCLE`, `SEAL.CEREMONY`, `SEAL.ATTEST`
- Handles preimage load, SHA-256 hashing, signature generation, seal formatting, and counter increment

### AE0 — Attestation Engine
- Constructs identity and state bundles  
- Hashes and signs attestation artifacts  
- Outputs canonical attestation bundles

### EV0 — Enclave Vault
- Stores private keys, identity keys, seal counters, ceremony state, firmware lineage, and mask lineage
- No external read/write, no DMA, no debug, no bypass

### CSR0 — CSR Controller
- Manages sovereign registers for identity, seals, attestation, epoch/cycle, and security

### FM0 — Fuse Matrix
- Enforces irreversible security invariants:
  - identity lock  
  - firmware lock  
  - mask lock  
  - seal counter lock  
  - debug disable  
  - tamper lock  
  - consecration  
  - retirement

### IE0 — Identity Engine
- Manages Stone identity, Device identity, certificate hashes, and lineage anchors

### CT0 — Ceremony Time Engine
- Maintains `CSR_EPOCH`, `CSR_CYCLE`, and ceremony time state  
- Updates on `SEAL.EPOCH` and `SEAL.CYCLE`

### BI0 — Bus Interface Engine
- Arbitrates SBUS, IBUS, LBUS, Sensor Bus  
- Prioritizes ceremony-aligned operations and seal state propagation

---

## CSR register map

### Identity
- `CSR_IDENTITY` — Stone identity hash  
- `CSR_DEVICE_ID` — Device identity hash  
- `CSR_CERT_HASH` — certificate hash  
- `CSR_FIRMWARE_HASH` — firmware lineage hash

### Seals
- `CSR_SEAL_COUNTER` — monotonic seal counter  
- `CSR_SEAL_PREIMAGE` — preimage buffer  
- `CSR_SEAL_OUTPUT` — seal output buffer  
- `CSR_SEAL_TYPE` — seal type selector

### Attestation
- `CSR_ATTEST_TRIGGER` — trigger attestation  
- `CSR_ATTEST_STATE` — attestation state  
- `CSR_ATTEST_OUTPUT` — attestation bundle

### Epoch / Cycle
- `CSR_EPOCH` — current epoch  
- `CSR_CYCLE` — current cycle  
- `CSR_TIME_STATE` — ceremony time state

### Security
- `CSR_TAMPER_STATE` — tamper detection  
- `CSR_FUSE_STATE` — fuse matrix state  
- `CSR_ENCLAVE_STATE` — enclave integrity  
- `CSR_BOOT_STATE` — secure boot status

---

## Fuse matrix

- `FUSE_IDENTITY_LOCK`  
- `FUSE_DEVICE_ID_LOCK`  
- `FUSE_FW_LOCK`  
- `FUSE_FW_LINEAGE_LOCK`  
- `FUSE_MASK_LOCK`  
- `FUSE_MASK_LINEAGE_LOCK`  
- `FUSE_SEAL_COUNTER_LOCK`  
- `FUSE_SEAL_PRIVKEY_LOCK`  
- `FUSE_DEBUG_DISABLE`  
- `FUSE_TAMPER_LOCK`  
- `FUSE_ENCLAVE_LOCK`  
- `FUSE_CONSECRATION`  
- `FUSE_RETIREMENT`

All fuses are blown only under ceremony control and are irreversible.

---

## Bus architecture

### SBUS
- Ceremony and seal operations
- Highest priority bus for Rootstone-I

### IBUS
- Identity and attestation data
- Secondary priority for identity flows

### LBUS
- Lineage and artifact transfer
- Ensures consistent Merkle Forest state

### Sensor Bus
- Tamper, power, and environmental sensors
- Monitored by the Ceremony Time Engine

---

## Ceremony alignment

Rootstone-I is the canonical hardware root of trust for:
- Root Protocol Canon  
- Root Ledger Specification  
- Seal Logic & Cryptographic Canon  
- Ceremony Engine Specification

The hardware architecture is explicitly aligned to the institutional lineage model and the Root Build’s ceremonial structure.
