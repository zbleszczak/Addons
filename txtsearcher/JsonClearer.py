import json

# Open the JSON file and load its contents
with open(r'C:\Users\kompu\Desktop\projekty\txtsearcher\input.json', 'r', encoding='utf-8', errors='replace') as f:
    data = json.load(f)

# Dump the data in a formatted way
json_string = json.dumps(data, indent=4)

# Write the JSON string to a text file
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(json_string)