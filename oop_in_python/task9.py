class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration
        
        self.current_count += 1
        
        if self.current_count == 1:
            return self.a
        
        self.a, self.b = self.b, self.a + self.b
        return self.a

print("Generating the first 5 Fibonacci numbers:")
fib_iterator_5 = FibonacciIterator(5)
for number in fib_iterator_5:
    print(number)

print("\nGenerating the first 7 Fibonacci numbers into a list:")
fib_list_7 = list(FibonacciIterator(7))
print(fib_list_7)
