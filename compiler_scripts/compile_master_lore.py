import json
from pathlib import Path

# Base directory of the script
base_dir = Path(__file__).resolve().parent.parent

# Input directories for each category
json_dir = base_dir / 'objects' / 'json'
categories = {
    'characters': json_dir / 'characters',
    'organizations': json_dir / 'organizations',
    'vehicles': json_dir / 'vehicles',
    'events': json_dir / 'events'
}

# Output path
output_dir = base_dir / 'compiled_data'
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / 'master_lore.json'

# Compile data
master_data = {}
for category, folder in categories.items():
    master_data[category] = []
    if not folder.exists():
        print(f"⚠️ Warning: Folder not found for {category}: {folder}")
        continue
    for file in folder.glob('*.json'):
        try:
            with file.open('r', encoding='utf-8') as f:
                content = json.load(f)
                master_data[category].append(content)
        except Exception as e:
            print(f"❌ Error loading {file.name}: {e}")

# Save compiled JSON
with output_file.open('w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=4, ensure_ascii=False)

print(f"✅ Master lore compiled successfully to: {output_file}")
