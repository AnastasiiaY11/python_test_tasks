def add(a, b):
    """Addition function"""
    return a + b

def subtract(a, b):
    """Subtraction function"""
    return a - b

def multiply(a, b):
    """Multiplication function"""
    return a * b

def divide(a, b):
    """Division function with error handling"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    """Power function"""
    return a ** b

def get_number(prompt):
    """Helper function to get valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_operation():
    """Helper function to get valid operation from user"""
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide),
        '5': ('Power', power)
    }
    
    while True:
        print("\nAvailable operations:")
        for key, (name, _) in operations.items():
            print(f"{key}: {name}")
        
        choice = input("Choose operation (1-5): ")
        if choice in operations:
            return operations[choice][1]
        print("Invalid choice! Please try again.")

def calculator():
    """Main calculator function"""
    print("Welcome to Function Calculator!")
    
    while True:
        # Get first number
        num1 = get_number("Enter first number: ")
        
        # Get operation
        operation = get_operation()
        
        # Get second number
        num2 = get_number("Enter second number: ")
        
        # Perform calculation
        result = operation(num1, num2)
        
        # Display result
        print(f"\nResult: {result}")
        
        # Ask if user wants to continue
        if input("\nDo you want to perform another calculation? (yes/no): ").lower() != 'yes':
            break
    
    print("Thank you for using Function Calculator!")

calculator()
