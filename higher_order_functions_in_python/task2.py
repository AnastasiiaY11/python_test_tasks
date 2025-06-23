def make_adder(add_value):
    def adder(number):
        return number + add_value
    return adder

print("Creating a function that adds 1...")
incrementer = make_adder(1)

result = incrementer(5)
print(f"Using the incrementer on 5: {result}") 

