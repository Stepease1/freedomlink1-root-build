# Governance Router Specification

| Document field | Value |
|---|---|
| Version | 2.0 |
| Status | Production Candidate |
| Contract | `contracts/governance/GovernanceRouter.sol` |
| Authority model | Multisig controlled |
| Transfer model | Two-step authority transfer |
| Lineage impact | Non-breaking security enhancement |

This specification describes the intended behavior of the FreedomLink1 Governance Router. Deployment or execution claims require the applicable on-chain verification and governance approval evidence.

## 1. Purpose

The Governance Router centralizes authorization for FL1C credential minting, credential revocation, and role changes. It separates institutional authority from individual accounts and provides a controlled transfer mechanism.

## 2. Security Enhancements

- Two-step governance authority transfer.
- Pending governance authority with explicit acceptance.
- Multisig-ready current and pending authority model.
- Constructor validation of governance dependencies.
- Governance action events for authority and permission changes.
- Batch synchronization limits for permission updates.
- Individual and batch permission management.
- Compatibility owner fields for existing integrations.

## 3. Authority Model

```text
Safe Multisig
      |
      v
Governance Router
      |
      +--> FL1C credential authorization
      +--> Epoch management dependency
      +--> Lineage registry dependency
```

The current governance authority may propose a transfer but cannot complete it by changing the authority directly. The pending authority must accept the transfer.

The canonical source for the router is `freedomlink1-root/contracts/governance/GovernanceRouter.sol`.

## 4. Transfer Process

```text
Current Authority
      |
      v
proposeGovernanceAuthority(newAuthority)
      |
      v
Pending Authority
      |
      v
acceptGovernanceAuthority()
      |
      v
Transfer Complete
```

The current authority may cancel a pending transfer. The pending authority is authorized to accept only the specific proposed address.

## 5. Batch Limits

`MAX_BATCH_SYNC = 100`

Purpose:

- Prevent oversized transaction payloads.
- Improve operational reliability.
- Reduce failed or excessive governance executions.
- Preserve attributable batch event records.

Batch permission updates must provide account and permission arrays of equal length. An empty batch or a batch above the limit is rejected.

## 6. Governance Event Coverage

The router emits events for:

- Credential mint permission updates.
- Credential burn permission updates.
- Role-change permission updates.
- Batch permission updates.
- Governance authority transfer proposals.
- Governance authority transfer acceptance.
- Governance authority transfer cancellation.
- Current authority and legacy ownership compatibility updates.

The router remains compatible with operations that reference credential issuance, credential revocation, epoch advancement, and lineage synchronization. Such operations must use the appropriate subsystem contract and governance authority.

## 7. Dependency Model

The constructor validates:

- Governance authority address.
- FL1C contract address.
- Epoch manager address.
- Lineage registry address.

No dependency may be the zero address. This validates router deployment inputs but does not attest to the correctness or approval status of deployed dependencies.

## 8. Deployment Requirements

Create and review a Safe multisig before production deployment.

Recommended:

- Network: BNB Smart Chain.
- Threshold: 3 of 5.

Signer roles:

1. Founder Steward.
2. Technical Steward.
3. Governance Steward.
4. Recovery Steward.
5. Institutional Reserve Steward.

Production deployment is a governed operation and must follow the applicable institutional review process.

## 9. Constructor Interface

```solidity
constructor(
    address governanceAuthority,
    address fl1cAddress,
    address epochManagerAddress,
    address lineageRegistryAddress
)
```

## 10. Verification

After deployment, verify:

```solidity
governanceAuthority()
```

The result must equal the approved multisig address.

Additional verification should confirm:

- The deployed router address.
- The approved FL1C, epoch manager, and lineage registry addresses.
- Pending authority is initially zero.
- Permissions are assigned only to approved identities or contracts.
- Transfer proposal and acceptance events identify the expected authorities.
