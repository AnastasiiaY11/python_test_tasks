def add_five_decorator(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result + 5
    return wrapper

def double_decorator(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result * 2
    return wrapper

@add_five_decorator
@double_decorator
def get_value():
    return 10

final_result = get_value()
print(f"Final result of chained decorators: {final_result}")

@double_decorator
@add_five_decorator
def get_value_reversed():
    return 10

final_result_reversed = get_value_reversed()
print(f"Final result with reversed decorators: {final_result_reversed}")
