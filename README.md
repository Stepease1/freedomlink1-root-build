# Freedomlink

A decentralized, cryptographically-verified governance and record-keeping system with immutable blockchain anchors, timestamp proofs, and transparent verification capabilities.

![Epoch: Genesis](https://img.shields.io/badge/Epoch-Genesis-4af2c5)
![Verification: Open](https://img.shields.io/badge/Verification-Open-5f8cff)
![Governance: Active](https://img.shields.io/badge/Governance-Active-c28bff)
![Root Build v1.0.0](https://img.shields.io/badge/Root_Build-v1.0.0-0b1020)

## 🎯 Core Principles

- **Transparent**: All records are publicly verifiable and permanently archived
- **Decentralized**: Governance through community consensus, not centralized authority
- **Immutable**: Blockchain anchored, cryptographically signed, permanently auditable
- **Verifiable**: Independent verification using published standards and open tooling
- **Accountable**: Complete chain of custody and contributor attribution

## 📚 Key Documents

Start here:
- **[PROCLAMATION.md](PROCLAMATION.md)** - Mission statement and foundational principles
- **[VERIFY.md](VERIFY.md)** - Complete verification guide for cryptographic integrity
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution process and governance requirements
- **[LICENSE](LICENSE)** - MIT License with governance terms
- **[onboarding/WELCOME.md](onboarding/WELCOME.md)** - Welcome and quick start guide

Governance & Policy:
- [governance/charter.md](governance/charter.md) - Core governance charter
- [governance/amendment-protocol.md](governance/amendment-protocol.md) - Change management process
- [governance/permissions-matrix.md](governance/permissions-matrix.md) - Authorization levels
- [governance/oversight-appeals-sanctions.md](governance/oversight-appeals-sanctions.md) - Dispute resolution

## 🔐 Verification

All records are cryptographically verifiable:

```bash
# Quick verification
npm run build
python scripts/hashing.py
python scripts/signature-verification.py --verify-all
python scripts/merkle-tree.py --verify
```

See [VERIFY.md](VERIFY.md) for comprehensive verification procedures.

## 🔗 Blockchain Anchors

Root hash is anchored to multiple blockchains:
- **Ethereum**: Primary anchor with smart contract commitment
- **Polygon**: Secondary redundancy and distribution
- **Arweave**: Permanent document archive

See [anchors/blockchain-anchor.md](anchors/blockchain-anchor.md) for verification details.

## ⏱️ Timestamp Proofs

RFC 3161 compliant timestamp authority integration ensures:
- Cryptographic proof of when records were created
- Multi-authority redundancy
- Alignment with blockchain blocks

See [anchors/timestamp-proof.md](anchors/timestamp-proof.md) for details.

## 📋 Records & Lineage

Complete chain of custody documentation:
- [lineage/contributor-registry.md](lineage/contributor-registry.md) - All contributors and roles
- [lineage/device-registry.md](lineage/device-registry.md) - Hardware handling records
- [lineage/ceremonies.md](lineage/ceremonies.md) - Signing events and milestones
- [lineage/epoch-ledger.md](lineage/epoch-ledger.md) - Temporal markers and epochs

## 🛠️ Technical Stack

- **Language**: TypeScript with strict mode
- **Build**: npm/TypeScript compiler
- **Cryptography**: RFC 3161, RFC 5652, FIPS 186-4 standards
- **Scripts**: Python utilities for verification
- **Verification**: Merkle trees, digital signatures, hash validation

See [onboarding/tech-stack.md](onboarding/tech-stack.md) for full details.

## 🏗️ Project Structure

```
/
├── anchors/              # Blockchain & timestamp proofs
├── artifacts/            # Generated hashes & proofs
├── docs/                 # Complete documentation index
├── governance/           # Policy & charter documents
├── lineage/              # Contributors, devices, ceremonies
├── onboarding/           # Getting started guides
├── scripts/              # Verification & utility scripts
├── src/                  # TypeScript source code
└── visuals/              # Design tokens and glyphs
```

## 📦 Quick Start

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Verify integrity
python scripts/root-comparison.py

# Run verification suite
python scripts/signature-verification.py --verify-all
```

## 🤝 Contributing

We welcome contributions from the community! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to get started
- Contribution process
- Governance requirements
- Technical standards

All contributors are permanently recognized in our registry.

## 📖 Full Documentation

- [docs/index.md](docs/index.md) - Complete documentation index
- [docs/verification.md](docs/verification.md) - Verification procedures
- [docs/epochs.md](docs/epochs.md) - Temporal framework
- [docs/governance.md](docs/governance.md) - Governance overview
- [docs/lineage.md](docs/lineage.md) - Chain of custody
- [docs/codex.md](docs/codex.md) - Technical specifications

## 🔍 External References

- [RFC 3161](https://www.ietf.org/rfc/rfc3161.txt) - Time-Stamp Protocol
- [EIP-191](https://eips.ethereum.org/EIPS/eip-191) - Signed Data Standard
- [FIPS 186-4](https://csrc.nist.gov/) - Digital Signature Standard

See [anchors/external-references.md](anchors/external-references.md) for comprehensive references.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

Governance and contributor attribution terms are documented in [governance/licensing-ip.md](governance/licensing-ip.md).

## 🔗 Related Resources

- **Blockchain Anchor**: [anchors/blockchain-anchor.md](anchors/blockchain-anchor.md)
- **Timestamp Proof**: [anchors/timestamp-proof.md](anchors/timestamp-proof.md)
- **Verification Guide**: [VERIFY.md](VERIFY.md)
- **Governance Primer**: [onboarding/governance-primer.md](onboarding/governance-primer.md)

---

**Proclaimed**: 2026-07-01  
**Verification**: See [VERIFY.md](VERIFY.md) for cryptographic verification  
**Governance**: See [governance/charter.md](governance/charter.md) for framework
