# Governance Router Hardening

| Document field | Value |
|---|---|
| Classification | Governance Hardening Release |
| Artifact | Governance Router v2.0 |
| Status | Production Candidate |
| Security classification | Production Candidate |
| Authority model | Multisig Controlled |
| Transfer model | Two-Step Authority Transfer |
| Lineage impact | Non-breaking security enhancement |

## Summary

This release hardens governance authority management for the FreedomLink1 FL1C system while preserving the existing permission and FL1C integration model.

## Added

- Two-step governance authority transfers.
- Explicit pending governance authority.
- Cancellation of pending authority transfers.
- Constructor validation for governance dependencies.
- Governance action events.
- A 100-item batch permission synchronization limit.
- Batch permission updates with array-length validation.
- Compatibility with existing `owner`, permission, and FL1C authorization interfaces.

## Constructor Interface

```solidity
constructor(
    address governanceAuthority,
    address fl1cAddress,
    address epochManagerAddress,
    address lineageRegistryAddress
)
```

## Governance Recommendation

Deploy behind a reviewed Safe multisig.

Recommended threshold:

```text
3 of 5
```

## Signer Roles

1. Founder Steward.
2. Technical Steward.
3. Governance Steward.
4. Recovery Steward.
5. Institutional Reserve Steward.

Signer assignment and any threshold or signer change require the applicable governance approval and evidence.

## Deployment Procedure

1. Create and review the Safe multisig on BNB Smart Chain.
2. Record the approved Safe address as `GOVERNANCE_SAFE_ADDRESS`.
3. Confirm the approved FL1C, epoch manager, and lineage registry addresses.
4. Deploy the Governance Router using the validated dependency addresses.
5. Assign permissions only to approved operators or contracts.
6. Verify `governanceAuthority()` returns `GOVERNANCE_SAFE_ADDRESS`.
7. Verify `pendingGovernanceAuthority()` is initially zero.
8. Preserve deployment transaction, verified source, constructor arguments, and multisig approval evidence.

## Verification

Production readiness requires:

- Hardhat compilation.
- Router and FL1C tests.
- Two-step transfer test evidence.
- Batch-limit test evidence.
- Constructor dependency validation.
- Multisig deployment approval.
- Reviewed and verified contract source.
- Independent review of production dependencies.

## Architectural Outcome

Single-key governance authority is replaced by a documented, accept-required multisig authority model.

This change does not itself transfer existing on-chain authority. The current contract owner must execute the two-step proposal process and the approved pending multisig must accept it.

## Constitutional Notice

This record documents a production candidate hardening change. It does not itself amend the Canonical Epoch Ledger, alter epoch lineage, authorize an on-chain transfer, or attest to deployed contract behavior.
