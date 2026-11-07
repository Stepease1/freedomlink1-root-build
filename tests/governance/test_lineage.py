import json

def test_lineage_valid():
    with open("lineage/epoch_ledger.json") as f:
        ledger = json.load(f)
    assert "epochs" in ledger
    assert len(ledger["epochs"]) > 0
    active_epochs = [epoch["epoch"] for epoch in ledger["epochs"] if epoch.get("status") == "active"]
    assert active_epochs == [ledger["current_epoch"]]
