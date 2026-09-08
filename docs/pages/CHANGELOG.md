---
title: Freedomlink1 CHANGELOG - Root Build v1.2
layout: default
permalink: /CHANGELOG
---

## Freedomlink1 CHANGELOG - Root Build v1.2 (Epoch 2)

**Date:** March 8, 2026  
**Build Tag:** `freedomlink1-root-2026.03.08`  
**Commit:** `7c40e48e73878fc9f6b0bf3a48a03609bb5e438a`  
**Merkle Root:** `ec8ba39cf291dd95e02004f50bed946019bf1116f49e0fabf1ba3bb9f57bcb41`  
**Status:** Sovereign State Anchored

## Summary

Root Build v1.2 introduces the first fully sovereign, lineage-anchored governance cycle for Freedomlink1.

This release finalizes:

- the Epoch 2 ledger block
- the canonical hash manifest
- the Merkle leaf and Merkle root
- the sovereign signature block
- the GitHub Pages release page

It also integrates the complete Rootstone-I hardware specification into the governance organism.

## Added

### Governance and Protocol

- Steward initialization flow
- Decade Seal Cycle execution
- Audit logging for all admin seed actions
- Health endpoint with Postgres and Redis readiness checks
- Lineage-anchored governance artifacts
- Sovereign signature block for Epoch 2

### CI and Automation

- Full CI pipeline for deterministic governance testing
- Ephemeral Postgres and Redis startup
- Prisma migrations
- Agent build and start
- Steward flow simulation
- Decade Seal execution
- Artifact upload: `agent.log`, `agent.pid`
- Local automation script: `run_local_integration.sh`

### Hardware and Rootstone-I

- Electrical specification: power rails and clock domains
- RTL module hierarchy: SC0, SE0, AE0, EV0, CSR0, FM0, IE0, CT0, BI0
- Sovereign Board bus architecture: SBUS, IBUS, LBUS, Sensor Bus
- Ceremony Time Engine integration
- Seal Engine and Attestation Engine pathways
- Fuse Matrix invariants

### Lineage and Sovereign Anchoring

- Epoch 2 ledger entry
- Hash manifest entry
- Merkle leaf for Epoch 2
- Merkle root regeneration
- Sovereign signature block
- GitHub Pages release page

## Changed

- Updated lineage structure to support multi-epoch Merkle tree
- Updated governance primitives to reference Rootstone-I
- Updated CI workflow to include seal and attestation simulation
- Updated documentation to reflect sovereign hardware integration
- Updated Device System Architecture Codex references

## Fixed

- Corrected admin seed gating under `NODE_ENV=test|development`
- Ensured audit logging consistency across seed routes
- Resolved readiness race conditions in local integration script
- Stabilized CI artifact upload paths

## Removed

- Legacy non-sovereign initialization flows
- Deprecated seal simulation harness
- Old hardware placeholder documentation

## Sovereign Anchoring Artifacts

- `epoch_ledger.json` - Epoch 2 block
- `hash_manifest.json` - canonical hash entry
- `merkle_leaf_epoch_2.json`
- `merkle_root.txt`
- `sovereign_signature_epoch_2.json`
- `release_v1_2.md`

## Institutional Status

Root Build v1.2 is:

- **anchored**
- **sealed**
- **signed**
- **validated**
- **published**

Epoch 2 is now part of the permanent lineage of Freedomlink1.
