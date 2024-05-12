import os
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def isValid(email):
    if re.fullmatch(regex, email):
        return True
    return False


path = r"C:\Users\Admin\Downloads\Telegram Desktop\dupa\steam_results.txt"
allFolders = os.listdir(path)

output = open(r"C:\Users\Admin\Downloads\Telegram Desktop\kox.txt", "w", encoding="utf-8")

for folder in allFolders:
    passwordsPath = path + "\\" + folder + "\\Passwords.txt"
    print(passwordsPath)
    if not os.path.exists(passwordsPath):
        continue
    with open(passwordsPath, "r", encoding="utf-8") as f:
        emails = []
        passwords = []
        for line in f.readlines():
            if line.startswith("Password:"):
                value = line.split(" ")[1]
                value = value.strip(" \n\t").split("\n")[0]
                if value in passwords:
                    continue
                passwords.append(value)
            elif line.startswith("Username:"):
                value = line.split(" ")[1]
                if not "@" in value:
                    continue
                value = value.strip(" \n\t").split("\n")[0]
                if value in emails:
                    continue
                emails.append(value)
        for email in emails:
            for password in passwords:
                output.write(email + ":" + password + "\n")

output.close()