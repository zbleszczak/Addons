import json
records = []
# read the JSON file
with open(r'C:\Users\kompu\Desktop\txtsearcher\resultall.json', encoding='utf-8') as f:
    for line in f:
        record = json.loads(line)
        records.append(record)

    # sort the data by highest RpBalance
    sorted_data = sorted(records, key=lambda x: x['RpBalance'], reverse=True)

    # replace unknown characters with a space
    for account in sorted_data:
        for key, value in account.items():
            if isinstance(value, str):
                account[key] = value.replace('?', ' ')

    # save the sorted data to a text file
    with open('sorted_data.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(sorted_data, indent=4))