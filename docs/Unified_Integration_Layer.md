# Freedomlink1 Unified Integration Layer (Full Edition)

## 1. Purpose

The Unified Integration Layer defines how Freedomlink1 functions as a single sovereign institution across:

- Protocol (code, deployments, infrastructure)
- Governance (lineage, seals, signatures, doctrines)
- Hardware (Rootstone-I)
- Institutional layer (PPTF)
- Multi-chain deployments
- Epoch advancement and continuity

It lives in the `freedomlink1-unified` repository and is authoritative for cross-repo bindings.

---

## 2. Layer Model

### 2.1 Protocol Layer

**Repo:** `freedomlink1-protocol`

**Scope:**

- `contracts/` - Solidity and protocol logic
- `interfaces/` - external and internal interfaces
- `deploy/` - deployment scripts and tooling
- `ci/` - CI/CD pipelines
- `docs/` - protocol documentation
- `dashboard/` - UI for protocol state
- `analytics/` - metrics, leaderboard, Dune layouts
- `manifest/` - network and multi-chain manifests
- `ceremony/` - deployment ceremony scripts

The Protocol Layer is deterministic, technical, and chain-facing.

### 2.2 Governance Layer

**Repo:** `freedomlink1-governance`

**Scope:**

- `lineage/` - epoch lineage, anchors, seals, ledger
- `lineage/seals/` - sealed epoch artifacts
- `lineage/anchors/` - anchor points for hardware and epochs
- `lineage/ledger/` - epoch-by-epoch governance records
- `docs/governance/` - doctrines, proclamations, rights & duties
- `sentinel/` - sentinel directives and oversight logic
- `continuity/` - continuity and succession frameworks

The Governance Layer is sovereign, institutional, and human-facing.

### 2.3 Unified Layer

**Repo:** `freedomlink1-unified`

**Scope:**

- `unified/freedomlink1.unified.yaml` - canonical unified manifest
- `unified/protocol.map.json` - protocol repo mapping
- `unified/governance.map.json` - governance repo mapping
- `unified/epoch.bindings.json` - epoch <-> protocol <-> governance bindings
- `unified/sovereign.bindings.json` - sovereign keys and signatures bindings
- `unified/deployment.bindings.json` - deployment manifests and ceremonies
- `unified/rootstone.bindings.json` - Rootstone-I hardware bindings
- `unified/pptf.bindings.json` - PPTF institutional bindings
- `unified/multi_chain.map.json` - multi-chain deployment mapping
- `versioning/*.version` - version tracking for unified, protocol, governance, lineage

The Unified Layer is declarative, integrative, and system-facing.

---

## 3. Binding Models

### 3.1 Epoch Binding Model

**File:** `unified/epoch.bindings.json`

Each epoch entry binds:

- a governance artifact (seal, anchor, ledger)
- a protocol state (contracts, deployment scripts, manifests)
- a lineage state (epoch number, merkle root, anchor)

Example:

```json
{
  "epoch_4": {
    "merkle_root": "...",
    "seal": "freedomlink1-governance/lineage/seals/epoch_4_seal.json",
    "contracts": "freedomlink1-protocol/contracts/",
    "deployment_scripts": "freedomlink1-protocol/deploy/"
  }
}
```

This ensures every epoch has a verifiable technical and governance footprint.

### 3.2 Sovereign Binding Model

**File:** `unified/sovereign.bindings.json`

Defines:

- founder key location
- epoch-specific signatures
- linkage to Rootstone-I and PPTF identity bindings

Example:

```json
{
  "sovereign": {
    "founder_key": "/c/Users/crazy/founder.key",
    "epoch_signatures": {
      "epoch_3": "founder_epoch3.sig",
      "epoch_4": "founder_epoch4.sig"
    },
    "rootstone_identity": "rootstone.bindings.json",
    "pptf_identity": "pptf.bindings.json"
  }
}
```

This model ties human sovereignty to technical and hardware identity.

### 3.3 Deployment Binding Model

**File:** `unified/deployment.bindings.json`

Defines:

- network manifests (mainnet, testnet, local)
- deployment ceremony script

Example:

```json
{
  "deployment": {
    "networks": {
      "mainnet": "freedomlink1-protocol/manifest/mainnet.json",
      "testnet": "freedomlink1-protocol/manifest/testnet.json",
      "local": "freedomlink1-protocol/manifest/local.json"
    },
    "ceremony": "freedomlink1-protocol/ceremony/deployment_ceremony.md"
  }
}
```

This ensures deployments are both technically valid and ceremonially recorded.

### 3.4 Hardware Binding Model (Rootstone-I)

**File:** `unified/rootstone.bindings.json`

Defines:

- hardware root identity
- governance anchor
- protocol binding path

Example:

```json
{
  "rootstone": {
    "hardware_root": "Rootstone-I",
    "identity_anchor": "freedomlink1-governance/lineage/anchors/rootstone_anchor.json",
    "protocol_binding": "freedomlink1-protocol/contracts/rootstone/"
  }
}
```

This binds physical hardware identity into the protocol and governance fabric.

### 3.5 Institutional Binding Model (PPTF)

**File:** `unified/pptf.bindings.json`

Defines:

- PPTF as institutional layer
- governance documents path
- protocol binding path

Example:

```json
{
  "pptf": {
    "institutional_layer": "PPTF",
    "documents": "freedomlink1-governance/docs/pptf/",
    "protocol_binding": "freedomlink1-protocol/contracts/pptf/"
  }
}
```

This binds institutional finance/trust structures into the protocol.

### 3.6 Multi-Chain Binding Model

**File:** `unified/multi_chain.map.json`

Defines:

- supported chains
- reference to protocol multi-chain manifest

Example:

```json
{
  "multi_chain": {
    "chains": [
      "ethereum",
      "polygon",
      "arbitrum",
      "optimism",
      "base",
      "solana"
    ],
    "manifest": "freedomlink1-protocol/manifest/multi_chain.json"
  }
}
```

This keeps multi-chain expansion declarative and centralized.

## 4. Versioning and Continuity

**Files:**

- `versioning/unified.version` - version of unified manifest layer
- `versioning/protocol.version` - reference to protocol repo version/tag
- `versioning/governance.version` - reference to governance repo version/tag
- `versioning/lineage.version` - current epoch / lineage state

### 4.1 Versioning Rules

- Bump `unified.version` when bindings or manifests change in a way that affects integration.
- Update `protocol.version` when the protocol repo hits a significant release or tag.
- Update `governance.version` when the governance corpus or lineage hits a significant milestone.
- Update `lineage.version` when a new epoch is sealed/anchored.

This creates a time-ordered, cross-repo continuity record.

## 5. Evolution Model

### 5.1 Adding a New Epoch

1. Update the governance repo:
   - add a new ledger entry
   - add a new seal/anchor
2. Update the protocol repo:
   - deploy new contracts or manifests if needed
3. Update the unified repo:
   - add a new entry to `epoch.bindings.json`
   - update `lineage.version`
   - bump `unified.version`

### 5.2 Adding a New Chain

1. Update `freedomlink1-protocol/manifest/multi_chain.json`.
2. Add the chain to `unified/multi_chain.map.json`.
3. Bump `unified.version`.

### 5.3 Adding a New Hardware or Institutional Anchor

1. Add the anchor in the governance repo.
2. Add the binding in `rootstone.bindings.json` or `pptf.bindings.json`.
3. Bump `unified.version`.

## 6. Role of the Unified Repo

The Unified Repo:

- does **not** execute code
- does **not** store governance documents
- does **not** store protocol logic

It **declares** how all of those pieces fit together.

It is the institutional map that ensures Freedomlink1 remains:

- traceable
- auditable
- sovereign
- extensible
- multi-layer and multi-chain aware

over time.
