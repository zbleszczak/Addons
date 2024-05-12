filename = input(r"C:\Users\kompu\Desktop\txtsearcher\output.json")
try:
    # open the file for reading
    with open(filename, "r") as file:
        lines = file.readlines()

        # create a set of unique lines and a list of duplicates
        unique_lines = set()
        duplicates = []
        for line in lines:
            if line in unique_lines:
                # line is a duplicate, add it to the duplicates list
                duplicates.append(line)
            else:
                # line is unique, add it to the unique lines set
                unique_lines.add(line)

        # write the unique lines back to the file
        with open(filename, "w") as file:
            for line in unique_lines:
                file.write(line)

        # print the number of duplicates removed
        print(f"{len(duplicates)} duplicates were removed.")
except FileNotFoundError:
    print("File not found.")
