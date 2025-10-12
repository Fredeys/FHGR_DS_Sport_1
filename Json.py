!pip install pathlib
from pathlib import Path

# Pfad zum Polar-Export
data_dir = Path("/Users/frederickurbel@MacBook-Air-von-Frederic/Downloads/polar-user-data-export_7e32ae84-89cf-4c56-b29e-d089feef4207")

# Liste aller JSON-Dateien im Ordner
json_files = list(data_dir.glob("*.json"))
print(f"{len(json_files)} JSON-Dateien gefunden:")
for f in json_files:
    print(" -", f.name)
