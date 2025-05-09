import user_authentication

# Ask for user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Validate input
is_user_valid = user_authentication.validate_user(username)
is_pass_valid = user_authentication.validate_pass(password)

# Check if both match (basic simulation, not secure logic)
if is_user_valid and is_pass_valid:
    print("✅ Login successful!")
else:
    print("❌ Invalid username or password.")
