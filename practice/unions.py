# Method 1 using .union() method
# Define two sets with some overlapping values
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

# Combine them using the .union() method
result = set_a.union(set_b)

print(result)
# Output: {'banana', 'google', 'apple', 'microsoft', 'cherry'}
# Note: 'apple' only appears once, and sets are unordered.

# Method 2 using | operator
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Combine them using the pipe operator
result = set_a | set_b

print(result)
# Output: {1, 2, 3, 4, 5}

# Combining multiple sets
x = {"a", "b"}
y = {"b", "c"}
z = {"c", "d"}

# Chaining with .union()
union_method = x.union(y, z)

# Chaining with the | operator
union_operator = x | y | z

print(union_method)    # Output: {'a', 'b', 'c', 'd'}
print(union_operator)  # Output: {'a', 'b', 'c', 'd'}