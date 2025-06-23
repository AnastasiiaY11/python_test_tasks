def min_max_avg(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None, None
    
    # Find the minimum and maximum values
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the average value
    avg_value = sum(numbers) / len(numbers)
    
    return min_value, max_value, avg_value

# Examples of usage
numbers_list = [1, 4, 9, 2, 7, 5, 3]
min_val, max_val, avg_val = min_max_avg(numbers_list)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")

# Check the extreme case (empty list)
empty_list = []
min_val, max_val, avg_val = min_max_avg(empty_list)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")

# Check the list with one number
single_number = [5]
min_val, max_val, avg_val = min_max_avg(single_number)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")
