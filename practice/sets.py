# Python sets are an unordered collection of unique elements
# Unique elements (duplicate elements are removed)
# Unordered & Unindexed
# Hashable items only (immutable types string, numbers, tuples)

# Create a set
fruits = {"apple", "banana", "cherry"}

# Create a set from a list
numbers = set([1, 2, 2, 3, 4, 4]) # results in {1,2,3,4}

# Create an empty set
empty_set = set()

# Modify a set
colors = {"red", "green"}

# Add a single item
colors.add("blue")

# Add multiple items
colors.update(["yellow", "orange"])

# Remove an item if it exists
colors.remove("green")

# Safely remove an item
colors.discard("purple")

# Mathematical set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)          # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)          # Output: {3}

# Difference
print(set_a - set_b)          # Output: {1, 2}

# Symmetric Difference
print(set_a ^ set_b)          # Output: {1, 2, 4, 5}

# Membership Testing (Performance)
guests = {"Alice", "Bob", "Charlie"}

if "Alice" in guests:
    print("Alice is invited!")