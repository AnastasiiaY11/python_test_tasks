def multiply_decorator(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_result = func(*args, **kwargs)
            modified_result = original_result * factor
            return modified_result
        
        return wrapper

    return decorator

@multiply_decorator(factor=2)
def get_price():
    return 50

final_price = get_price()
print(final_price)

@multiply_decorator(factor=3)
def get_quantity():
    return 10

print("\n--- Multiplying quantity by 3 ---")
final_quantity = get_quantity()
print(final_quantity)
