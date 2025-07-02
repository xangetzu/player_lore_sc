import json
from pathlib import Path

# Base directory of the script
base_dir = Path(__file__).resolve().parent.parent

# Input and output paths
input_dir = base_dir / 'external_data' / 'sc_trade_tools'
output_dir = base_dir / 'compiled_data'
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / 'master_sc_trade_tools.json'

# Container for compiled data
compiled_data = {}

# Walk through all JSON files in the input directory
for file_path in input_dir.glob('*.json'):
    try:
        with file_path.open('r', encoding='utf-8') as f:
            content = json.load(f)
            compiled_data[file_path.stem] = content
    except Exception as e:
        print(f"❌ Error reading {file_path.name}: {e}")

# Save compiled output
with output_file.open('w', encoding='utf-8') as f:
    json.dump(compiled_data, f, indent=4, ensure_ascii=False)

print(f"✅ SC Trade Tools data compiled successfully to: {output_file}")
