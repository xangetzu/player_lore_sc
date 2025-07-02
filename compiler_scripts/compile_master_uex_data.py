import os
import json

# Directory containing individual JSON files
input_dir = "external_data/uex"  # Change this per script
output_file = "compiled_data/uex_compiled.json"  # Change this per script

compiled_data = {}

# Iterate through every JSON file in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        path = os.path.join(input_dir, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                key = os.path.splitext(filename)[0]  # Use filename (without .json) as key
                compiled_data[key] = data
        except Exception as e:
            print(f"⚠️ Failed to load {filename}: {e}")

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the compiled data into one file, formatted for readability
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(compiled_data, f, indent=2)

print(f"✅ Compiled JSON saved to: {output_file}")
