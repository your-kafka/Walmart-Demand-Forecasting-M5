import json
from pathlib import Path

# Go through all .ipynb files in current folder and subfolders
for nb_file in Path('.').rglob("*.ipynb"):
    with open(nb_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Remove authors from metadata if present
    if 'metadata' in data:
        data['metadata'].pop('authors', None)
    
    # Save the cleaned notebook
    with open(nb_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)

print("All notebook authors removed!")
