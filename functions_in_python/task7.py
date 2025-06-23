# Input list of names
names = ["Alice", "Bob", "Charlie"]

# Using map with lambda to create tuples of name and length
result = list(map(lambda name: (name, len(name)), names))

# Print the result
print(f"Input names: {names}")
print(f"Result: {result}")

# Additional test with different names
other_names = ["John", "Elizabeth", "Dan", "Katherine"]
other_result = list(map(lambda name: (name, len(name)), other_names))
print(f"\nAdditional test:")
print(f"Input names: {other_names}")
print(f"Result: {other_result}")
