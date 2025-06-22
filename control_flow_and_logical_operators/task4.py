year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Output: {year} is a leap year.")
else:
    print(f"Output: {year} is not a leap year.")
