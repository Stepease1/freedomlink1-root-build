# Codex: Technical Specifications

**Version**: 1.0.0  
**Status**: Genesis  
**Last Updated**: 2026-07-02

## Codex Overview

The Codex contains the complete technical specifications for FreedomLink1's cryptographic systems, data structures, and verification mechanisms.

## Volume I: Cryptographic Foundations

### 1.1 Hashing Algorithm
- **Primary**: SHA-256
- **Purpose**: All document hashing
- **Canonicalization**: See `scripts/canonicalization.py`
- **Verification**: See `scripts/hashing.py`

### 1.2 Digital Signatures
- **Standard**: RFC 5652 (CMS)
- **Algorithm**: ECDSA or RSA-2048+
- **Verification**: See `scripts/signature-verification.py`
- **Key Management**: Device Registry

### 1.3 Timestamp Authority
- **Standard**: RFC 3161
- **Provider**: Configured in artifacts
- **Verification**: See VERIFY.md
- **Chain**: Timestamped -> Blockchain -> Archive

## Volume II: Merkle Tree Structures

### 2.1 Tree Construction
- **Type**: Binary Merkle Tree
- **Leaf Nodes**: Document hashes
- **Interior Nodes**: Hash(left + right)
- **Root**: Blockchain anchor point

### 2.2 Proof Verification
- **Algorithm**: See `scripts/merkle-tree.py`
- **Proof Format**: Array of sibling hashes
- **Verification Time**: O(log n)

### 2.3 Tree Updates
- **Immutable**: Old trees preserved
- **New Epoch**: Fresh tree created
- **Continuity**: Hash chain maintained

## Volume III: Blockchain Integration

### 3.1 Network Configuration
- **Primary**: Ethereum Mainnet
- **Secondary**: Polygon
- **Archive**: Arweave
- **Contract**: [Address in artifacts]

### 3.2 Anchor Strategy
- **Root Hash**: Committed to contract
- **Batch**: Merkle batch in 2025Q4
- **Frequency**: End of epoch
- **Verification**: Cross-chain validation

### 3.3 Transaction Format
```solidity
function anchorProof(
  bytes32 merkleRoot,
  uint256 epoch,
  bytes calldata metadata
) public
```

## Volume IV: Data Structures

### 4.1 Document Schema
```yaml
document:
  id: unique-identifier
  hash: sha256-hash
  timestamp: iso8601
  signatures: [signatures]
  metadata: key-value
```

### 4.2 Governance Records
```yaml
governance_record:
  type: amendment|ceremony|vote
  proposer: contributor-id
  date: timestamp
  content: full-text
  votes: [voter-list]
  result: approved|rejected
```

### 4.3 Artifact Format
```json
{
  "hash": "sha256-hex",
  "timestamp": "iso8601",
  "merkle_root": "hex",
  "blockchain": {
    "network": "ethereum",
    "transaction": "0x..."
  }
}
```

## Volume V: Verification Algorithms

### 5.1 Hash Verification
1. Compute hash of document
2. Compare with recorded hash
3. Verify timestamp
4. Check blockchain anchor

### 5.2 Signature Verification
1. Extract signature from document
2. Get signer's public key
3. Verify signature using public key
4. Check timestamp of signature
5. Verify TSA timestamp

### 5.3 Tree Verification
1. Collect leaf hashes
2. Reconstruct tree bottom-up
3. Verify root matches anchor
4. Check blockchain commitment

## Volume VI: Script Implementations

### 6.1 Canonicalization (`canonicalization.py`)
- Deterministic document representation
- Consistent hash output
- Platform-independent
- Idempotent transformation

### 6.2 Hashing (`hashing.py`)
- SHA-256 computation
- Batch processing
- Canonical form enforcement
- Output verification

### 6.3 Merkle Tree (`merkle-tree.py`)
- Tree construction
- Root computation
- Proof generation
- Proof verification

### 6.4 Signature Verification (`signature-verification.py`)
- ECDSA/RSA verification
- RFC 3161 timestamp checking
- Key lookup in registry
- Audit trail generation

### 6.5 Root Comparison (`root-comparison.py`)
- Compare computed vs. recorded roots
- Identify discrepancies
- Generate verification report
- Highlight problematic hashes

## Volume VII: Error Handling

### 7.1 Hash Mismatch
- **Detection**: Verify script output
- **Investigation**: Check source document
- **Resolution**: Review change history
- **Report**: Create incident record

### 7.2 Signature Failure
- **Cause**: Invalid key or tampering
- **Recovery**: Check timestamp
- **Investigation**: Review device logs
- **Remedy**: Ceremony rollback if needed

### 7.3 Blockchain Anchor Issues
- **Problem**: Transaction failed
- **Retry**: Resubmit with new timestamp
- **Fallback**: Use alternate network
- **Record**: Document delay

## Volume VIII: Performance Specifications

### 8.1 Timing
- **Hash computation**: < 1ms per document
- **Signature verification**: < 10ms
- **Merkle proof verification**: < 50ms
- **Full verification**: < 1 second

### 8.2 Scalability
- **Documents**: Unlimited (sharded)
- **Batch size**: Up to 10,000 per epoch
- **Storage**: O(n) for n documents
- **Lookup**: O(log n) via tree

### 8.3 Security Assumptions
- SHA-256: No known preimages
- ECDSA: 256-bit security
- RSA-2048: 112-bit symmetric security
- Blockchain: Immutable ledger

## Standards Compliance

- ✓ RFC 3161 (Timestamp Protocol)
- ✓ RFC 5652 (CMS)
- ✓ FIPS 186-4 (DSS)
- ✓ EIP-191 (Signed Data)
- ✓ EIP-712 (Structured Signing)

## References

- See `anchors/external-references.md` for links
- See `VERIFY.md` for implementation guide
- See `scripts/` directory for source code
