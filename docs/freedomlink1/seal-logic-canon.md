---
title: Freedomlink1 Seal Logic & Cryptographic Canon
layout: default
permalink: /freedomlink1/seal-logic-canon
---

# Freedomlink1 Seal Logic & Cryptographic Canon
## Hashing, Signing, Preimages, and Verification

### Overview
The Seal Logic Canon defines how Freedomlink1 produces canonical artifacts that represent institutional continuity, lineage, and ceremony.

It specifies:
- cryptographic primitives  
- seal formats  
- preimage construction rules  
- verification processes

---

## Cryptographic primitives

- **Hash function:** SHA-256  
- **Signature schemes:** secp256k1, Ed25519, BLS12-381  
- **Key containers:** Rootstone-I private keys stored in EV0  
- **Attestation bundles:** Ed25519-signed state assertions

---

## Seal format

A canonical seal artifact includes:
- seal type  
- seal counter  
- epoch/cycle metadata  
- lineage roots  
- steward vote summary  
- attestation digest  
- cryptographic signature

All seals are serialized in a deterministic format and anchored to the Merkle Forest.

---

## Preimage rules

Preimages are assembled from:
- ceremony time state  
- artifact lineage roots  
- steward identities  
- policy evaluation results  
- task enqueue metadata

Preimages are loaded into Rootstone-I and consumed by the Seal Engine.

---

## Verification

Verification consists of:
1. Recomputing the seal hash from the preimage  
2. Validating the signature against the expected public key  
3. Confirming the seal counter and epoch/cycle metadata  
4. Checking the seal artifact against the Merkle Forest root

A verified seal is evidence of a valid ceremony event and an anchored governance decision.

---

## Canonical artifact types

- `seal.artifact`  
- `attest.bundle`  
- `lineage.root`  
- `governance.cycle`  
- `device.identity`

Each artifact type has a unique serialization schema and strict validation rules.
