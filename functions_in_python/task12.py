def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """Generator function that yields prime numbers infinitely"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Get first 10 prime numbers
print("First 10 prime numbers:")
primes = generate_primes()
for i, prime in enumerate(primes):
    if i >= 10:  # Stop after 10 prime numbers
        break
    print(prime)

# Additional demonstration: get next 5 prime numbers
print("\nNext 5 prime numbers:")
for i, prime in enumerate(primes):
    if i >= 5:  # Stop after 5 more prime numbers
        break
    print(prime)
