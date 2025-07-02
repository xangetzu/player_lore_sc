import os
import requests
from dotenv import load_dotenv

# 1. Load your API key
load_dotenv()
token = os.getenv("UEX_API_KEY")
if not token:
    raise Exception("❌ UEX_API_KEY not found in .env.")

# 2. Headers for authentication
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

# 3. Correct UEX endpoint prefix
base_url = "https://uexcorp.space/2.0"

# 4. Define the list of resources to download
resources = {
    "items": "/items",
    "item_prices": "/items_prices",
    "pois": "/pois",
    "fuel_prices": "/fuel_prices"
}

# 5. Create output directory
output_dir = "external_data/uex"
os.makedirs(output_dir, exist_ok=True)

# 6. Fetch each resource
for name, path in resources.items():
    url = base_url + path
    print(f"🔄 Fetching {name} from {url}...")
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        with open(os.path.join(output_dir, f"{name}.json"), "w", encoding="utf-8") as f:
            f.write(resp.text)
        print(f"✅ {name}.json saved.")
    except requests.HTTPError as http_err:
        print(f"❌ HTTP error on {name}: {http_err.response.status_code} — {http_err.response.reason}")
    except Exception as err:
        print(f"❌ Failed to fetch {name}: {err}")