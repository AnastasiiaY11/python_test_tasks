def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"6! = {factorial(6)}")
print(f"7! = {factorial(7)}")
