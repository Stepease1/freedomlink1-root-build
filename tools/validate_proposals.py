#!/usr/bin/env python3
import sys
from pathlib import Path

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
PROPOSALS = ROOT / "docs" / "proposals"

REQUIRED_SECTIONS = [
    "PREAMBLE",
    "I.",
    "II.",
    "III.",
    "IV.",
    "V.",
    "VI.",
    "VII.",
]


def validate_markdown(path: Path):
    md = MarkdownIt()
    try:
        md.parse(path.read_text(encoding="utf-8"))
        print(f"[OK] Markdown valid: {path.name}")
        return True
    except Exception as error:
        print(f"[ERR] Markdown parse failed for {path.name}: {error}")
        return False


def validate_structure(path: Path):
    text = path.read_text(encoding="utf-8")
    ok = True
    for section in REQUIRED_SECTIONS:
        if section not in text:
            print(f"[ERR] Missing required section '{section}' in {path.name}")
            ok = False
    if ok:
        print(f"[OK] Structure valid: {path.name}")
    return ok


def validate_index():
    index = PROPOSALS / "index.md"
    if not index.exists():
        print("[ERR] Missing proposals index.md")
        return False

    text = index.read_text(encoding="utf-8")
    ok = True

    for file in PROPOSALS.glob("*.md"):
        if file.name == "index.md":
            continue
        if file.name not in text:
            print(f"[ERR] index.md missing link to {file.name}")
            ok = False

    if ok:
        print("[OK] index.md links validated")
    return ok


def main():
    ok = True

    for file in PROPOSALS.glob("*.md"):
        if file.name == "index.md":
            continue
        ok &= validate_markdown(file)
        ok &= validate_structure(file)

    ok &= validate_index()

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
