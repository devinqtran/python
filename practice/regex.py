import re

# re.search(pattern, string) scans a string and returns a match object for the first occurrence
print(re.search(r'\d+', 'Item 42 and 99'))

# re.findall(pattern, string) returns all non-overlapping matches as a list of strings
print(re.findall(r'\d+', 'Item 42 and 99'))

# re.finditer(pattern, string) returns an iterator yielding match objects for all matches
# re.finditer(pattern, string)

# re.match checks for a match only at the beginning of a string
print(re.match(r'\d+', 'Item 42 and 99'))