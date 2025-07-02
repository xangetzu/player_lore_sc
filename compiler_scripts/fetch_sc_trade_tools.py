import requests
import json
from pathlib import Path

# Dynamically resolve the output directory based on the script's location
base_dir = Path(__file__).resolve().parent.parent
output_dir = base_dir / "external_data" / "sc_trade_tools"
output_dir.mkdir(parents=True, exist_ok=True)

# Base URL for the SC Trade Tools API
base_url = "https://sc-trade.tools/api"

# List of API endpoints to pull JSON from
endpoints = [
    "locations",
    "shops",
    "ships",
    "securityLevels",
    "locationTypes",
    "items",
    "itemTypes",
    "factions",
    "system/supporters",
    "crowdsource/locationBounties",
    "crowdsource/leaderboards/current",
    "crowdsource/leaderboards/overall",
    "crowdsource/leaderboards/previous",
    "crowdsource/commodity-listings"
]

# Iterate over each endpoint and fetch/save JSON response
for endpoint in endpoints:
    try:
        url = f"{base_url}/{endpoint}"
        print(f"🔄 Fetching {endpoint} from {url}...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise on HTTP errors (4xx, 5xx)

        data = response.json()
        safe_name = endpoint.replace('/', '_')  # Flatten nested endpoint names
        output_path = output_dir / f"{safe_name}.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Successfully saved: {output_path.name}")

    except requests.RequestException as e:
        print(f"❌ Failed to fetch {endpoint}: {e}")
    except json.JSONDecodeError:
        print(f"❌ Failed to parse JSON for {endpoint}: Non-JSON response")
