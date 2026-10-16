# ✦ Freedomlink1 Style Guide Linting Ruleset

*Editorial Enforcement — Epoch 6*

The Style Guide Linting Ruleset defines automated checks aligned with the [Sovereign Editorial Charter](freedomlink1_institutional_style_guide.md) across all Freedomlink1 documents. These rules preserve institutional tone, authority boundaries, verification limits, continuity phrasing, formatting discipline, and sovereign closure across the Unified Layer.

This ruleset applies to all governance, continuity, verification, hardware trust, economic, lineage, identity, automation, and stewardship artifacts.

## ✦ 1. Sovereign Tone Rules

### Rule ST-01 — No Metaphor or Flourish

Reject documents containing figurative language, metaphor, or rhetorical flourish.

### Rule ST-02 — No Emotional Framing

Reject documents containing emotional adjectives or persuasive tone.

### Rule ST-03 — Declarative Tone Required

Require declarative, intentional phrasing in all sections.

## ✦ 2. Canonical Phrasing Rules

### Rule CP-01 — Canonical Phrases Must Match Exactly

Verify presence of required institutional phrases when applicable.

### Rule CP-02 — Reject Non-Canonical Substitutions

Reject documents that paraphrase sovereign phrases.

### Rule CP-03 — Ceremony Phrases Must Be Exact

Check for exact matches of:

- “By authority of the Freedomlink1 Institution…”
- “I affirm sovereign identity provenance…”
- “I invoke Rootstone-I hardware trust binding…”
- “I acknowledge lineage continuity…”
- “This ceremony does not grant authority.”
- “This verification does not validate runtime behavior.”

## ✦ 3. Structural Ritual Rules

### Rule SR-01 — Required Section Order

Documents must follow the ten-step sovereign structure:

1. Invocation
2. Authority Evidence
3. Lineage
4. Identity
5. Hardware Trust
6. Economic Continuity
7. Verification Boundaries
8. Declaration
9. Multi-Surface Recording
10. Closure

### Rule SR-02 — Reject Missing Sections

Reject documents missing any required structural element.

### Rule SR-03 — Reject Reordered Sections

Reject documents that alter the sovereign sequence.

## ✦ 4. Authority-Safe Language Rules

### Rule AL-01 — Reject Authority-Implying Verbs

Reject documents containing:

- authorize
- validate
- enforce
- attest
- guarantee
- certify
- approve, unless referencing evidence

### Rule AL-02 — Require Authority-Bounded Verbs

Require use of:

- affirm
- acknowledge
- declare
- invoke
- record
- prepare
- reflect
- align
- maintain

## ✦ 5. Verification-Safe Language Rules

### Rule VL-01 — Verification Boundaries Must Be Stated

Require explicit statements that verification:

- verifies local artifacts only
- does not validate runtime behavior
- updates `last_check`
- is steward-initiated

### Rule VL-02 — Reject Runtime Claims

Reject documents implying:

- runtime correctness
- chain-state correctness
- economic execution correctness
- hardware attestation
- identity attestation

## ✦ 6. Continuity-Safe Language Rules

### Rule CL-01 — Reject Autonomous Epoch Claims

Reject documents implying:

- performing an epoch transition
- advancing the epoch
- executing continuity

### Rule CL-02 — Require Continuity-Aligned Phrasing

Require:

- prepares an epoch transition
- aligns continuity surfaces
- records continuity events
- acknowledges lineage anchors

## ✦ 7. Hardware Trust Language Rules

### Rule HT-01 — Rootstone-I Must Be Declared, Not Attested

Reject:

- hardware attestation
- hardware verification
- hardware enforcement

Require:

- declared hardware identity
- hardware trust invocation
- physical sovereignty binding

## ✦ 8. Economic Continuity Language Rules

### Rule EC-01 — Reject Runtime Economic Claims

Reject:

- economic correctness
- treasury execution validation
- runtime economic verification

### Rule EC-02 — Require Policy-Aligned Phrasing

Require:

- declared economic configuration
- economic continuity alignment
- treasury governance policy

## ✦ 9. Formatting Rules

### Rule FR-01 — Header Hierarchy

Require:

- H1 for document title
- H2 for major sections
- H3 for subsections

### Rule FR-02 — Single-Level Lists Only

Reject nested bullet lists.

### Rule FR-03 — No Emojis

Reject any emoji characters.

### Rule FR-04 — Ceremony Scripts Must Use Blockquotes

Require blockquote formatting for ritual text.

### Rule FR-05 — Commands Must Use Code Blocks

Require fenced code blocks for commands.

### Rule FR-06 — Section Marker Only

Reject the section marker when used outside section headers.

## ✦ 10. Terminology Rules

### Rule TR-01 — Required Institutional Terms

Require consistent use of:

- Steward
- Institution
- Unified Layer
- Root Build
- Epoch
- Continuity Surfaces
- Verification Surfaces
- Hardware Trust
- Economic Continuity
- Lineage Anchors

### Rule TR-02 — Reject Undefined Terms

Reject documents introducing new institutional terms without definition.

## ✦ 11. Document Boundary Rules

### Rule DB-01 — Boundary Declaration Required

Documents must explicitly state:

- what they do
- what they do not do
- what authority they defer to
- what verification they cannot claim
- what runtime behavior they cannot imply
- what autonomous action they cannot perform

Reject documents lacking boundary declarations.

## ✦ 12. Sovereign Closure Rules

### Rule SC-01 — Required Closing Block

Require the institutional footer format:

> Freedomlink1 Unified Layer  
> [Document Name] — Epoch N

The footer epoch is selected as follows:

1. Use an explicit epoch declared in document metadata, the title, or the filename when present. This preserves historical Epoch 6 closures after the canonical ledger advances.
2. Otherwise, use the active epoch recorded in `lineage/epoch-ledger.md`.
3. For an unmarked historical document that already has a valid earlier-epoch footer, preserve that footer instead of rewriting it to the active epoch.

Epoch identifiers 1 through 7 are recognized. New Epoch 7 documents must declare Epoch 7 and close with an Epoch 7 footer. Historical Epoch 1–6 documents retain their declared epoch footer.

### Rule SC-02 — Reject Missing or Altered Closure

Reject documents without the required institutional closing block or with a footer epoch that does not match the document's declared or applicable active epoch.

## ✦ Closing

The Style Guide Linting Ruleset applies the Sovereign Editorial Charter and preserves Freedomlink1’s institutional voice, authority boundaries, verification limits, continuity alignment, and sovereign identity.

Freedomlink1 Unified Layer  
Style Guide Linting Ruleset — Epoch 6