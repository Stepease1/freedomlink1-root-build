# Blockchain Anchor

## Purpose
This document establishes the cryptographic anchor of the Freedomlink system to blockchain networks, ensuring immutable verification and long-term proof of custody.

## Hash Registration
The root hash of this archive is registered on the following blockchain networks:

- **Ethereum Mainnet**: Contract address with merkle root commitment
- **Polygon**: Secondary anchor for redundancy and distribution
- **Arweave**: Permanent archive with full document storage

## Verification Process
1. Compute the master hash from the omni-proof structure
2. Cross-reference against blockchain transaction logs
3. Verify cryptographic signatures from authorized signers
4. Confirm timestamp alignment with blockchain blocks

## Transaction Records
All blockchain transactions related to this archive are indexed in `artifacts/hash-manifest.json` with:
- Transaction hashes
- Block numbers and timestamps
- Network identifiers
- Verification status
