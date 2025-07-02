import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Resolve output directory relative to the script's location
base_dir = Path(__file__).resolve().parent.parent
output_dir = base_dir / "external_data" / "uex"
output_dir.mkdir(parents=True, exist_ok=True)

# Load API key from .env
load_dotenv()
token = os.getenv("UEX_API_KEY")
if not token:
    raise Exception("UEX_API_KEY not found in .env")

# Set up headers for authentication
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

# Define base API URL and list of resources to fetch
base_url = "https://api.uexcorp.space/2.0"
resources = [
    "categories", "categories_attributes", "cities", "commodities", "commodities_alerts",
    "commodities_averages", "commodities_prices", "commodities_prices_all",
    "commodities_prices_history", "commodities_ranking", "commodities_raw_averages",
    "commodities_raw_prices", "commodities_raw_prices_all", "commodities_routes",
    "commodities_status", "companies", "contacts", "contracts", "crew", "data_extract",
    "data_parameters", "factions", "fleet", "fuel_prices", "fuel_prices_all",
    "game_versions", "items", "items_attributes", "items_prices", "items_prices_all",
    "jump_points", "jurisdictions", "marketplace_favorites", "marketplace_listings",
    "marketplace_negotiations", "marketplace_negotiations_messages", "moons",
    "orbits", "orbits_distances", "organizations", "outposts", "planets", "poi",
    "refineries_audits", "refineries_capacities", "refineries_methods",
    "refineries_yields", "release_notes", "space_stations", "star_systems",
    "terminals", "terminals_distances", "user", "user_notifications",
    "user_refineries_jobs", "user_trades", "vehicles", "vehicles_loaners",
    "vehicles_prices", "vehicles_purchases_prices", "vehicles_purchases_prices_all",
    "vehicles_rentals_prices", "vehicles_rentals_prices_all", "wallet_balance"
]

# Fetch and save each resource
for resource in resources:
    url = f"{base_url}/{resource}"
    try:
        print(f"🔄 Fetching: {resource}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        output_file = output_dir / f"{resource}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Saved: {output_file.name}")
    except Exception as e:
        print(f"❌ Error fetching {resource}: {e}")
