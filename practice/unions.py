# Define two sets with some overlapping values
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

# Combine them using the .union() method
result = set_a.union(set_b)

print(result)
# Output: {'banana', 'google', 'apple', 'microsoft', 'cherry'}
# Note: 'apple' only appears once, and sets are unordered.