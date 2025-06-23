def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

# Test the generator with a for loop
print("Testing generator with for loop (n=5):")
for square in generate_squares(5):
    print(square)

# Test the generator with sum() function
result = sum(generate_squares(4))
print(f"\nSum of squares from 1 to 4: {result}")  # Should output 30 (1 + 4 + 9 + 16)

# Additional demonstration: converting generator to list
squares_list = list(generate_squares(3))
print(f"\nList of squares from 1 to 3: {squares_list}")  # Should output [1, 4, 9]
