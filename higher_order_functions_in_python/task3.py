def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = str(original_result).upper()
        return modified_result
    
    return wrapper

@uppercase_decorator
def greet():
    return "Hello"

print(greet())

def say_goodbye():
    return "Goodbye"

decorated_goodbye = uppercase_decorator(say_goodbye)
print(decorated_goodbye())
