# Epoch Rollback Procedure

Rollback is permitted only under critical corruption.

## Steps

1. Identify last valid epoch
2. Restore epoch ledger
3. Regenerate hash manifest
4. Regenerate Merkle root
5. Steward signs restored artifacts
