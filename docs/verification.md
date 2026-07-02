# Verification Procedures

**Version**: 1.0.0  
**Status**: Active  
**Last Updated**: 2026-07-02

## Complete Verification Guide

See [VERIFY.md](../VERIFY.md) for the comprehensive verification guide.

## Verification Levels

- **Level 1**: Basic hash verification (5 min)
- **Level 2**: Signature verification (15 min)
- **Level 3**: Merkle tree verification (30 min)
- **Level 4**: Full chain verification (1-2 hours)

## Verification Tools

- `scripts/hashing.py` - Compute hashes
- `scripts/signature-verification.py` - Verify signatures
- `scripts/merkle-tree.py` - Build and verify trees
- `scripts/root-comparison.py` - Compare roots

## Standards

- RFC 3161 (Timestamps)
- RFC 5652 (CMS)
- FIPS 186-4 (DSS)
- EIP-191/712 (Ethereum)

See [VERIFY.md](../VERIFY.md) for complete details.
