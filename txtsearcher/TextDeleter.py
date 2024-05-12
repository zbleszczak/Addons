import json

input_file_path = r'C:\Users\kompu\Desktop\projekty\txtsearcher\output.json'
output_file_path = file_path = r'C:\Users\kompu\Desktop\txtsearcher\input.json'

# Load the JSON data from the input file
with open(input_file_path, 'r', encoding='utf-8', errors='replace') as f:
    data = json.load(f)

# Remove the "ChampionList" and "SkinList" keys from each account
for account in data['Accounts']:
    if 'ChampionList' in account:
        del account['ChampionList']
    if 'SkinList' in account:
        del account['SkinList']

# Write the modified data to a new text file with indentation
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)