while True:
    try:
        user_input = input("Enter a number between 1 and 10: ")
        number = int(user_input)
        
        if 1 <= number <= 10:
            print(f"Thank you! Your number is {number}.")
            break
        else:
            print("Invalid input. The number is not between 1 and 10. Try again.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number. Try again.")
