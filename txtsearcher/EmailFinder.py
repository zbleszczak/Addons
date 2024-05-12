import os

# get the current working directory
path = os.getcwd()

# create a new file to store the results with the filename as the keyword entered
result_file_name = "email_results.txt"
result_file_path = os.path.join(path, result_file_name)
result_file = open(result_file_path, "w", encoding="utf-8")

# initialize a counter for the number of times the keyword is found
count = 0

# loop through each file in the directory and its subdirectories and search for the keyword
for root, dirs, files in os.walk(path):
    for file in files:
        if file == "Passwords.txt":
            with open(os.path.join(root, file), "r", encoding="utf-8", errors="replace") as f:
                try:
                    # read the contents of the file
                    contents = f.read()

                    # search for the email address in the contents of the file
                    username_start = contents.find("Username:")
                    if username_start != -1:
                        username_end = contents.find("\n", username_start)
                        username_str = contents[username_start:username_end]
                        if "@wp" in username_str:
                            # increment the counter and write the email and password to the result file
                            count += 1
                            result_file.write(f"{username_str.split('Username:')[1].strip()}\n")
                except UnicodeDecodeError:
                    print(f"Error: Could not decode file '{file}' with 'utf-8' encoding. Skipping...")

# close the result file
result_file.close()

# print the number of times the email address was found
print(f"Email addresses were found in {count} files. Results saved in '{result_file_name}'.")
