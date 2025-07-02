import os
import requests

# Base URL for the Cornerstone Item API
base_url = "https://cornerstone.tools/api/items"

# List of item categories available via Cornerstone's API
categories = [
    "armor",
    "attachments",
    "commodities",
    "consumables",
    "devices",
    "equipment",
    "gadgets",
    "grenades",
    "harvesting-tools",
    "medical",
    "mining-tools",
    "missiles",
    "munitions",
    "personal-weapons",
    "power-plants",
    "quantum-drives",
    "refining",
    "shields",
    "ship-weapons",
    "turrets",
    "utilities",
    "vehicles"
    ]

# Output directory where fetched data will be saved
output_dir = "external_data/cornerstone"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

# Loop through each category and fetch the corresponding data
for category in categories:
    try:
        url = f"{base_url}/{category}"  # Construct API endpoint
        response = requests.get(url)    # Make HTTP GET request
        response.raise_for_status()     # Raise exception for HTTP errors

        # Save the response content to a local JSON file
        with open(os.path.join(output_dir, f"{category}.json"), "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"✅ Successfully fetched: {category}")

    except requests.RequestException as e:
        print(f"❌ Error fetching {category}: {e}")