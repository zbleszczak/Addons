import os
import shutil
# Define the path where the .txt files are located
src_path = r"C:\Users\kompu\Downloads\Telegram Desktop\all"

# Define the path where you want to create the new directory
dst_path = r"C:\Users\kompu\Downloads\Telegram Desktop"

# Create a new directory named "passwords" in the specified path
if not os.path.exists(os.path.join(dst_path, "passwords")):
    os.makedirs(os.path.join(dst_path, "passwords"))

# Move all .txt files from source path to the "passwords" directory
counter = 1
for foldername, subfolders, filenames in os.walk(src_path):
    for filename in filenames:
        if filename.endswith('.txt'):
            file_path = os.path.join(foldername, filename)
            new_file_name = f"file{counter}.txt"
            counter += 1
            shutil.move(file_path, os.path.join(dst_path, "passwords", new_file_name))