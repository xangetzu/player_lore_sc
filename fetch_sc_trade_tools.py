import os
import requests
import json

# Base URL for SC Trade Tools API
base_url = "https://sc-trade.tools/api"

# List of endpoints we want to retrieve and store
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

# Output directory to save the JSON files
output_dir = "external_data/sc_trade_tools"
os.makedirs(output_dir, exist_ok=True)

# Loop through each endpoint and fetch its data
for endpoint in endpoints:
    try:
        url = f"{base_url}/{endpoint}"
        print(f"🔄 Fetching {endpoint} from {url}...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP 4xx/5xx

        # Parse and pretty-print JSON
        data = response.json()
        output_path = os.path.join(output_dir, f"{endpoint.replace('/', '_')}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Successfully saved: {output_path}")

    except requests.RequestException as e:
        print(f"❌ Failed to fetch {endpoint}: {e}")
    except json.JSONDecodeError:
        print(f"❌ Failed to parse JSON for {endpoint}: Non-JSON response")
