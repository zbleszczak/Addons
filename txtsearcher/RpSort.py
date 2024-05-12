import json

# Open the input file for reading using utf-8 codec
with open('input.json', 'r', encoding='utf-8') as f:
    # Load the JSON data into a list of dictionaries
    accounts = json.load(f)['Accounts']

# Sort the list of dictionaries by the 'RpBalance' value in descending order
sorted_accounts = sorted(accounts, key=lambda account: account['RpBalance'], reverse=True)

# Open the output file for writing using utf-8 codec
with open('output.json', 'w', encoding='utf-8') as f:
    # Write the sorted data to the output file in JSON format
    json.dump({'Accounts': sorted_accounts}, f, indent=4, ensure_ascii=False)
