fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original list: {fruits}")

reversed_fruits = fruits[::-1]

print("\nReversed list with indices:")

for index, fruit in enumerate(reversed_fruits):
    print(f"Index {index}: {fruit}")
