import os
import shutil

# Set the path to search for Passwords.txt files
path = r'C:\Users\kompu\Downloads\Telegram Desktop'

# Create a new folder named "Passwords"
new_folder_name = os.path.join(path, 'Passwords')
if not os.path.exists(new_folder_name):
    os.mkdir(new_folder_name)

# Walk through each folder in the path
for foldername, subfolders, filenames in os.walk(path):
    # Check if the folder contains a Passwords.txt file
    if 'Passwords.txt' in filenames:
        # Get the path of the Passwords.txt file
        passwords_file_path = os.path.join(foldername, 'Passwords.txt')
        # Create a new file with a numbered suffix inside the "Passwords" folder
        i = 1
        while True:
            new_passwords_file_name = f"Passwords{i}.txt"
            new_passwords_file_path = os.path.join(new_folder_name, new_passwords_file_name)
            if not os.path.exists(new_passwords_file_path):
                shutil.copy(passwords_file_path, new_passwords_file_path)
                break
            i += 1