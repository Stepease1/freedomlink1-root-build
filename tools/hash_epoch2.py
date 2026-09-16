from pathlib import Path
import hashlib

p = Path('C:/Users/crazy/Freedomlink1-root-build/docs/governance/Institutional_Genesis_Seal_Epoch_2.md')
print(hashlib.sha256(p.read_bytes()).hexdigest())
