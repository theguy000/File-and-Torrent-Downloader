import json
import re

try:
    with open('Downloader.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: Downloader.ipynb not found.")
    exit(1)

separator = '___JSON_SEPARATOR___'
content_with_separator = re.sub(r'(?<=})\\s*,\\s*(?={)|(?<=})\\s*(?={)', separator, content)
json_strings = content_with_separator.split(separator)

notebooks = []
for s in json_strings:
    try:
        notebooks.append(json.loads(s))
    except json.JSONDecodeError:
        pass

if not notebooks:
    print("Could not parse any notebook from the file.")
    exit(1)

final_notebook = notebooks[0]
all_cells = final_notebook.get('cells', [])

for notebook in notebooks[1:]:
    all_cells.extend(notebook.get('cells', []))

final_notebook['cells'] = all_cells

with open('Downloader.ipynb', 'w', encoding='utf-8') as f:
    json.dump(final_notebook, f, indent=2)

print("Notebook fixed successfully.")

import json
import re

try:
    with open('Downloader.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: Downloader.ipynb not found.")
    exit(1)

separator = '___JSON_SEPARATOR___'
content_with_separator = re.sub(r'(?<=})\\s*,\\s*(?={)|(?<=})\\s*(?={)', separator, content)
json_strings = content_with_separator.split(separator)

notebooks = []
for s in json_strings:
    try:
        notebooks.append(json.loads(s))
    except json.JSONDecodeError:
        pass

if not notebooks:
    print("Could not parse any notebook from the file.")
    exit(1)

final_notebook = notebooks[0]
all_cells = final_notebook.get('cells', [])

for notebook in notebooks[1:]:
    all_cells.extend(notebook.get('cells', []))

final_notebook['cells'] = all_cells

with open('Downloader.ipynb', 'w', encoding='utf-8') as f:
    json.dump(final_notebook, f, indent=2)

print("Notebook fixed successfully.")

