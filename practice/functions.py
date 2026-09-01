# Define a function using def keyword
def greet():
    print("Hello, welcome to Python!")

# Call the function
greet()

# Function with a positional/keyword parameter and a default parameter
def introduce(name, language="Python"):
    print(f"Hi, I am {name} and I code in {language}.")

introduce("Alice")                # Uses default: language="Python"
introduce("Bob", language="Java") # Overrides default using a keyword argument

# Return values
def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # Outputs: 12

# Arbitrary arguments *args and *kwargs
def total_items(*args):
    return sum(args)

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(total_items(1, 2, 3, 4))   # Outputs: 10
show_profile(username="dev_joe", role="admin")

# Lambda functions
# Syntax: lambda arguments: expression
multiply = lambda x, y: x * y
print(multiply(4, 5))  # Outputs: 20

# zip function good for looking at lists with corresponding indices
students = ["Devin", "Max", "Mary", "Amelia"]
grades = [100, 25, 90, 90]

# use zip to create pairs of student and grade
for student, grade in zip(students, grades):
    print(f"{student}: {grade}")

print(list(zip(students, grades)))