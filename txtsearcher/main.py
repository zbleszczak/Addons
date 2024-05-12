import os

# declare the path to the folder
path = r"C:\Users\kompu\Downloads\Telegram Desktop\PRIVATE @zet_cloud #15"

# ask the user for the keyword to search for
keyword = input("Enter the keyword to search for: ")

# create a new file to store the results with the filename as the keyword entered
result_file_name = f"{keyword}_results.txt"
result_file_path = os.path.join(path, result_file_name)
result_file = open(result_file_path, "w", encoding="utf-8")

# initialize a counter for the number of times the keyword is found
count = 0

# loop through each file in the folder and search for the keyword
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt") and file.lower() == "passwords.txt":
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                try:
                    # read the contents of the file
                    contents = f.read()

                    # search for the keyword in the contents of the file
                    if keyword in contents:
                        # increment the counter and print the username and password
                        count += 1
                        index = contents.find(keyword)
                        username_start = contents.find("\n", index) + 1
                        username_end = contents.find("\n", username_start)
                        password_start = contents.find("\n", username_end) + 1
                        password_end = contents.find("\n", password_start)

                        username_str = contents[username_start:username_end]
                        if "Username:" in username_str:
                            username = username_str.split("Username:")[1].strip()
                        else:
                            username = username_str.strip()

                        password_str = contents[password_start:password_end]
                        if "Password:" in password_str:
                            password = password_str.split("Password:")[1].strip()
                        else:
                            password = password_str.strip()

                        result_file.write(f"{username}:{password}\n")
                except UnicodeDecodeError:
                    print(f"Error: Could not decode file '{file_path}' with 'utf-8' encoding. Skipping...")

print(count)
# close the result file
result_file.close()