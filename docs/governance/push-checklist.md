# Governance Push Checklist

Before pushing:

1. Ensure no Git lock exists:
   - Delete `.git/index.lock` if present.

2. Ensure repo folder is writable:
   - Remove Windows "Read-only" attribute.

3. Ensure repo is NOT inside OneDrive:
   - Move to a local folder if needed.

4. Validate tasks.json:
   - Must be valid JSON.
   - No trailing commas.
   - No hidden Unicode characters.

5. Validate governance docs:
   - docs/governance/runner.md exists.
   - docs/badges/ exist.
   - ceremonies/ exist.
   - governance/ exist.

6. Run governance checks locally:
   - Ctrl+Shift+B → Run Governance Checks

7. Commit via terminal if VS Code GUI hangs:
   - git add .
   - git commit -m "governance: update"
   - git push
