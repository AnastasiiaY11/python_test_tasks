# Input data
numbers = [2, 4, 6, 8, 10]

# First double each number using map
doubled = map(lambda x: x * 2, numbers)

# Then filter numbers less than or equal to 10
result = list(filter(lambda x: x <= 10, doubled))

# Print results
print(f"Original numbers: {numbers}")
print(f"Numbers doubled and filtered (<=10): {result}")
