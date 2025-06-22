import random

# Create lists of characters
lower_case = list('abcdefghijklmnopqrstuvwxyz')
upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')

# Combine the lists
all_chars = lower_case + upper_case + digits

# Generate a password
password_list = []
for _ in range(8):
    password_list.append(random.choice(all_chars))

password = "".join(password_list)
print(f"Generated password: {password}")