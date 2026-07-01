# Verification Guide

This document provides comprehensive instructions for verifying the integrity, authenticity, and lineage of the Freedomlink archive.

## Quick Start

```bash
# Verify the master hash
python scripts/root-comparison.py

# Verify all signatures
python scripts/signature-verification.py

# Validate merkle tree structure
python scripts/merkle-tree.py --verify
```

## Verification Layers

### 1. Cryptographic Hash Verification
- **Master Hash**: Located in `artifacts/omni-proof-master.json`
- **Hash Computation**: See `scripts/hashing.py`
- **Verification**: Compare computed hash against blockchain anchor and timestamp proofs

```bash
python scripts/hashing.py --file artifacts/hash-manifest.json
```

### 2. Signature Verification
All governance documents and critical artifacts are cryptographically signed by authorized contributors.

- **Contributor Keys**: See `lineage/contributor-registry.md`
- **Verification Tool**: `scripts/signature-verification.py`

```bash
python scripts/signature-verification.py --verify-all
```

### 3. Blockchain Anchor Verification
Cross-reference the root hash against blockchain networks:

1. Open [Ethereum Transaction Explorer](https://etherscan.io/)
2. Search for contract address in `artifacts/hash-manifest.json`
3. Verify transaction hash and timestamp
4. Confirm merkle root commitment

See `anchors/blockchain-anchor.md` for detailed blockchain integration.

### 4. Timestamp Authority Verification
Validate temporal proof using RFC 3161 standards:

```bash
python scripts/signature-verification.py --verify-timestamp
```

See `anchors/timestamp-proof.md` for timestamp authority details.

### 5. Lineage Verification
Trace the complete chain of custody through epochs and ceremonies:

- **Epoch Ledger**: `lineage/epoch-ledger.md`
- **Ceremonies**: `lineage/ceremonies.md`
- **Device Registry**: `lineage/device-registry.md`
- **Contributor Registry**: `lineage/contributor-registry.md`

## Manual Verification Steps

### Step 1: Hash Consistency
```bash
# Compute the canonical hash
python scripts/canonicalization.py > canonical.txt
python scripts/hashing.py --file canonical.txt > computed_hash.txt

# Compare against artifacts
cat artifacts/hash-manifest.json | grep "master_hash"
```

### Step 2: Merkle Tree Validation
```bash
python scripts/merkle-tree.py --verify --verbose
```

### Step 3: Chain of Custody
Review the following in order:
1. `lineage/device-registry.md` - Hardware that handled the data
2. `lineage/ceremonies.md` - Events and signing ceremonies
3. `lineage/contributor-registry.md` - All contributors and their roles
4. `governance/permissions-matrix.md` - Authorization records

### Step 4: Governance Compliance
Verify that all modifications comply with governance:
- `governance/charter.md` - Core principles
- `governance/amendment-protocol.md` - Process for changes
- `governance/permissions-matrix.md` - Who can do what

## Verification Results

All verification scripts produce detailed reports:

```bash
# Full verification report
python scripts/root-comparison.py --report > verification-report.txt
```

## Dispute Resolution

If verification fails, consult:
- `governance/oversight-appeals-sanctions.md` - Dispute procedures
- Contact listed contributors in `lineage/contributor-registry.md`

## Standards Compliance

This verification process conforms to:
- RFC 3161 (Time-Stamp Protocol)
- FIPS 186-4 (Digital Signature Standard)
- EIP-191 and EIP-712 (Ethereum signing standards)
- ISO standards for data integrity

## Additional Resources

- [Cryptographic Standards](anchors/external-references.md)
- [Blockchain Integration](anchors/blockchain-anchor.md)
- [Timestamp Proofs](anchors/timestamp-proof.md)
- [Full Index](docs/index.md)
