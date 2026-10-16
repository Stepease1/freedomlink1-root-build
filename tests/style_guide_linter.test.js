const assert = require("node:assert/strict");
const test = require("node:test");
const { lintText } = require("../dist/tools/style_guide_linter.js");

const validDocument = [
    "# Institutional Record",
    "",
    "This document records a declared local configuration and describes its purpose.",
    "It does not grant authority; governance approval evidence remains authoritative.",
    "Verification is limited to local artifacts and does not validate runtime behavior.",
    "Runtime behavior and autonomous action are outside this document's scope.",
    "The steward must record the declared configuration.",
    "",
    "Freedomlink1 Unified Layer  ",
    "Institutional Record — Epoch 6"
].join("\n");

function ruleIds(file, text) {
    return new Set(lintText(file, text).diagnostics.map(({ ruleId }) => ruleId));
}

test("accepts a document within the declared boundaries", () => {
    assert.deepEqual(lintText("record.md", validDocument).diagnostics, []);
});

test("preserves an explicit Epoch 6 footer after the ledger advances to Epoch 7", () => {
    const epoch6Document = validDocument.replace(
        "The steward must record the declared configuration.",
        "This record prepares an epoch transition, aligns continuity surfaces, records continuity events, and acknowledges lineage anchors. The steward records the declared configuration."
    );
    assert.deepEqual(lintText("epoch6_record.md", epoch6Document).diagnostics, []);
});

test("requires an explicit Epoch 7 document to use an Epoch 7 footer", () => {
    const epoch7Document = validDocument.replace(
        "The steward must record the declared configuration.",
        "This record prepares an epoch transition, aligns continuity surfaces, records continuity events, and acknowledges lineage anchors. The steward records the declared configuration."
    )
        .replace("# Institutional Record", "# Epoch 7 — Institutional Record")
        .replace("Institutional Record — Epoch 6", "Institutional Record — Epoch 7");
    assert.deepEqual(lintText("epoch7_record.md", epoch7Document).diagnostics, []);

    const staleFooter = epoch7Document.replace("Institutional Record — Epoch 7", "Institutional Record — Epoch 6");
    assert.ok(ruleIds("epoch7_record.md", staleFooter).has("SC-01"));
    assert.ok(ruleIds("epoch7_record.md", staleFooter).has("SC-02"));
});

test("defaults unmarked documents to the active ledger epoch", () => {
    const currentDocument = validDocument.replace("Institutional Record — Epoch 6", "Institutional Record — Epoch 7");
    assert.deepEqual(lintText("record.md", currentDocument).diagnostics, []);
});

test("rejects footer epoch identifiers outside the supported range", () => {
    const unsupportedDocument = validDocument
        .replace("# Institutional Record", "# Epoch 8 — Institutional Record")
        .replace("Institutional Record — Epoch 6", "Institutional Record — Epoch 8");
    assert.ok(ruleIds("epoch8_record.md", unsupportedDocument).has("SC-02"));
});

test("implements all 29 rules with deterministic diagnostics", () => {
    const ritualHeadings = [
        "# Ceremony Record",
        "## ✦ Closure",
        "## ✦ Invocation"
    ].join("\n");
    const cases = [
        ["tone.md", "A guiding light illuminates an incredible future?"],
        ["tone.md", "Please consider this proposal."],
        ["ceremony.md", `${ritualHeadings}\n\nI affirm this declaration.`],
        ["phrasing.md", "By authority of Freedomlink1 Institution"],
        ["authority.md", "The steward will approve the request."],
        ["plain.md", "The specification is complete."],
        ["verification.md", "Verification reports runtime correctness."],
        ["continuity.md", "The process must advance the epoch."],
        ["continuity.md", "This continuity report is ready."],
        ["hardware.md", "The system provides hardware attestation."],
        ["economic.md", "This confirms economic correctness."],
        ["economic.md", "The treasury governance report is ready."],
        ["headings.md", "# Title\n### Skipped level"],
        ["lists.md", "# Title\n\n- Parent\n  - Nested"],
        ["emoji.md", "# Title\n\nApproved ✅"],
        ["ceremony.md", "# Ceremony\n\nI affirm this action."],
        ["commands.md", "# Title\n\nnpm run build"],
        ["marker.md", "# Title\n\n✦ outside heading"],
        ["terms.md", "# Title\n\n## Hardware trust"],
        ["terms.md", "# Title\n\n**Quantum Custodians** are referenced."],
        ["plain.md", "# Title\n\nA short description."],
        ["closure.md", "# Title\n\nNo institutional closure." ]
    ];
    const observed = new Set(cases.flatMap(([file, text]) => [...ruleIds(file, text)]));
    const expected = [
        "ST-01", "ST-02", "ST-03", "CP-01", "CP-02", "CP-03",
        "SR-01", "SR-02", "SR-03", "AL-01", "AL-02", "VL-01", "VL-02",
        "CL-01", "CL-02", "HT-01", "EC-01", "EC-02", "FR-01", "FR-02",
        "FR-03", "FR-04", "FR-05", "FR-06", "TR-01", "TR-02", "DB-01",
        "SC-01", "SC-02"
    ];
    assert.deepEqual([...observed].sort(), expected.sort());
});

test("accepts canonical marker headings and exempt rejection examples", () => {
    const result = lintText("rules.md", [
        "# ✦ Editorial Rules",
        "",
        "## ✦ 1. Boundaries",
        "",
        "Reject documents containing:",
        "",
        "- enforce authority",
        "- hardware attestation",
        "",
        "This document describes the rules. It does not grant authority. Governance approval evidence controls.",
        "Verification is limited to local artifacts. Runtime behavior is outside scope. Autonomous action is not performed.",
        "The steward records the declared configuration.",
        "",
        "Freedomlink1 Unified Layer  ",
        "Editorial Rules — Epoch 6"
    ].join("\n"));
    assert.deepEqual(result.diagnostics, []);
});