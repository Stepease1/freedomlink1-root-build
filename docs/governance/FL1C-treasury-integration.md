# FL1-C Treasury Integration Rules

Freedomlink1 Root Build - PPTF Treasury Governance Alignment

This document defines the intended economic governance requirements for Freedomlink1 Credit (FL1C) in relation to the PPTF Treasury Governance System. It distinguishes policy requirements and binding declarations from behavior currently enforced by the FL1C contract.

These rules do not, by themselves, create a treasury contract, authorize an action, or prove operational integration.

## Economic Governance Overview

- **Treasury System:** PPTF - Patent Protected Trust Fund
- **Asset Class:** Sovereign Credit Token
- **Symbol:** FL1C
- **Decimals:** 18
- **Declared Governance Authority:** GovernanceRouter
- **Configured Epoch:** 6 - Continuity Epoch

The Unified Layer binding declares PPTF alignment, governance-controlled minting, and a non-inflationary supply policy unless expansion is authorized. These are declared integration rules; treasury execution must be provided by deployed and verified system components.

## Treasury Minting Rules

FL1C minting is intended to be governance-controlled. The current `FL1C.sol` contract enforces this authorization check on `mint`:

```solidity
require(governance.isAuthorized(msg.sender), "Not authorized");
```

A successful authorized call increases `totalSupply` and the recipient balance. The contract does not implement a direct PPTF treasury authorization interface.

### Required Governance Conditions

Before authorizing minting for treasury purposes, the responsible governance process must establish:

- Epoch alignment with the approved treasury action
- Lineage continuity and a record of the action
- Identity provenance for the responsible actor
- Hardware trust evidence where required by institutional policy
- Treasury authorization, allocation purpose, and amount

These are policy requirements. The current token contract checks only whether `governance.isAuthorized(msg.sender)` returns true; it does not itself enforce each condition above.

### Minting Implementation Status

The contract does not impose a supply cap or per-epoch mint limit. Any account accepted by the configured governance router can call `mint` with an amount; therefore, the non-inflationary policy depends on governance controls and is not independently enforced as a token-level cap.

## Treasury Supply Model

The binding declares the supply model as "non-inflationary unless authorized." In implementation terms:

- Minting requires the configured GovernanceRouter to authorize the caller.
- The contract has no maximum supply, rate limit, or treasury allocation check.
- An authorized caller can mint any amount accepted by the EVM's `uint256` arithmetic.
- Supply changes should be approved, documented, and auditable under the applicable treasury process before execution.

A fixed or capped supply must not be claimed unless an enforceable limit is added and verified.

## Treasury Continuity Requirements

### Epoch Awareness

The binding configures epoch 6 as FL1C's lineage epoch and declares epoch awareness. The current contract stores an EpochManager reference, but does not call it or enforce epoch alignment during minting. Epoch checks must be performed by the governance process or added to the contract before they are represented as on-chain enforcement.

### Lineage Anchoring

The binding declares the FL1C genesis event and lineage anchor. The contract registers `FL1C Token Genesis` with its configured LineageRegistry during construction. It does not register subsequent mints or treasury events, nor does it update the local anchor file.

Treasury actions must be recorded in the applicable lineage system before they are described as lineage-anchored. The declared anchor path is `lineage/FL1C_anchor.json`; the available workspace artifact is `freedomlink1-root/lineage/FL1C_anchor.json`.

### Identity Provenance

The contract calls the configured CreatorIdentityRegistry to bind the deployer during construction. This does not verify the identity of each later minter or treasury recipient. Treasury procedures must separately establish that participants are authorized and identity requirements are satisfied.

### Hardware Trust

The contract calls the configured RootstoneBinding for the deployer during construction. This does not attest each later treasury action or prove a live hardware trust state. Such evidence must be checked by the relevant governance process and retained with the action record.

## Treasury Authorization Flow

The following is the required policy flow for a treasury action, not a claim that FL1C implements the complete sequence on-chain:

1. GovernanceRouter receives the treasury request.
2. The applicable access-control process verifies authority.
3. The EpochManager or governance process verifies epoch alignment.
4. Lineage records the approved action and its outcome.
5. Required identity and hardware evidence is checked.
6. PPTF Treasury Governance approves and executes the economic action.
7. If the action mints FL1C, the configured GovernanceRouter must authorize the caller to the token contract.

The current FL1C contract directly enforces only the final token-level caller authorization among these checks.

## Treasury Event Types

The treasury process may classify actions as:

- **Minting:** Governance-authorized supply expansion
- **Allocation:** Distribution to approved institutional modules
- **Continuity:** Epoch-based economic transitions
- **Adjustment:** Governance-authorized supply or rule changes
- **Verification:** Integrity or drift checks

The current contract emits its token `Transfer` event for minting. It registers the genesis event in the LineageRegistry during construction, but does not itself record the other event classes above. Do not describe those events as recorded or anchored until the relevant integrations are implemented and checked.

## Treasury Verification

Evidence may include:

- Unified Layer Drift Detector output
- Unified Layer Integrity Report
- Current binding metadata
- Lineage anchor and registry records
- Identity registry evidence
- Hardware attestation evidence
- PPTF treasury approval and execution records

The drift detector checks local binding metadata against the available lineage artifact. It does not verify deployed contract state, live governance decisions, hardware attestations, PPTF execution, or treasury solvency. Verification statements must identify the evidence and scope used.

## Implementation Checklist

Before claiming full treasury integration, verify that:

- The configured governance, epoch, lineage, identity, and hardware addresses are deployed and correct.
- Epoch and treasury-policy checks are enforced at the appropriate authority boundary.
- Supply limits or governance safeguards match the adopted issuance policy.
- Mint, allocation, adjustment, and continuity actions are recorded in lineage and treasury systems.
- Identity and hardware requirements are checked for relevant actors and actions.
- Tests cover authorization failures, unauthorized issuance, policy boundaries, and event recording.

## Closing

The FL1C binding declares alignment with PPTF and governance-controlled minting. The current contract enforces GovernanceRouter authorization for minting and performs creator, hardware, and genesis-lineage calls during construction. Epoch enforcement, supply caps, per-action identity and hardware validation, and treasury execution are not implemented by the token contract itself.

This document defines the requirements and records that implementation boundary so future changes can be evaluated without confusing policy declarations with verified behavior.

Freedomlink1 Root Build

FL1-C Treasury Integration Rules - Epoch 6
