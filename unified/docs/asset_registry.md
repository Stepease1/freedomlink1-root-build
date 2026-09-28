# Unified Layer Asset Registry

Freedomlink1 Unified Layer - Sovereign Asset Index

The Unified Layer Asset Registry is the canonical documentation index of sovereign assets registered in this workspace. Registry entries link each asset to its binding and supporting integration, lineage, identity, hardware, and economic metadata. Listing here records the asset's declared Unified Layer integration; it is not, by itself, legal recognition or proof of deployed operation.

## Registry Overview

- **Registry Type:** Sovereign Asset Index
- **Institution:** Freedomlink1
- **Configured Epoch:** 6 - Continuity Epoch
- **Registry State:** Active
- **Verification Surface:** [Unified Layer Integrity Report](unified_layer_integrity.md)
- **Drift Detection:** Enabled
- **Currently Listed Assets:** 1

Entries are listed after their binding and supporting integration references are recorded. Status claims are limited to the evidence and verification scope noted in each entry.

## Registered Sovereign Assets

### 1. FL1-C - Freedomlink1 Credit

- **Type:** Sovereign Token
- **Symbol:** FL1C
- **Decimals:** 18
- **Origin:** Freedomlink1 Root Build
- **Configured Epoch:** 6 - Continuity Epoch
- **Binding File:** `unified/bindings/fl1c_binding.json`
- **Integration Doc:** `unified/docs/integration/FL1C-unified-integration.md`
- **Declared Lineage Anchor:** `lineage/FL1C_anchor.json`
- **Resolved Lineage Artifact:** `freedomlink1-root/lineage/FL1C_anchor.json`
- **Drift Report:** `unified/reports/fl1c_drift_report.json`

#### Cross-Layer Recognition

| Layer | Declared Integration | Local Check Result |
|-------|----------------------|--------------------|
| Governance | GovernanceRouter, EpochManager, LineageRegistry, AccessControl | Binding declarations present; governance lineage event matches |
| Lineage | FL1C Token Genesis; epoch 6 | Event and epoch match the resolved anchor |
| Identity | CreatorIdentityRegistry; `identity.bindCreator(msg.sender)`; sovereign-creator-attested | Binding declarations present; anchor records `creator-bound` |
| Hardware | RootstoneBinding; `rootstone.bind(msg.sender)`; Rootstone-I | Binding declarations present; anchor records `bound` |
| Economic | PPTF; governance-aligned, governance-controlled minting | Binding declares economic consistency; operational behavior not tested |
| Unified Layer | Version 1.0.0; integration state `bound` | Consistency flags are true; all checked local metadata matched |

#### Verification Status

The most recent local drift check reported `none_detected` for the checks it performs. The machine-readable report records all checks as passing, with no failed or unknown checks, and records the resolved lineage artifact above.

- **Last Check:** Timestamp recorded in `unified/reports/fl1c_drift_report.json` and mirrored in the binding
- **Verification Scope:** Local binding metadata and on-disk lineage artifact only
- **Runtime / Deployment Verification:** Not performed

The detector checks declared governance bindings, event and epoch alignment, identity and hardware anchor metadata, and Unified Layer consistency flags. It does not verify deployed contracts, live registries, hardware attestations, treasury operations, or legal status.

FL1-C is the first and currently only asset listed in this registry.

## Registry Structure

Each asset entry should provide:

- Asset name, type, symbol where applicable, and configured epoch
- Machine-readable binding reference
- Human-readable integration document
- Declared and resolved lineage anchor references
- Identity provenance metadata
- Hardware trust binding metadata
- Economic alignment and policy declarations
- Unified Layer consistency metadata
- Machine-readable drift report and its verification scope

This structure gives future entries a consistent, reviewable set of references without implying checks that have not been performed.

## Registry Expansion

Future entries may include modules, tokens, registries, charters, treasury instruments, continuity modules, and integration frameworks. Add an asset after its binding and supporting references are available and its verification status is documented.

Recommended onboarding artifacts:

1. Binding JSON
2. Integration document
3. Explorer visibility
4. Integrity report entry
5. Drift detector coverage and machine-readable output

## Closing

The Unified Layer Asset Registry is the index of assets currently documented as integrated in this workspace. It starts with FL1-C and provides a consistent reference structure for future entries across governance, lineage, identity, hardware, economic, and Unified Layer concerns.

Freedomlink1 Unified Layer

Asset Registry - Epoch 6
