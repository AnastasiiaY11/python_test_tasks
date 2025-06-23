numbers = [3, 7, 1, 9, 4]
print(f"Original list: {numbers}")

for index, number in enumerate(numbers):
    multiplied_value = number * 3
    
    if multiplied_value > 15:
        numbers[index] = 'Too large'
    else:
        numbers[index] = multiplied_value

print(f"Modified list: {numbers}")
