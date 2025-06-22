number = int(input("Enter a number: "))

if number < 10:
    message = "The number is less than 10."
elif number <= 20:
    message = "The number is between 10 and 20."
else:
    message = "The number is greater than 20."

print("Output:", message)