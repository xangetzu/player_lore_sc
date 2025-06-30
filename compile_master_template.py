import os
import json

# Path to your templates directory
base_path = os.path.join("objects", "templates")
output_file = "master_template.json"

# Load all .json files from the templates directory
master_data = {}

for filename in os.listdir(base_path):
    if filename.endswith(".json"):
        file_path = os.path.join(base_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                key_name = filename.replace("_template.json", "").replace(".json", "")
                master_data[key_name] = data
            except json.JSONDecodeError as e:
                print(f"Error decoding {filename}: {e}")

# Write to master_template.json
with open(output_file, "w", encoding="utf-8") as out_file:
    json.dump(master_data, out_file, indent=2)

print(f"master_template.json created with {len(master_data)} sections.")