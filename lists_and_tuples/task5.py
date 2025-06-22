first_value_str = input("Enter first value: ")
second_value_str = input("Enter second value: ")

first_value = first_value_str
second_value = second_value_str
print(f"\nBefore Swap: First Value = {first_value}, Second Value = {second_value}")

(first_value, second_value) = (second_value, first_value)
print(f"After Swap: First Value = {first_value}, Second Value = {second_value}")
