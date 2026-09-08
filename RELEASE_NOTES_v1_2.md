# Freedomlink1 - Root Build v1.2 (Epoch 2)

**Build Tag:** `freedomlink1-root-2026.03.08`  
**Commit:** `7c40e48e73878fc9f6b0bf3a48a03609bb5e438a`  
**Merkle Root:** `ec8ba39cf291dd95e02004f50bed946019bf1116f49e0fabf1ba3bb9f57bcb41`  
**Status:** Sovereign State Anchored  
**Prepared by:** Joshua  
**Date:** March 8, 2026

## Overview

Freedomlink1 Root Build v1.2 is the second sovereign epoch of the Freedomlink1 governance organism.

This release finalizes the complete anchoring cycle:

- Epoch 2 ledger block
- Hash manifest
- Merkle leaf and Merkle root
- Sovereign signature block
- GitHub Pages release page
- Public CHANGELOG

This is the first fully **sovereign-anchored** release of Freedomlink1.

## Highlights

### Governance

- Steward initialization flow
- Decade Seal Cycle execution
- Lineage-anchored governance artifacts
- Audit logging for all admin seed actions
- Health endpoint with Postgres and Redis readiness checks

### CI Pipeline

- Ephemeral Postgres and Redis
- Prisma migrations
- Agent build and start
- Steward flow simulation
- Decade Seal execution
- Artifact upload: `agent.log`, `agent.pid`

### Local Automation

`run_local_integration.sh` provides:

- install
- migrate
- build
- start
- readiness wait
- simulation
- log collection

## Rootstone-I Integration

Rootstone-I is the sovereign processor for Freedomlink1's Device and Civic Nodes.

### Electrical Specs

- VCORE 1.2V
- VENCLAVE 1.0V
- VIO 3.3V
- VSEAL 1.2V
- VSENSE 3.3V

### Clock Domains

- 800 MHz main core
- 600 MHz enclave
- 400 MHz seal engine
- 300 MHz attestation engine
- 50 MHz fuse matrix

### RTL Modules

- SC0 Sovereign Core
- SE0 Seal Engine
- AE0 Attestation Engine
- EV0 Enclave Vault
- CSR0 Controller
- FM0 Fuse Matrix
- IE0 Identity Engine
- CT0 Ceremony Time Engine
- BI0 Bus Interface Engine

## Artifacts Included

- `Freedomlink1_RootstoneI_Electrical_RTL_Spec.md`
- `Freedomlink1_Device_Hardware_Reference_Manual.md`
- `Freedomlink1_Ceremony_Engine_Specification.md`
- `Freedomlink1_Seal_Logic_Cryptographic_Canon.md`
- `agent.log`
- `agent.pid`

## Lineage Anchoring Artifacts

- `epoch_ledger.json`
- `hash_manifest.json`
- `merkle_leaf_epoch_2.json`
- `merkle_root.txt`
- `sovereign_signature_epoch_2.json`
- `release_v1_2.md`
- `CHANGELOG.md`

## Required CI Secrets

- `SAASPILOT_API_KEY`
- `TEST_API_KEY`
- `DATABASE_URL`
- `REDIS_URL`
- `NEXT_PUBLIC_AGENT_PUBLIC_BASE_URL`
- `NEXT_PUBLIC_AGENT_STEWARD_BASE_URL`
- Optional: `SENTRY_DSN`, `CI_SSH_KEY`

## Local Run Instructions

### Manual Run

```bash
cd agent
npm ci
export NODE_ENV=test
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/freedomlink1_test"
export REDIS_URL="redis://localhost:6379"
export TEST_API_KEY="your_test_api_key"
export PORT=8080
npx prisma migrate deploy || npx prisma migrate reset --force
npm run build
nohup npm start > agent.log 2>&1 & echo $! > agent.pid
curl -sSf http://localhost:8080/health | jq .
TEST_AGENT_BASE_URL=http://localhost:8080 TEST_API_KEY=$TEST_API_KEY node test/simulate_steward_flow.js
```

Root Build v1.2 is:

- **anchored**
- **sealed**
- **signed**
- **validated**
- **published**

Epoch 2 is now part of the permanent lineage of Freedomlink1.
