import os
import requests

# Base URL of the scunpacked-data repository
base_url = "https://raw.githubusercontent.com/StarCitizenWiki/scunpacked-data/master"

# List of JSON files to fetch
files_to_fetch = [
    "fps-items.json",
    "items.json",
    "labels.json",
    "manufacturers.json",
    "ship-items.json",
    "ships.json"
]

# Local target directory
target_directory = "external_data/scrunpacked"
os.makedirs(target_directory, exist_ok=True)

# Fetch and save each file
for filename in files_to_fetch:
    url = f"{base_url}/{filename}"
    response = requests.get(url)
    
    if response.status_code == 200:
        file_path = os.path.join(target_directory, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")
