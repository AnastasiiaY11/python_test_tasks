numbers = [10, 20, 30, 40, 50, 11, 17, 22]

even_sum = 0
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number
        even_count += 1

print(f"Sum of even numbers: {even_sum}")
print(f"Number of even numbers: {even_count}")
