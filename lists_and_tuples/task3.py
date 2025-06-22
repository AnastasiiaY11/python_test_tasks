numbers = [5, 12, 7, 9, 20, 15]
print(f"Original list: {numbers}")

numbers.append(25)
print(f"After adding 25: {numbers}")

numbers.remove(7)
print(f"After removing 7: {numbers}")

numbers.sort()
print(f"Sorted list: {numbers}")

largest_number = max(numbers)
smallest_number = min(numbers)
print(f"Largest number: {largest_number}")
print(f"Smallest number: {smallest_number}")