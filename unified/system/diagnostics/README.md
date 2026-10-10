# CIM Introspection Diagnostics

`cim-introspection.ps1` collects a local system profile through `Get-CimInstance`.
Run the smoke test from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File ./unified/system/diagnostics/test-introspection.ps1
```

The profile includes hardware serial numbers and network adapter MAC addresses.
Treat the output as sensitive and do not publish it without reviewing it first.