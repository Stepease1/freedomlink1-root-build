def test_ceremony_files_exist():
    import os
    ceremonies = [
        "ceremonies/poc_graduation_01.md",
        "ceremonies/module_activation_02.md",
        "ceremonies/epoch_advancement.md"
    ]
    for c in ceremonies:
        assert os.path.exists(c)
