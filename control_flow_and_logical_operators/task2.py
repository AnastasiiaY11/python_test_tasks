password = input("Enter your password: ")

if len(password) < 8:
    print("Output: Password is invalid. Reason: Less than 8 characters")
elif 'Python' not in password:
    print("Output: Password is invalid. Reason: Does not contain Python")
elif ' ' in password:
    print("Output: Password is invalid. Reason: Password contains a space")
else:
    print("Output: Password is valid")