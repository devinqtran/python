import re

# \d matches any digit (0-9).
# \w matches any alphanumeric character or underscore.
# \s matches whitespace (spaces, tabs, newlines).
# . matches any character except a newline.
# + means 1 or more repetitions.* means 0 or more repetitions.
# ? means 0 or 1 repetition (or makes a quantifier non-greedy).
# ^ and $ anchor the match to the start or end of the string.

# re.search(pattern, string) scans a string and returns a match object for the first occurrence
print(re.search(r'\d+', 'Item 42 and 99'))

# re.findall(pattern, string) returns all non-overlapping matches as a list of strings
print(re.findall(r'\d+', 'Item 42 and 99'))

# re.finditer(pattern, string) returns an iterator yielding match objects for all matches
# re.finditer(pattern, string)

print("Check for a match at beginning of a string\n")
# re.match checks for a match only at the beginning of a string
print(re.match(r'\d+', 'Item 42 and 99'))

# re.sub(pattern, repl, string) replaces occurrences of the pattern with a replacement string
print(re.sub(r'\s+', '=', 'A B C'))

# re.split(pattern, string) splits the string by occurrences of the pattern
print(re.split(r',', 'a,b,c'))

# --- Using Regex to split a phone number ---
phone = '435-881-0990'

# Split the string by '-', then join the resulting list into an empty string
phone_str = "".join(re.split(r'-', phone))

print(phone_str) # Output: 4358810990