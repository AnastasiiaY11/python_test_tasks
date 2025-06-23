def get_positive_integer(prompt):
    """Helper function to get a positive integer from the user."""
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

def generate_number_triangle():
    """Generates a right-angled triangle of numbers using nested for loops."""
    print("\n--- Number Triangle ---")
    rows = get_positive_integer("Enter the number of rows: ")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  

def generate_multiplication_table():
    """Generates a multiplication table using nested for loops."""
    print("\n--- Multiplication Table ---")
    size = get_positive_integer("Enter the size of the table: ")
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()  

def generate_countdown():
    """Generates a countdown sequence using a while loop."""
    print("\n--- Countdown ---")
    start_num = get_positive_integer("Enter the countdown start number: ")
    while start_num > 0:
        print(start_num)
        start_num -= 1
    print("Blast off!")

def main():
    """Main function to run the pattern generator program."""
    while True:
        print("\n===== Number Pattern Generator Menu =====")
        print("1. Generate Number Triangle")
        print("2. Generate Multiplication Table")
        print("3. Generate Countdown")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            generate_number_triangle()
        elif choice == '2':
            generate_multiplication_table()
        elif choice == '3':
            generate_countdown()
        elif choice == '4':
            print("Thank you for using the pattern generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

main()
