def apply_function(func, value):
    return func(value)
triple = lambda x: x * 3
number = 4

result = apply_function(triple, number)
print(f"Applying 'lambda x: x * 3' to {number}:")
print(result)
