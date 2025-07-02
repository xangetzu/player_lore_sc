import os
import requests
import json

# Base URL for SC Trade Tools API
base_url = "https://sc-trade.tools/api"

# List of endpoints we want to retrieve and store
endpoints = [
    "locations",     # All planets, moons, outposts, etc.
    "commodities",   # All tradable goods like Laranite, Titanium, etc.
    "prices",        # Buy/sell prices at various locations
    "refineries",    # Refining facilities and yield information
    "shops",         # Shops and what they sell
    "shipyards"      # Locations selling ships
]

# Directory where the downloaded JSON files will be saved
output_dir = "external_data/sc_trade_tools"
os.makedirs(output_dir, exist_ok=True)  # Create the folder if it doesn't exist

# Loop through each endpoint and fetch data
for endpoint in endpoints:
    url = f"{base_url}/{endpoint}"  # Construct full URL for the request
    try:
        print(f"🔄 Fetching {endpoint} from {url}...")
        response = requests.get(url)           # Send the GET request
        response.raise_for_status()            # Raise error if request fails (e.g., 404, 500)

        # Parse the JSON response for formatting
        data = response.json()

        # Save the response content to a formatted (pretty) JSON file
        with open(os.path.join(output_dir, f"{endpoint}.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)  # Pretty-print with 2-space indentation

        print(f"✅ Successfully saved: {endpoint}.json")

    except requests.RequestException as e:
        # Catch and print any network/API errors
        print(f"❌ Failed to fetch {endpoint}: {e}")
    except json.JSONDecodeError as e:
        # Catch any JSON decoding issues
        print(f"❌ Failed to parse JSON for {endpoint}: {e}")
