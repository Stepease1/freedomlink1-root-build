# Epoch Advancement Protocol
**Freedomlink1 — Sovereign Digital Institution**  
**Version:** 1.0  
**Epoch:** 2 (Root Build v1.2)  
**Prepared by:** Joshua W. Blaz

## 1. Purpose
The Epoch Advancement Protocol ("Protocol") defines the formal process by which Freedomlink1 transitions from one epoch to the next. It ensures:

- continuity of sovereign lineage
- integrity of governance artifacts
- correctness of Merkle root evolution
- proper sealing of epoch boundaries
- activation of new governance modules
- preservation of institutional identity

Epoch advancement is a constitutional act and must follow this Protocol exactly.

## 2. Definitions

### 2.1 Epoch
A discrete governance period representing a stable state of the Institution.

### 2.2 Lineage Seal
A cryptographic seal binding the final Merkle root of the epoch to the sovereign signature.

### 2.3 Advancement Trigger
An authorized action that initiates epoch transition.

### 2.4 Sovereign Signature
A cryptographic signature produced by the Founder's key, used to validate lineage.

### 2.5 Merkle Root
A cryptographic digest representing the complete governance corpus.

## 3. Authority to Advance Epochs
Epoch advancement may only be initiated by:

### 3.1 Founder (Ceremonial Steward)
The Founder holds sovereign authority to advance epochs.

### 3.2 Governance Modules (with consensus)
Modules may recommend advancement but cannot execute it without Founder authorization.

### 3.3 Sentinel Recommendation
Sentinels may recommend advancement when drift, corruption, or major governance changes occur.

## 4. Advancement Triggers
Epoch advancement may be triggered by:

### 4.1 Major Governance Additions
New constitutional artifacts, charters, codices, or protocols.

### 4.2 Structural Governance Changes
Changes to module architecture, lineage structure, or sovereign rights.

### 4.3 Hardware Trust Updates
Changes to Rootstone-I or other hardware trust anchors.

### 4.4 Sentinel Alerts
Critical alerts indicating drift or governance instability.

### 4.5 Founder Proclamation
A direct sovereign proclamation by the Founder.

## 5. Advancement Sequence
Epoch advancement follows this exact sequence:

### 5.1 Corpus Finalization
All governance artifacts for the current epoch must be:

- indexed
- hashed
- registered
- validated

### 5.2 Merkle Root Generation
The governance pipeline computes the Merkle root for the finalized corpus.

### 5.3 Sovereign Signature Generation
The Founder signs the Merkle root using the sovereign private key.

### 5.4 Lineage Seal Creation
A lineage seal is created containing:

- epoch number
- Merkle root
- sovereign signature
- timestamp
- module state

### 5.5 Seal Registration
The lineage seal is stored in:

- `/lineage/seals/epoch_<n>.json`
- governance manifest
- module registry

### 5.6 Epoch Increment
The epoch counter is incremented:

```text
epoch = epoch + 1
```

### 5.7 Module Activation
New governance modules for the next epoch are activated.

### 5.8 Sentinel Reset
Sentinels reset their drift-detection baselines.

## 6. Lineage Seal Format
A lineage seal must contain:

```json
{
  "epoch": <integer>,
  "merkle_root": "<sha256>",
  "sovereign_signature": "<signature>",
  "timestamp": "<iso8601>",
  "modules": {
    "active": [...],
    "inactive": [...]
  }
}
```

This seal is immutable once created.

## 7. Verification Requirements
Before an epoch can advance:

### 7.1 Merkle Root Verification
The computed root must match the governance corpus.

### 7.2 Signature Verification
The sovereign signature must match the Merkle root.

### 7.3 Module Integrity Verification
All modules must pass integrity checks.

### 7.4 Manifest Consistency
The governance manifest must match the corpus.

### 7.5 Sentinel Clearance
Sentinels must report no critical anomalies.

## 8. Failure Conditions
Epoch advancement must halt if:

- signature verification fails
- Merkle root mismatch occurs
- module integrity fails
- sentinel reports critical drift
- lineage seal cannot be generated

These failures must be logged and escalated.

## 9. Founder Responsibilities
The Founder must:

- verify corpus completeness
- generate sovereign signature
- authorize advancement
- seal lineage
- activate next-epoch modules
- publish advancement proclamation

## 10. Sentinel Responsibilities
Sentinels must:

- monitor advancement sequence
- verify module activation
- update drift baselines
- confirm lineage seal integrity

## 11. Module Responsibilities
Modules must:

- validate their own state
- confirm readiness for next epoch
- register updated configuration
- report anomalies

## 12. Advancement Proclamation
Upon successful advancement, the Founder issues a proclamation containing:

- new epoch number
- lineage seal reference
- governance changes summary
- module activation summary

This proclamation becomes part of the governance corpus.

## 13. Signatures

### Institution (Freedomlink1):
**Joshua W. Blaz**  
Founder & Ceremonial Steward  
*Signature:* `SIG(<sovereign-signature>)`  
*Date:* `<timestamp>`

### Module Authority:
**Governance Module:** __________________________  
**Signature:** __________________________  
**Date:** __________________________
