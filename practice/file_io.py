# File operations r = read, w = write, a = append, rb/wb = binary, r+ = read/write

# Reading the entire file at once
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line-by-line (Most memory-efficient for large files)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes trailing newlines (\n)

# Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Overwriting or creating a file
with open("output.txt", "w") as file:
    file.write("This will overwrite existing content.\n")
    file.write("You must add your own newline characters.\n")

# Appending to an existing file
with open("output.txt", "a") as file:
    file.write("This line is appended to the bottom.\n")

# File exception handling
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The specified file could not be found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
