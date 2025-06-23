def create_user(username, email, password, **kwargs):
    # Validate username length
    if len(username) < 5:
        return "Error: Username must be at least 5 characters long"
    
    # Validate email format
    if '@' not in email:
        return "Error: Email must contain '@'"
    
    # Validate password length
    if len(password) < 8:
        return "Error: Password must be at least 8 characters long"
    
    # Create user dictionary with required fields
    user_data = {
        'username': username,
        'email': email,
        'password': password
    }
    
    # Add additional fields from kwargs
    user_data.update(kwargs)
    
    return user_data

# Test valid input
print("Test 1 - Valid input:")
result = create_user(
    username="john123",
    email="john@example.com",
    password="securePass123",
    age=30
)
print(result)

# Test invalid username
print("\nTest 2 - Invalid username:")
result = create_user(
    username="john",  # too short
    email="john@example.com",
    password="securePass123"
)
print(result)

# Test invalid email
print("\nTest 3 - Invalid email:")
result = create_user(
    username="john123",
    email="johnemailcom",  # missing @
    password="securePass123"
)
print(result)

# Test invalid password
print("\nTest 4 - Invalid password:")
result = create_user(
    username="john123",
    email="john@example.com",
    password="short"  # too short
)
print(result)
