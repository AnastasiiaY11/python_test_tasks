from functools import reduce

# Input data
numbers = [1, 2, 3, 4]

# Calculate cumulative sum using reduce and lambda
cumulative_sum = reduce(lambda acc, x: acc + [acc[-1] + x] if acc else [x], numbers, [])

# Print results
print(f"Original numbers: {numbers}")
print(f"Cumulative sum: {cumulative_sum}")