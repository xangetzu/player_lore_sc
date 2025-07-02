import json
import requests
from pathlib import Path

# Dynamically resolve output directory
base_dir = Path(__file__).resolve().parent.parent
output_dir = base_dir / "external_data" / "scrunpacked"
output_dir.mkdir(parents=True, exist_ok=True)

# Define base URL and filenames
base_url = "https://raw.githubusercontent.com/scunpacked/data/master/"
files_to_fetch = [
    "items.json",
    "ships.json",
    "components.json",
    "locations.json",
    "manufacturers.json",
    "modules.json"
]

# Download each file
for file_name in files_to_fetch:
    url = base_url + file_name
    try:
        print(f"🔄 Downloading {file_name} from {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        with open(output_dir / file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Saved: {file_name}")
    except Exception as e:
        print(f"❌ Failed to fetch {file_name}: {e}")
