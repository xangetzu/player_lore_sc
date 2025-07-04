import json
import requests
from pathlib import Path

# Dynamically resolve base directory and output path
base_dir = Path(__file__).resolve().parent.parent
output_dir = base_dir / "external_data" / "star_citizen_wiki"
output_dir.mkdir(parents=True, exist_ok=True)

# Base API URL for Star Citizen Wiki (v2)
base_url = "https://api.star-citizen.wiki/api/v2"

# Endpoints with their relative paths
endpoints = {
    "vehicles": "vehicles",                  # e.g., vehicles/300i
    "manufacturers": "manufacturers",        # e.g., manufacturers/RSI
    "comm_links": "comm-links",              # e.g., comm-links/12667
    "star_systems": "starsystems"            # e.g., starsystems/SOL
}

# Fetch and save each endpoint to a JSON file
for key, path in endpoints.items():
    url = f"{base_url}/{path}"
    try:
        print(f"🔄 Fetching {key} from {url}")
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        outfile = output_dir / f"{key}.json"
        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved: {outfile.name}")

    except requests.RequestException as e:
        print(f"❌ Failed to fetch {key}: {e}")
    except json.JSONDecodeError:
        print(f"❌ Failed to parse {key}: Invalid JSON response")