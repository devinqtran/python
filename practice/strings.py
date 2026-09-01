# Creating Strings
# Single or double quotes (identical functionality)
single = 'Hello'
double = "World"

# Triple quotes for multi-line strings
multi_line = """This string spans
multiple lines easily."""

# Indexing/Slicing Python strings are zero-indexed (access using bracket notation [start:end:step])
text = "Python"
name = "Devin"

# Indexing
print(text[0])   # Output: 'P' (First character)
print(text[-1])  # Output: 'n' (Last character via negative indexing)

# Slicing (The 'end' index is exclusive)
print(text[0:2]) # Output: 'Py'
print(text[2:])  # Output: 'thon' (Omitting end goes to the finish)
print(text[::-1])# Output: 'nohtyP' (Reverses the string using step -1)

print(name[0])
print(name[0:5:2]) # prints every other char

# Core String Operations
# len() gets total character count
print(len("Code"))        # Output: 4

# Concatenation using + operator
print("Super" + "nova")   # Output: 'Supernova'

# Repetition using * operator
print("Hi!" * 3)          # Output: 'Hi!Hi!Hi!'

# Membership using 'in' or 'not in'
print("py" in "python")   # Output: True

# String formatting f-strings (formatted string literals)
name = "Alice"
age = 30

# Using f-strings
print(f"My name is {name} and I am {age} years old.") 

# Formatting float numbers inside an f-string
pi = 3.14159
print(f"Pi to two decimal places: {pi:.2f}")  # Output: 3.14

# Built-in string methods
# .upper() converts all characters to uppercase
print("Devin".upper())

# .lower() converts all characters to lowercase
print("DeViN".lower())

# .strip() removes leading and trailing whitespace
print(" devin ".strip())

# "delimiter".join(list) merges a list of strings into one string
print("-".join(["D", "E", "V", "I", "N"])) # returns D-E-V-I-N

# .split() splits a string into a list of substrings
print("D,E,V,I,N".split(",")) # returns ['D', 'E', 'V', 'I', 'N']

# .replace(old, new)
print("Devin".replace("D", "Z"))

# .find(substring) returns the lowest index of a match or -1
idx = "Devin".find("ev")
print(idx)

# .isdigit() returns True if all characters are numbers
allNumbers = False
allNumbers = "12345".isdigit()
print(allNumbers)

# STRING MANIPULATION C++ vs PYTHON
# input.substr(1) = self.input = self.input[1:]