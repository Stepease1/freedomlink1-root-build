# POC Domain Mapping

**Adopted**: 2026-07-13  
**Status**: Integrated into Genesis Governance Lineage  
**Purpose**: Map the Proof-of-Concept work into the FreedomLink1 governance, documentation, and verification architecture.

## Scope

This document defines how the POC outputs connect to the existing FreedomLink1 framework across governance, lineage, ceremony, and epoch documentation.

## Mapping Domains

### 1. Governance Domain
- Anchors the POC in the constitutional framework defined by [governance/charter.md](../governance/charter.md)
- Establishes review criteria through [governance/poc-governance-rubric.md](../governance/poc-governance-rubric.md)
- Confirms that POC decisions remain traceable to the governance process

### 2. Documentation Domain
- Records the POC in the public documentation stack under [docs/index.md](index.md)
- Preserves narrative context for future auditors and contributors
- Supports discoverability for governance reviews and verification workflows

### 3. Ceremony Domain
- Connects activation milestones to the formal ceremony log in [lineage/ceremonies.md](../lineage/ceremonies.md)
- Defines the activation event as a governance milestone rather than an informal note
- Ensures the POC transition is witnessed and archived

### 4. Epoch Domain
- Situates the POC within the temporal framework governed by [docs/epochs.md](epochs.md)
- Tracks the POC through initiation, execution, review, and transition phases
- Provides continuity with the broader Genesis epoch progression

## Relationship to Other Artifacts

This mapping document is the reference point for:
- [docs/poc-activation-ceremony.md](poc-activation-ceremony.md) for the formal activation event
- [governance/poc-governance-rubric.md](../governance/poc-governance-rubric.md) for evaluation criteria
- [docs/poc-epoch-progression.md](poc-epoch-progression.md) for lifecycle tracking

## Constitutional Anchoring Matrix

This matrix ensures every POC is constitutionally anchored within the FreedomLink1 governance lineage.

| POC | Primary Domain | Secondary Domains | Rationale |
| --- | --- | --- | --- |
| Merkle Inclusion API | Proof | Ledger, Index | Generates inclusion proofs; strengthens the Proof Master and Merkle lineage. |
| On-Chain Timestamp Oracle | Archive | Eternity, Ledger | Anchors events into immutable time; extends the Archive domain. |
| Deterministic Signatures | Authority | Oath, Covenant | Ensures reproducible sovereign signing; aligns with Authority and Oath. |
| Devnet Consensus Sim | Legitimacy | Unity, Harmony | Validates consensus behavior; ensures governance legitimacy. |
| Badge-Service Integration | Index | Dignity, Continuum | Renders real-time verification badges; enhances public indexing. |
| Governance Contract POC | Sanctions | Oversight, Appeals | Prototypes voting and upgrade logic; aligns with governance enforcement. |
| Updater POC | Continuum | Transcendence, Genesis | Automates amendment updates; ensures continuity across epochs. |

## Governance Significance

The POC is not treated as peripheral experimentation. It is recognized as an accountable contribution that must:
1. Be documented in public governance materials
2. Be reviewable under formal criteria
3. Be archived as part of the lineage record
4. Remain compatible with the epoch-based governance system

## Status Summary

- ✓ Mapped to governance architecture
- ✓ Linked to ceremony and lineage records
- ✓ Positioned within the Genesis epoch framework
- ✓ Prepared for formal review and archival
