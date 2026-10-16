/**
 * Freedomlink1 Unified Layer
 * Style Guide Linting Engine — Epoch-aware closure
 *
 * Implements the Style Guide Linting Ruleset (12 sections, 29 rule identifiers).
 */

import * as fs from "node:fs";
import * as path from "node:path";
import { execFileSync } from "node:child_process";

export interface LintDiagnostic {
    ruleId: string;
    line: number;
    message: string;
}

export interface LintResult {
    file: string;
    diagnostics: LintDiagnostic[];
}

interface SourceLine {
    number: number;
    text: string;
    inCodeFence: boolean;
    excludedList: boolean;
}

const ruleIds = [
    "ST-01", "ST-02", "ST-03",
    "CP-01", "CP-02", "CP-03",
    "SR-01", "SR-02", "SR-03",
    "AL-01", "AL-02",
    "VL-01", "VL-02",
    "CL-01", "CL-02",
    "HT-01",
    "EC-01", "EC-02",
    "FR-01", "FR-02", "FR-03", "FR-04", "FR-05", "FR-06",
    "TR-01", "TR-02",
    "DB-01",
    "SC-01", "SC-02"
] as const;

const canonicalPhrases = [
    "By authority of the Freedomlink1 Institution",
    "I affirm sovereign identity provenance",
    "I invoke Rootstone-I hardware trust binding",
    "I acknowledge lineage continuity",
    "I affirm alignment with PPTF Treasury Governance",
    "I acknowledge that verification is limited to local artifacts",
    "I declare the following action",
    "I record this action across all required institutional surfaces",
    "This ceremony does not grant authority.",
    "This verification does not validate runtime behavior."
];

const ceremonyPhrases = canonicalPhrases.filter((phrase) =>
    phrase.startsWith("By authority") ||
    phrase.startsWith("I affirm sovereign") ||
    phrase.startsWith("I invoke") ||
    phrase.startsWith("I acknowledge lineage") ||
    phrase.startsWith("This ceremony") ||
    phrase.startsWith("This verification")
);

const ritualSections = [
    "invocation",
    "authority evidence",
    "lineage",
    "identity",
    "hardware trust",
    "economic continuity",
    "verification boundaries",
    "declaration",
    "multi-surface recording",
    "closure"
];

const authorityVerbs = ["affirm", "acknowledge", "declare", "invoke", "record", "prepare", "reflect", "document", "align", "maintain"];
const institutionalTerms = [
    "Steward", "Institution", "Unified Layer", "Root Build", "Epoch",
    "Continuity Surfaces", "Verification Surfaces", "Hardware Trust",
    "Economic Continuity", "Lineage Anchors"
];

function sourceLines(text: string): SourceLine[] {
    const lines: SourceLine[] = [];
    let inFence = false;
    let inHtmlComment = false;
    let excludedList = false;
    let awaitingExcludedList = false;

    text.replace(/^\uFEFF/, "").split(/\r?\n/).forEach((line, index) => {
        const trimmed = line.trim();
        const fenceLine = /^\s*(```|~~~)/.test(line);
        const lineInFence = inFence || fenceLine;
        const isListItem = /^\s*(?:[-*+]|\d+[.)])\s/.test(line);

        if (/<!--/.test(line)) inHtmlComment = true;
        if (!trimmed && excludedList) excludedList = false;

        const startsExcludedList = /\b(?:reject|avoid|never imply|do not use|must not|forbidden|prohibited|not permitted)\b.*:\s*$/i.test(trimmed);
        if (startsExcludedList) awaitingExcludedList = true;
        if (awaitingExcludedList && isListItem) {
            excludedList = true;
            awaitingExcludedList = false;
        }

        lines.push({
            number: index + 1,
            text: line,
            inCodeFence: lineInFence || inHtmlComment,
            excludedList: excludedList && isListItem
        });

        if (/-->/.test(line)) inHtmlComment = false;
        if (fenceLine) inFence = !inFence;
        if (trimmed && !isListItem && !startsExcludedList) {
            excludedList = false;
            awaitingExcludedList = false;
        }
    });

    return lines;
}

function isNegated(text: string, matchIndex: number): boolean {
    const prefix = text.slice(Math.max(0, matchIndex - 64), matchIndex);
    return /\b(?:does not|do not|did not|cannot|can't|must not|never|not|without|no|reject|avoid|prohibit)\s+(?:\w+\s+){0,3}$/i.test(prefix);
}

function textWithoutMarkdownExamples(lines: SourceLine[]): string {
    return lines
        .filter((line) => !line.inCodeFence && !line.excludedList)
        .map((line) => line.text)
        .join("\n");
}

function add(diagnostics: LintDiagnostic[], ruleId: typeof ruleIds[number], line: number, message: string): void {
    diagnostics.push({ ruleId, line, message });
}

function findLine(lines: SourceLine[], pattern: RegExp): number {
    return lines.find((line) => !line.inCodeFence && pattern.test(line.text))?.number ?? 1;
}

export function lintText(file: string, text: string): LintResult {
    const lines = sourceLines(text);
    const prose = lines.filter((line) => !line.inCodeFence && !line.excludedList);
    const activeText = prose.map((line) => line.text).join("\n");
    const diagnostics: LintDiagnostic[] = [];
    const addTextMatch = (ruleId: typeof ruleIds[number], pattern: RegExp, message: string): void => {
        for (const line of prose) {
            pattern.lastIndex = 0;
            const match = pattern.exec(line.text);
            if (match && !isNegated(line.text, match.index)) add(diagnostics, ruleId, line.number, message);
        }
    };
    const documentName = path.basename(file).toLowerCase();
    const isCeremonyDocument = /ceremony|oath|invocation/.test(documentName);
    const isVerificationDocument = /verification|integrity|audit/i.test(documentName) || /\bverification (?:report|procedure|result|scope)\b/i.test(activeText);
    const isContinuityDocument = /continuity|epoch|lineage/i.test(documentName) || /\bcontinuity (?:report|record|procedure)\b/i.test(activeText);
    const isHardwareDocument = /hardware|rootstone/i.test(documentName) || /\bhardware trust (?:record|binding|procedure)\b/i.test(activeText);
    const isEconomicDocument = /economic|treasury|pptf/i.test(documentName) || /\b(?:treasury governance|economic continuity)\b/i.test(activeText);

    // ST-01: deterministic high-confidence metaphor and flourish indicators.
    addTextMatch("ST-01", /\b(?:guiding light|north star|beacon of|tapestry of|journey toward|at the heart of|watershed moment|game changer)\b/i, "Figurative or rhetorical flourish detected.");

    // ST-02: a bounded vocabulary catches overtly emotional or persuasive framing.
    addTextMatch("ST-02", /\b(?:thrilled|delighted|proud|inspiring|incredible|unprecedented|revolutionary|remarkable|exciting|must trust)\b/i, "Emotional or persuasive framing detected.");

    // ST-03: require prose to use declarative sentences rather than questions or direct appeals.
    for (const line of prose) {
        if (/\?\s*$/.test(line.text) || /^\s*(?:please\s+)?(?:consider|remember|imagine|trust)\b/i.test(line.text)) {
            add(diagnostics, "ST-03", line.number, "Use declarative, intentional phrasing.");
        }
    }

    // CP-01 and CP-03: ceremony phrasing applies to ceremony artifacts, not every document.
    if (isCeremonyDocument) {
        if (!canonicalPhrases.some((phrase) => activeText.includes(phrase))) {
            add(diagnostics, "CP-01", 1, "Ceremony document must use at least one exact canonical institutional phrase.");
        }
        const blockquote = prose.filter((line) => /^\s*>/.test(line.text)).map((line) => line.text).join("\n");
        for (const phrase of ceremonyPhrases) {
            if (!blockquote.includes(phrase)) {
                add(diagnostics, "CP-03", 1, `Ceremony script is missing the exact phrase: ${phrase}`);
            }
        }
    }

    // CP-02: recognize common near-miss variants while leaving unrelated prose alone.
    const substitutions = [
        /By authority of Freedomlink1 Institution/i,
        /I affirm (?:my )?identity provenance/i,
        /I invoke Rootstone-I (?:hardware )?attestation/i,
        /I acknowledge (?:the )?lineage inheritance/i
    ];
    for (const pattern of substitutions) addTextMatch("CP-02", pattern, "Use the exact canonical institutional phrase instead of a paraphrase.");

    // SR-01 through SR-03: apply ordered ritual checks when the document uses this structure.
    const headings = prose.filter((line) => /^\s{0,3}#{1,6}\s/.test(line.text));
    const ritualMatches = headings.map((line) => ({
        line,
        index: ritualSections.findIndex((section) => new RegExp(`\\b${section.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\b`, "i").test(line.text))
    })).filter((item) => item.index >= 0);
    const hasRitualOpeningAndClosure = ritualMatches.some((item) => item.index === 0) && ritualMatches.some((item) => item.index === 9);
    if (isCeremonyDocument || hasRitualOpeningAndClosure) {
        const found = new Set(ritualMatches.map((item) => item.index));
        for (let index = 0; index < ritualSections.length; index++) {
            if (!found.has(index)) add(diagnostics, "SR-02", 1, `Missing required ritual section: ${ritualSections[index]}.`);
        }
        const sequence = ritualMatches.map((item) => item.index);
        if (sequence.some((value, index) => index > 0 && value < sequence[index - 1])) {
            add(diagnostics, "SR-03", ritualMatches[0]?.line.number ?? 1, "Ritual sections are out of sovereign order.");
        }
        if (ritualMatches[0]?.index !== 0 || ritualMatches[ritualMatches.length - 1]?.index !== 9) {
            add(diagnostics, "SR-01", ritualMatches[0]?.line.number ?? 1, "Ritual sequence must begin with Invocation and end with Closure.");
        }
    }

    // AL-01: reject active authority claims, while allowing negated boundaries and reject lists.
    addTextMatch("AL-01", /\b(?:authoriz(?:e|es|ed|ing)|validat(?:e|es|ed|ing)|enforc(?:e|es|ed|ing)|attest(?:s|ed|ing)?|guarantee(?:s|d|ing)?|certif(?:y|ies|ied|ying)|approv(?:e|es|ing))\b/i, "Authority-implying verb detected outside a negated boundary.");

    // AL-02: institutional prose must use at least one approved bounded action verb.
    if (!new RegExp(`\\b(?:${authorityVerbs.join("|")})\\b`, "i").test(activeText)) {
        add(diagnostics, "AL-02", 1, "Use at least one authority-bounded verb from the charter vocabulary.");
    }

    // VL-01: verification artifacts must state their local scope and governed-write boundary.
    if (isVerificationDocument) {
        const requiredVerificationStatements = [
            /verifies? local artifacts only/i,
            /does not validate runtime behavior|does not validate runtime correctness/i,
            /updates? `?last_check`?/i,
            /steward[- ]initiated/i
        ];
        requiredVerificationStatements.forEach((pattern) => {
            if (!pattern.test(activeText)) add(diagnostics, "VL-01", 1, `Verification boundary missing: ${pattern.source}.`);
        });
    }

    // VL-02: reject claims unless the document explicitly negates them.
    for (const claim of ["runtime correctness", "chain-state correctness", "economic execution correctness", "hardware attestation", "identity attestation"]) {
        addTextMatch("VL-02", new RegExp(`\\b${claim.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\b`, "i"), `Unsupported verification claim: ${claim}.`);
    }

    // CL-01 and CL-02: continuity checks are scoped to continuity and epoch artifacts.
    if (isContinuityDocument) {
        for (const claim of ["perform an epoch transition", "advance the epoch", "execute continuity"]) {
            addTextMatch("CL-01", new RegExp(`\\b${claim}\\b`, "i"), `Autonomous continuity claim detected: ${claim}.`);
        }
        for (const phrase of ["prepares an epoch transition", "aligns continuity surfaces", "records continuity events", "acknowledges lineage anchors"]) {
            if (!new RegExp(`\\b${phrase}\\b`, "i").test(activeText)) add(diagnostics, "CL-02", 1, `Required continuity phrasing is missing: ${phrase}.`);
        }
    }

    // HT-01: hardware artifacts distinguish declared metadata from attestation.
    if (isHardwareDocument) {
        for (const claim of ["hardware attestation", "hardware verification", "hardware enforcement"]) {
            addTextMatch("HT-01", new RegExp(`\\b${claim}\\b`, "i"), `Unsupported hardware trust claim: ${claim}.`);
        }
        for (const phrase of ["declared hardware identity", "hardware trust invocation", "physical sovereignty binding"]) {
            if (!new RegExp(`\\b${phrase}\\b`, "i").test(activeText)) add(diagnostics, "HT-01", 1, `Required declared-hardware phrasing is missing: ${phrase}.`);
        }
    }

    // EC-01 and EC-02: economic artifacts state policy, not runtime execution.
    if (isEconomicDocument) {
        for (const claim of ["economic correctness", "treasury execution validation", "runtime economic verification"]) {
            addTextMatch("EC-01", new RegExp(`\\b${claim}\\b`, "i"), `Unsupported economic claim: ${claim}.`);
        }
        for (const phrase of ["declared economic configuration", "economic continuity alignment", "treasury governance policy"]) {
            if (!new RegExp(`\\b${phrase}\\b`, "i").test(activeText)) add(diagnostics, "EC-02", 1, `Required policy-aligned economic phrasing is missing: ${phrase}.`);
        }
    }

    // FR-01: one H1, and no skipped heading levels.
    const headingLevels = headings.map((line) => /^\s{0,3}(#{1,6})/.exec(line.text)?.[1].length ?? 0);
    if (headingLevels.filter((level) => level === 1).length !== 1 || headingLevels[0] !== 1 || headingLevels.some((level, index) => index > 0 && level > headingLevels[index - 1] + 1)) {
        add(diagnostics, "FR-01", headings[0]?.number ?? 1, "Use one H1 title and do not skip heading levels.");
    }

    // FR-02: nested bullet lists are not permitted.
    for (const line of prose) {
        if (/^\s{2,}[-*+]\s/.test(line.text)) add(diagnostics, "FR-02", line.number, "Nested bullet lists are not permitted.");
    }

    // FR-03: test emoji presentation characters, not ordinary non-ASCII punctuation.
    for (const line of prose) {
        if (/[\p{Emoji_Presentation}\uFE0F]/u.test(line.text)) add(diagnostics, "FR-03", line.number, "Emoji characters are not permitted.");
    }

    // FR-04: ceremony script lines must be blockquoted.
    if (isCeremonyDocument) {
        for (const line of prose) {
            if (/^\s*(?:I (?:affirm|invoke|acknowledge|declare)|By authority of)\b/.test(line.text) && !/^\s*>/.test(line.text)) {
                add(diagnostics, "FR-04", line.number, "Ceremony script text must use blockquote formatting.");
            }
        }
    }

    // FR-05: command lines must appear inside a fenced code block.
    let inFence = false;
    for (const line of lines) {
        const fenceLine = /^\s*(```|~~~)/.test(line.text);
        if (!inFence && !fenceLine && /^\s*(?:\$\s+)?(?:npm|npx|node|git|python(?:3)?|pip|powershell|pwsh|bash)\s+/.test(line.text)) {
            add(diagnostics, "FR-05", line.number, "Commands must be placed in fenced code blocks.");
        }
        if (fenceLine) inFence = !inFence;
    }

    // FR-06: the section marker may only appear in a Markdown heading.
    for (const line of prose) {
        const validMarker = /^\s{0,3}#{1,6}\s+(?:\d+[.)]\s*)?✦(?:\s|$)/.test(line.text);
        if (line.text.includes("✦") && !validMarker) {
            add(diagnostics, "FR-06", line.number, "The section marker is only permitted in headings.");
        }
    }

    // TR-01: reject common capitalization variants of canonical institutional terms.
    const termVariants: Array<[RegExp, string, RegExp?]> = [
        [/\bUnified layer\b/g, "Unified Layer"],
        [/\bRoot build\b/g, "Root Build"],
        [/\bContinuity surfaces\b/g, "Continuity Surfaces", /\baligns continuity surfaces\b/i],
        [/\bVerification surfaces\b/g, "Verification Surfaces"],
        [/\bHardware trust\b/g, "Hardware Trust", /\b(?:hardware trust invocation|Rootstone-I hardware trust binding)\b/i],
        [/\bEconomic continuity\b/g, "Economic Continuity", /\beconomic continuity (?:alignment|defines policy)\b/i],
        [/\bLineage anchors\b/g, "Lineage Anchors", /\backnowledges lineage anchors\b/i]
    ];
    for (const line of prose) {
        for (const [pattern, canonical, allowedPhrase] of termVariants) {
            if (/^\s{0,3}#{1,6}\s/.test(line.text) && pattern.test(line.text) && !(allowedPhrase?.test(line.text))) {
                add(diagnostics, "TR-01", line.number, `Use the canonical term capitalization: ${canonical}.`);
            }
            pattern.lastIndex = 0;
        }
    }
    void institutionalTerms;

    // TR-02: explicitly emphasized institutional terms must be defined in the same document.
    const emphasizedTerms = [...activeText.matchAll(/\*\*([A-Z][A-Za-z0-9 -]{2,40})\*\*/g)];
    for (const match of emphasizedTerms) {
        const term = match[1].trim();
        if (institutionalTerms.includes(term)) continue;
        const definition = new RegExp(`\\b${term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\b.{0,80}\\b(?:means|refers to|is defined as)\\b`, "i");
        if (!definition.test(activeText)) {
            const line = findLine(lines, new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));
            add(diagnostics, "TR-02", line, `Define emphasized institutional term: ${term}.`);
        }
    }

    // DB-01: all six boundary dimensions must be stated explicitly.
    const boundaryChecks: Array<[RegExp, string]> = [
        [/\b(?:describes|documents|records|defines|specifies|supports|establishes)\b/i, "purpose"],
        [/\b(?:does not|doesn't|not intended to|does not itself)\b/i, "non-purpose"],
        [/\b(?:authority|governance approval|governing instrument)\b/i, "deferred authority"],
        [/\b(?:does not validate|cannot validate|verification is limited|not independently verified)\b/i, "verification limits"],
        [/\b(?:runtime behavior|runtime correctness|runtime execution)\b/i, "runtime boundary"],
        [/\b(?:autonomous|autonomously)\b/i, "autonomous-action boundary"]
    ];
    for (const [pattern, boundary] of boundaryChecks) {
        if (!pattern.test(activeText)) add(diagnostics, "DB-01", 1, `Document boundary is missing: ${boundary}.`);
    }

    // SC-01 and SC-02: require the institutional footer for the document's epoch.
    const finalLines = text.replace(/\s+$/, "").split(/\r?\n/).slice(-2).map((line) => line.replace(/^>\s?/, "").trim());
    const footerMatch = finalLines[1]?.match(/^(?:.+|\[Document Name\]) — Epoch (\d+)$/);
    const ledgerPath = path.resolve(process.cwd(), "lineage/epoch-ledger.md");
    let activeEpoch = 6;
    if (fs.existsSync(ledgerPath)) {
        const ledger = fs.readFileSync(ledgerPath, "utf8");
        const activeMatch = ledger.match(/^\*\*Current Epoch\*\*:\s*Epoch\s+(\d+)\s+—\s+Active\s*$/m)
            ?? ledger.match(/^## Current Epoch\s*\r?\n\*\*Epoch\s+(\d+)\s+—\s+Active\*\*\s*$/m);
        if (activeMatch) activeEpoch = Number(activeMatch[1]);
    }

    const leadingText = lines.slice(0, 40).map((line) => line.text).join("\n");
    const filenameEpoch = path.basename(file).match(/(?:^|[_-])epoch[_-]?(\d+)(?:[_-]|\.|$)/i);
    const metadataEpoch = leadingText.match(/^\s*(?:\*\*Epoch:\*\*|epoch:)\s*(\d+)\b/im);
    const headingEpoch = leadingText.match(/^\s*#{1,6}\s+Epoch\s+(\d+)\b/im);
    const declaredEpoch = filenameEpoch ?? metadataEpoch ?? headingEpoch;
    const footerEpoch = footerMatch ? Number(footerMatch[1]) : undefined;
    const documentEpoch = declaredEpoch
        ? Number(declaredEpoch[1])
        : footerEpoch !== undefined && footerEpoch < activeEpoch
            ? footerEpoch
            : activeEpoch;
    const supportedEpoch = Number.isInteger(documentEpoch) && documentEpoch >= 1 && documentEpoch <= 7;
    const hasClosure = finalLines.length === 2 &&
        finalLines[0] === "Freedomlink1 Unified Layer" &&
        supportedEpoch && footerEpoch === documentEpoch;
    if (!hasClosure) {
        add(diagnostics, "SC-01", lines.length, "Required closing block is missing or altered.");
        const message = supportedEpoch
            ? `Document must end with its sovereign Epoch ${documentEpoch} closure.`
            : "Footer must use a recognized epoch identifier from 1 through 7.";
        add(diagnostics, "SC-02", lines.length, message);
    }

    const knownRuleIds: Set<string> = new Set(ruleIds);
    for (const diagnostic of diagnostics) {
        if (!knownRuleIds.has(diagnostic.ruleId)) throw new Error(`Unknown rule identifier: ${diagnostic.ruleId}`);
    }

    return { file, diagnostics };
}

function collectMarkdownFiles(target: string): string[] {
    const resolved = path.resolve(target);
    if (!fs.existsSync(resolved)) throw new Error(`Path does not exist: ${target}`);
    const stat = fs.statSync(resolved);
    if (stat.isFile()) return resolved.toLowerCase().endsWith(".md") ? [resolved] : [];

    const files: string[] = [];
    for (const entry of fs.readdirSync(resolved, { withFileTypes: true })) {
        if (entry.name === ".git" || entry.name === "node_modules" || entry.name === "dist") continue;
        const entryPath = path.join(resolved, entry.name);
        if (entry.isDirectory()) files.push(...collectMarkdownFiles(entryPath));
        else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) files.push(entryPath);
    }
    return files;
}

function gitMarkdownFiles(mode: "staged" | "changed"): string[] {
    let args: string[];
    if (mode === "staged") {
        args = ["diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "*.md"];
    } else {
        const baseRef = process.env.GITHUB_BASE_REF;
        const pushBefore = process.env.FL1_LINT_BASE_REF;
        args = baseRef
            ? ["diff", "--name-only", "--diff-filter=ACMR", `origin/${baseRef}...HEAD`, "--", "*.md"]
            : pushBefore && !/^0+$/.test(pushBefore)
                ? ["diff", "--name-only", "--diff-filter=ACMR", `${pushBefore}...HEAD`, "--", "*.md"]
                : ["diff", "--name-only", "--diff-filter=ACMR", "HEAD^", "HEAD", "--", "*.md"];
    }
    const output = execFileSync("git", args, { encoding: "utf8" });
    return output.split(/\r?\n/).filter((file) => file.trim() && fs.existsSync(file));
}

export function lintFile(filePath: string): LintResult {
    const resolved = path.resolve(filePath);
    return lintText(resolved, fs.readFileSync(resolved, "utf8"));
}

export function lintFiles(filePaths: string[]): LintResult[] {
    return filePaths.flatMap((filePath) => collectMarkdownFiles(filePath)).map(lintFile);
}

function printUsage(): void {
    console.log("Usage: node style_guide_linter.js [--staged | --changed] [file-or-directory ...]");
    console.log("With no arguments, lint Markdown files under docs/.");
}

function runCli(args: string[]): number {
    if (args.includes("--help") || args.includes("-h")) {
        printUsage();
        return 0;
    }

    try {
        let files: string[];
        if (args.includes("--staged") && args.includes("--changed")) throw new Error("Choose either --staged or --changed.");
        if (args.includes("--staged")) files = gitMarkdownFiles("staged");
        else if (args.includes("--changed")) files = gitMarkdownFiles("changed");
        else {
            const targets = args.filter((arg) => !arg.startsWith("-"));
            files = (targets.length ? targets : ["docs"]).flatMap(collectMarkdownFiles);
        }

        if (files.length === 0) {
            console.log("No Markdown files selected.");
            return 0;
        }

        let failed = false;
        for (const result of files.map(lintFile)) {
            const relativeFile = path.relative(process.cwd(), result.file);
            if (result.diagnostics.length) {
                failed = true;
                console.error(`FAIL ${relativeFile}`);
                for (const diagnostic of result.diagnostics) {
                    console.error(`  ${diagnostic.ruleId} line ${diagnostic.line}: ${diagnostic.message}`);
                }
            } else {
                console.log(`PASS ${relativeFile}`);
            }
        }
        return failed ? 1 : 0;
    } catch (error) {
        console.error(error instanceof Error ? error.message : String(error));
        printUsage();
        return 2;
    }
}

if (require.main === module) {
    process.exitCode = runCli(process.argv.slice(2));
}