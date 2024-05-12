import re

def count_keys_bought(file_path):
    total_keys = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Using regular expression to check for lines containing "(optional quantity) Klucz"
            match = re.search(r'(\d+\s)?Klucz', line)
            if match:
                # If there's a quantity, use it; otherwise, default to 1
                keys_bought = int(match.group(1)) if match.group(1) else 1
                total_keys += keys_bought

    return total_keys

# Provide the path to your input file
file_path = r'C:\Users\Admin\Desktop\Nowy Dokument tekstowy.txt'

# Call the function to get the total number of keys bought
total_keys_bought = count_keys_bought(file_path)

# Display the result
print(f'Total number of keys bought: {total_keys_bought}')
