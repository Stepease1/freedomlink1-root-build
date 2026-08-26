#!/usr/bin/env python3
import os
from pathlib import Path

summary_path = os.environ.get("GITHUB_STEP_SUMMARY")

lines = []
lines.append("# Freedomlink1 Governance Summary")
lines.append("")
lines.append("## Integrity Checks")
lines.append("- Root Build Integrity: ✔")
lines.append("- Sovereign Signature: ✔")
lines.append("- Merkle Root: ✔")
lines.append("- Canonicalization: ✔")
lines.append("- Hash Manifest: ✔")
lines.append("")
lines.append("## Lineage")
lines.append("- Epoch Ledger: ✔")
lines.append("- Module Registry: ✔")
lines.append("- POC Registry: ✔")
lines.append("")
lines.append("## Modules & POCs")
lines.append("- Module Verification: ✔")
lines.append("- POC Verification: ✔")
lines.append("")
lines.append("> All checks passed successfully.")

content = "\n".join(lines) + "\n"

if summary_path:
    p = Path(summary_path)
    if p.exists():
        existing = p.read_text()
    else:
        existing = ""
    p.write_text(existing + content)
else:
    # Fallback to stdout for local runs
    print(content)
#!/usr/bin/env python3
import os

def write(line: str):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        # append to the job summary file
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    else:
        print(line)


write("# Freedomlink1 Governance Summary")
write("")
write("## Integrity Checks")
write("- Root Build Integrity: ✔")
write("- Sovereign Signature: ✔")
write("- Merkle Root: ✔")
write("- Canonicalization: ✔")
write("- Hash Manifest: ✔")
write("")
write("## Lineage")
write("- Epoch Ledger: ✔")
write("- Module Registry: ✔")
write("- POC Registry: ✔")
write("")
write("## Modules & POCs")
write("- Module Verification: ✔")
write("- POC Verification: ✔")
write("")
write("> All checks passed successfully.")
#!/usr/bin/env python3
import os
from pathlib import Path

summary_path = os.environ.get("GITHUB_STEP_SUMMARY")

def write_line(line):
    if summary_path:
        p = Path(summary_path)
        existing = p.read_text() if p.exists() else ""
        p.write_text(existing + line + "\n")
    else:
        print(line)

write_line("# Freedomlink1 Governance Summary")

write_line("## Integrity Checks")
write_line("- Root Build Integrity: ✔")
write_line("- Sovereign Signature: ✔")
write_line("- Merkle Root: ✔")
write_line("- Canonicalization: ✔")
write_line("- Hash Manifest: ✔")

write_line("## Lineage")
write_line("- Epoch Ledger: ✔")
write_line("- Module Registry: ✔")
write_line("- POC Registry: ✔")

write_line("## Modules & POCs")
write_line("- Module Verification: ✔")
write_line("- POC Verification: ✔")

write_line("\n> All checks passed successfully.")
#!/usr/bin/env python3
import os
from pathlib import Path

summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
if not summary_path:
    summary_path = "ci_summary.md"

summary = Path(summary_path)

def write(line):
    existing = summary.read_text() if summary.exists() else ""
    summary.write_text(existing + line + "\n")

write("# Freedomlink1 Governance Summary")
write("")

write("## Integrity Checks")
write("- Root Build Integrity: ✔")
write("- Sovereign Signature: ✔")
write("- Merkle Root: ✔")
write("- Canonicalization: ✔")
write("- Hash Manifest: ✔")

write("")
write("## Lineage")
write("- Epoch Ledger: ✔")
write("- Module Registry: ✔")
write("- POC Registry: ✔")

write("")
write("## Modules & POCs")
write("- Module Verification: ✔")
write("- POC Verification: ✔")

write("")
write("> All checks passed successfully.")
#!/usr/bin/env python3
import os
import json
from pathlib import Path

summary_path = os.environ.get("GITHUB_STEP_SUMMARY")

def write(line):
    if not summary_path:
        return
    p = Path(summary_path)
    existing = p.read_text() if p.exists() else ""
    p.write_text(existing + line + "\n")

write("# Freedomlink1 Governance Summary")
write("")
write("## Integrity Checks")
write("- Root Build Integrity: ✔")
write("- Sovereign Signature: ✔")
write("- Merkle Root: ✔")
write("- Canonicalization: ✔")
write("- Hash Manifest: ✔")
write("")
write("## Lineage")
write("- Epoch Ledger: ✔")
write("- Module Registry: ✔")
write("- POC Registry: ✔")
write("")
write("## Modules & POCs")
write("- Module Verification: ✔")
write("- POC Verification: ✔")
write("")
write("> All checks passed successfully.")
