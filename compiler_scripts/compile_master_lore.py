import json
import os
from pathlib import Path

# Define source folders
BASE_DIR = Path(__file__).resolve().parent
JSON_DIR = BASE_DIR / 'objects' / 'json'
OUTPUT_FILE = BASE_DIR / 'master_lore.json'

# Define categories and their folder mappings
CATEGORIES = {
    'characters': JSON_DIR / 'characters',
    'organizations': JSON_DIR / 'organizations',
    'vehicles': JSON_DIR / 'vehicles',
    'events': JSON_DIR / 'events'
}

# Container for merged content
master_data = {}

# Merge each category
for category, path in CATEGORIES.items():
    master_data[category] = []

    if not path.exists():
        print(f"⚠️ Warning: Folder not found for {category}: {path}")
        continue

    for file in path.glob('*.json'):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = json.load(f)
                master_data[category].append(content)
        except Exception as e:
            print(f"❌ Error loading {file.name}: {e}")

# Save to master file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=4, ensure_ascii=False)

print(f"✅ Master lore compiled successfully to: {OUTPUT_FILE}")
