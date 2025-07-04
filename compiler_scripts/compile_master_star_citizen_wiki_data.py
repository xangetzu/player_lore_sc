import json
from pathlib import Path

# Resolve dynamic paths
base_dir = Path(__file__).resolve().parent.parent
input_dir = base_dir / "external_data" / "star_citizen_wiki"
output_dir = base_dir / "compiled_data"
output_file = output_dir / "master_star_citizen_wiki.json"

# Create output directory if needed
output_dir.mkdir(parents=True, exist_ok=True)

# Define the expected categories and corresponding filenames
categories = {
    "vehicles": "vehicles.json",
    "manufacturers": "manufacturers.json",
    "comm_links": "comm_links.json",
    "star_systems": "star_systems.json"
}

# Master container
compiled_data = {}

# Load each file and group under its category
for category, filename in categories.items():
    file_path = input_dir / filename
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            compiled_data[category] = data
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")

# Write the compiled output
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(compiled_data, f, indent=2, ensure_ascii=False)

print(f"✅ Star Citizen Wiki data compiled successfully to: {output_file}")