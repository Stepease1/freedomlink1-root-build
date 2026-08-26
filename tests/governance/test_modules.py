import json

def test_modules_have_hashes():
    with open("lineage/module_registry.json") as f:
        registry = json.load(f)
    for m in registry["modules"]:
        assert len(m["hash"]) > 0
