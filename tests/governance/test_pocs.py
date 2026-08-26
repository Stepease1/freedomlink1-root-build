import json

def test_pocs_have_domains():
    with open("lineage/poc_registry.json") as f:
        registry = json.load(f)
    for p in registry["pocs"]:
        assert "domain_primary" in p
