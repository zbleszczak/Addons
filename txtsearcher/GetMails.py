import os

# declare the path to the folder
path = r"C:\Users\kompu\Downloads\Passwords2"

# create a new file to store the results with the filename as the keyword entered
result_file_name = "email_results.txt"
result_file_path = os.path.join(path, result_file_name)
result_file = open(result_file_path, "w", encoding="utf-8")

# initialize a counter for the number of times the keyword is found
count = 0

# loop through each file in the folder and search for the keyword
for entry in os.scandir(path):
    if entry.is_file() and entry.name.endswith(".txt"):
        with open(entry.path, "r", encoding="utf-8", errors="replace") as f:
            try:
                # read the contents of the file
                contents = f.read()

                # search for the email address in the contents of the file
                username_start = contents.find("Username:")
                if username_start != -1:
                    username_end = contents.find("\n", username_start)
                    username_str = contents[username_start:username_end]
                    if "@" in username_str:
                        # increment the counter and print the email and password
                        count += 1

                        password_start = contents.find("Password:", username_end)
                        password_end = contents.find("\n", password_start)
                        password_str = contents[password_start:password_end].strip()

                        password = password_str.split("Password:")[1].strip()

                        result_file.write(f"{username_str.split('Username:')[1].strip()}:{password}\n")
            except UnicodeDecodeError:
                print(f"Error: Could not decode file '{entry.name}' with 'utf-8' encoding. Skipping...")

# close the result file
result_file.close()

# print the number of times the email address was found
print(f"Email addresses were found in {count} files. Results saved in '{result_file_name}'.")
