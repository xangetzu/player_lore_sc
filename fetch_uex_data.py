import os
import json
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
token = os.getenv("UEX_API_KEY")
if not token:
    raise Exception("UEX_API_KEY not found in .env")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}
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

output_dir = "external_data/uex"
os.makedirs(output_dir, exist_ok=True)

for resource in resources:
    url = f"{base_url}/{resource}"
    try:
        print(f"📡 Fetching {resource}")
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        
        # Parse and re-dump the JSON with indentation
        parsed_json = resp.json()
        with open(os.path.join(output_dir, f"{resource}.json"), "w", encoding="utf-8") as f:
            json.dump(parsed_json, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved: {resource}.json (formatted)")
    except requests.HTTPError as e:
        print(f"⚠️ Skipped {resource}: {e.response.status_code} {e.response.reason}")
    except Exception as e:
        print(f"❌ Error for {resource}: {e}")