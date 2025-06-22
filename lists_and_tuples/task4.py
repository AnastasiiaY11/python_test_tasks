days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(f"First day: {days[0]}")

print(f"Last day: {days[-1]}")

middle_days = days[1:6]
print(f"Middle days: {middle_days}")

days[2] = 'Humpday'
print(f"Updated list: {days}")