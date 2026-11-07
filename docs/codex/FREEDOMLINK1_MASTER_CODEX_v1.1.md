# Freedomlink1 Master Codex v1.1

- **Classification:** Proposed constitutional and technical synthesis
- **Version:** 1.1
- **Status:** Draft for institutional review; not yet approved or inscribed
- **Scope:** Freedomlink1 Root Build

> **Lineage note:** The repository's first substantive Version 1.0.0 Codex is [`docs/codex.md`](../codex.md), introduced in commit `831449f` after the Root Build v1.0.0 baseline commit `a62cf20`. No separately named `FREEDOMLINK1_MASTER_CODEX_v1.0.md` exists in repository history. This v1.1 draft is a documented successor synthesis, not a recovered or line-by-line copy of a missing Master Codex. See the [v1.0.0 Codex lineage record](FREEDOMLINK1_MASTER_CODEX_v1.0_LINEAGE.md).

This Codex brings together the repository's governance, Merkle Forest, epoch, ledger, Rootstone-I, and sovereign-layer materials. It distinguishes source-backed behavior from proposed policy and descriptive documentation. It does not replace a trust instrument, governance protocol, canonical ledger, contract, or other authority-bearing artifact.

## I. Purpose and Authority

The Master Codex is an index and synthesis of Freedomlink1's constitutional principles, technical components, and continuity records. It is intended to make their scope and relationships easier to review.

This draft does not itself:

- enact or amend institutional policy;
- activate an epoch or confer governance eligibility;
- establish that a smart contract is deployed or audited;
- prove hardware identity, runtime behavior, or signer identity; or
- supersede a governing instrument or a properly approved record.

Approval, amendment, and inscription must follow the applicable governance instruments and be recorded in the designated authoritative systems.

## II. Constitutional Principles

The proposed synthesis is guided by these principles:

1. **Verifiability:** Claims should identify the artifact and method by which they can be checked.
2. **Transparency:** Governance decisions and their status should be distinguishable from proposals.
3. **Continuity:** Successor records should identify their predecessors and preserve unresolved status accurately.
4. **Provenance:** A file, hash, signature, or declaration should not be represented as proving more than it does.
5. **Accountability:** Changes to authority-bearing artifacts require the review and approvals specified by their governing process.

These principles describe the intended framework; this Codex does not independently enforce them.

## III. System Architecture

The Root Build brings together governance documents, contracts, lineage and ledger records, integrity artifacts, and Rootstone-I specifications. The following is a conceptual map, not a claim that every branch is included in one cryptographic root:

```text
Freedomlink1 Root Build
├── Governance and institutional documents
├── Smart-contract source
├── Epoch and lineage records
├── Configured Merkle Forest artifacts
└── Rootstone-I and sovereign-layer specifications
```

The repository's generated Merkle Forest is scoped to the artifacts configured in its manifest. Its root must not be described as a hash of the complete institution unless the manifest and generation process are explicitly expanded and verified to cover that corpus.

## IV. Merkle Forest Architecture

The repository contains an Epoch 7 Merkle Forest manifest, generated hash data, and an SVG diagram:

- [Forest manifest](../merkle-forest.json)
- [Leaf and tree hashes](../merkle-forest-hashes.json)
- [Forest diagram](../merkle-forest.svg)

The generator reads the configured artifact paths, computes SHA-256 leaf and tree hashes, and writes the forest root, hashes, and diagram labels. The manifest currently lists five configured trees. This process provides integrity comparisons for those inputs; it is not, by itself, public verification, a signed manifest, or proof that all governance, ledger, seal, or hardware artifacts are covered.

**Intended purposes:**

- detect changes to configured inputs;
- support integrity review and provenance checks;
- make the configured artifact set inspectable; and
- provide a repeatable hash-generation process.

## V. Smart Contract Stack

The repository contains source for the three contracts below. The source files establish implementation details, not deployment, audit, production readiness, or use on any particular network.

### A. FreedomlinkBonusCodes

Source: [contracts/FreedomlinkBonusCodes.sol](https://github.com/Stepease1/freedomlink1-root-build/blob/main/contracts/FreedomlinkBonusCodes.sol)

The source supports steward and custodian roles, code issuance keyed by a code hash, expiry checks, redemption tracking, and calls to the configured reward and cadence contracts.

The current source does **not** implement the draft's `issueCodeWithSig(...)`, EIP-712 delegated issuance, or Merkle-proof redemption. Those capabilities must not be treated as available until implemented, reviewed, and separately evidenced.

### B. RewardsEngine

Source: [contracts/RewardsEngine.sol](https://github.com/Stepease1/freedomlink1-root-build/blob/main/contracts/RewardsEngine.sol)

The current source defines `BoostMultiplier`, `BadgeCredit`, `CadenceBoost`, `AccessPass`, and `LineageMark`. It updates the corresponding per-user mappings when called by its configured system address. These contract state changes are not, on their own, a general civic-score calculation or proof of governance rights in another system.

### C. CadenceCycle

Source: [contracts/CadenceCycle.sol](https://github.com/Stepease1/freedomlink1-root-build/blob/main/contracts/CadenceCycle.sol)

The current source records bonus-code events and updates a cadence score. Its `weightForRewardType` function returns weights of 5, 3, 10, 20, and 50 for reward types 0 through 4, respectively, and 1 for other values. These are source-level scoring values; they do not establish eligibility rules or a deployed governance process.

## VI. Bonus Code Protocol

The implemented source path is:

```text
Custodian issues a code hash
        ↓
User submits the raw code
        ↓
Contract hashes and checks the code and expiry
        ↓
Reward Engine and Cadence Cycle are called
        ↓
Redemption event is emitted
```

This describes the contract source only. The conceptual transformation
**Attention → Action → Attestation → Lineage → Sovereignty** is an institutional aspiration, not a guarantee made by the contract.

## VII. Reward System

The source-defined reward types are:

| Reward type | Current source behavior |
| --- | --- |
| `BoostMultiplier` | Adds to the user's boost multiplier |
| `BadgeCredit` | Adds to badge progress |
| `CadenceBoost` | Adds to the RewardsEngine cadence score |
| `AccessPass` | Sets the user's governance-access flag to `true` |
| `LineageMark` | Adds to the user's lineage marks |

These behaviors are limited to the contract mappings and calls shown in the source. They do not prove off-chain access enforcement, transferable rights, or a particular economic value.

## VIII. Civic Score System

A weighted civic score is a possible future policy, not an implemented system established by the current contract sources.

If adopted, a scoring formula, weights, data sources, update rules, appeals, and governance consequences must be defined in an approved specification. The cadence weights in `CadenceCycle.sol` must not be silently treated as a complete civic-score policy.

## IX. Epoch Governance System

Epochs and advancement are described in the [Epoch Advancement Protocol](../governance/Epoch_Advancement_Protocol.md) and recorded in repository ledger and lineage materials. The protocol describes a sequence involving corpus preparation, hashing, signature and seal records, validation, and activation. Those procedural statements do not prove that every step has occurred.

The history resolves the active-epoch status: signed commit `1d4a858a551c474be29f87b74e88c34c845aec0b` explicitly updates [`lineage/epoch-ledger.md`](https://github.com/Stepease1/freedomlink1-root-build/blob/main/lineage/epoch-ledger.md) to record Epoch 7 as active, after the Epoch 7 seal, explorer entry, continuity index, and lineage node were committed. The earlier Epoch 7 explorer records accurately described the state before that ledger update; their current versions now record the subsequent activation. The machine-readable [`lineage/epoch_ledger.json`](https://github.com/Stepease1/freedomlink1-root-build/blob/main/lineage/epoch_ledger.json) is synchronized to that canonical status. Epoch 7's seal JSON still has `key_fingerprint: PENDING`, `signature_status: unsigned`, and `seal_status: pending`; the ledger's active status does not erase or resolve those payload fields.

## X. Continuity Index System

Continuity indexes record relationships among epoch artifacts and describe continuity context. The Epoch 7 Continuity Index records its own limited authority: it does not activate an epoch or change the canonical ledger. The later signed ledger update, rather than the index or lineage node, records Epoch 7's active status.

An index is evidence of its recorded contents and provenance only. It is not a substitute for the applicable ledger update, signature, or authorization.

## XI. Lineage Node System

The repository includes an [Epoch 7 Lineage Node](https://github.com/Stepease1/freedomlink1-root-build/blob/main/freedomlink1-governance/explorer/epoch7_lineage_node.md). That record describes its relationship to the Epoch 7 seal, explorer entry, and continuity index. Its creation did not itself activate Epoch 7; the subsequent ledger update did.

Lineage records support historical reference and review. Their existence alone does not establish that all referenced payload fields are signed, complete, or authoritative.

## XII. Governance Eligibility

The proposed criteria in earlier design material—such as a cadence threshold, recent activity, lineage participation, or AccessPass status—are not established here as current policy. The reviewed contract sources do not enforce a cadence threshold of 200, a 30-day activity window, or automatic eligibility based on an AccessPass.

Eligibility rules require an approved governance specification and an identified enforcement and review process before they can be represented as operative.

## XIII. Governance Ledger

Governance records may include proposals, decisions, voting, sanctions, commendations, and other authorized actions. This Codex does not assert that every such record is currently captured in a single immutable ledger.

“Permanent,” “immutable,” and “publicly auditable” are properties that require evidence about storage, access, change controls, and verification. They are not established merely by describing a record as a ledger.

## XIV. Canonical Epoch Ledger

The [Epoch Advancement Protocol](https://github.com/Stepease1/freedomlink1-root-build/blob/main/governance/epoch_advancement_protocol.md) identifies `lineage/epoch_ledger.json` as the machine-readable advancement record. The human-readable [`lineage/epoch-ledger.md`](https://github.com/Stepease1/freedomlink1-root-build/blob/main/lineage/epoch-ledger.md) preserves the detailed history and activation rationale. Both records now identify Epoch 7 as active; unknown legacy dates and unrecorded activation lists remain explicitly unknown rather than being inferred. The Epoch 7 seal payload remains pending as described above.

The responsible governance authority should identify the canonical record, reconcile conflicting status, and preserve the decision and its provenance. Until then, this Codex makes no independent canonical-epoch declaration.

## XV. Monthly Codex

A monthly record could document steward statements, governance outcomes, lineage changes, cadence milestones, amendments, and institutional events. This section proposes a recordkeeping practice; it does not assert that a monthly Codex process is currently operating.

Any adopted process should identify its responsible authors, review and approval path, retention policy, and relationship to the canonical ledger.

## XVI. Rootstone-I

The repository documents Rootstone-I as a hardware-root-of-trust concept and identity surface in [Rootstone-I Identity](../rootstone/identity.md) and related specifications.

This Codex does not certify that physical hardware exists, is present, is secure, or has performed signing or verification. Hardware identity and operation require independent, appropriately scoped evidence.

## XVII. Governance Attestation System

The intended attestation framework may cover codices, ledgers, specifications, governance documents, and manifests. Each attestation should state what was signed or hashed, by whom or by which key, when, and how verification was performed.

A signed Git commit establishes the validity of that commit's signature under the verifier's configured key. It does not automatically sign the artifact's internal payload, establish the signer's real-world identity, or make every artifact in the repository attested.

## XVIII. Sovereign Intelligence Layer

Repository documentation describes intelligence dashboards and possible metrics such as integrity anomalies, epoch health, and drift indicators. These are documented concepts and decision-support surfaces; this Codex does not assert that forecasting, anomaly detection, or automated institutional monitoring is implemented or validated.

Any operational analytics must document its inputs, method, limitations, and responsible human review.

## XIX. Sovereign Autonomy Layer

Repository material describes autonomy and sentinel concepts. Such documentation is not evidence that autonomous actions are enabled, safe, authorized, or operating.

Any automation that can mutate governance, lineage, signatures, or epoch state requires explicit authorization boundaries, reviewable logs, failure handling, and controls preventing an advisory signal from being treated as approval.

## XX. Sovereign Consciousness Layer

Repository material describes governance memory, semantic context, institutional narrative, and steward guidance as concepts. This Codex treats these as descriptive or aspirational capabilities, not as evidence of machine consciousness, independent authority, or reliable institutional reasoning.

## XXI. Dashboard System

Possible dashboard views include civic and cadence scores, badges, governance status, timelines, and contribution summaries. The repository contains dashboard documentation, but this Codex does not claim that every proposed console, leaderboard, or live data feed is implemented or connected to authoritative sources.

Displayed information should identify its source, freshness, and limitations; dashboards should not confer authority.

## XXII. Analytics Layer

Potential analytics inputs include contract events, indexed data, dashboard queries, and governance records. Potential metrics include issuance and redemption counts, governance activity, cadence, epoch health, and score distributions.

The metrics are proposals unless a functioning data pipeline and its validation are independently established. Analytics should not be presented as complete or authoritative without documented coverage and reconciliation.

## XXIII. Deployment System

The proposed network list—BNB Smart Chain, Polygon, Arbitrum, and Base—is not a deployment claim. This Codex does not identify a verified contract address, chain, deployment transaction, source verification record, or production release for the contracts in Section V.

A deployment record should identify at minimum the network and chain ID, contract address, transaction, compiler settings, source verification, and responsible approval. A proposed pipeline of **Compile → Test → Deploy → Verify → Anchor → Publish** is a design sequence, not evidence that deployment has occurred.

## XXIV. Documentation System

The repository builds documentation with MkDocs and the Material theme. The strict documentation build validates configured navigation and links; it does not validate the truth, authority, completeness, or runtime behavior of the documented claims.

Documentation areas include governance, contracts, lineage, Rootstone-I, Codex materials, and the Merkle Forest.

## XXV. Visual System

Visual materials may include founder, governance, trust-root, and epoch seals; badges; and covers for protocols, charters, monthly records, and epoch assemblies.

Visual presence does not establish a cryptographic signature, legal status, governance approval, or hardware attestation.

## XXVI. Ceremonial Oath

In the presence of the civic record, before the lineage of those who built and those who will inherit, we affirm:

> Truth must be verifiable.
>
> Governance must be transparent.
>
> Lineage must remain unbroken.
>
> Rewards must be earned.
>
> Sovereignty must be preserved.
>
> Attention becomes action.
>
> Action becomes attestation.
>
> Attestation becomes lineage.
> Lineage becomes sovereignty.

This oath is declarative text. Its inclusion does not create an approval, signature, or enforceable control.

## XXVII. Root Build Status and Review

| Area | Repository evidence | Status in this Codex |
| --- | --- | --- |
| Governance and institutional documents | Present in repository | Governed by their own authority and approval process |
| Bonus code, rewards, and cadence contract source | Present in `contracts/` | Source exists; deployment and audit are not established here |
| Merkle Forest artifacts | Manifest, hashes, diagram, and generator present | Coverage is limited to configured manifest inputs |
| Epoch, continuity, and lineage records | Multiple records present | Active-epoch records conflict and require reconciliation |
| Rootstone-I | Documentation and specifications present | Physical hardware operation is not established |
| Intelligence, autonomy, and consciousness layers | Dashboard and governance documentation present | Descriptive capabilities; implementation is not established |
| Civic score, eligibility thresholds, and monthly Codex | Proposed in design material | Not established as operative policy |
| Multi-chain deployment | Networks proposed in design material | No deployment evidence asserted |
| Master Codex v1.0 lineage | Substantive v1.0.0 source identified as `docs/codex.md`; see the [lineage record](FREEDOMLINK1_MASTER_CODEX_v1.0_LINEAGE.md) | v1.1 is a successor synthesis, not a recovered file |

### Adoption Requirements

Before this draft is treated as a canonical successor:

1. Review the [v1.0.0 Codex lineage record](FREEDOMLINK1_MASTER_CODEX_v1.0_LINEAGE.md) and its source text.
2. Resolve the pending Epoch 7 seal-payload metadata through the authorized process; the active-epoch ledger status is already recorded.
3. Review all statements about contracts, hardware, signatures, analytics, and deployment against primary evidence.
4. Obtain the approvals required by applicable institutional instruments.
5. Record the approved version, its hash and signatures as required, and its lineage reference in the designated authoritative systems.

- **Artifact:** Freedomlink1 Root Build — Master Codex v1.1 draft
- **Classification:** Sovereign digital institution
- **Proposed motto:** *VERITAS • SECURITAS • AEQUITAS* — Truth • Security • Equity
- **Lineage and epoch status:** Refer to reconciled, authorized records; not declared by this draft.
