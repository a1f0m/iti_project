import username_valid

print("Choose what to validate:")
print("1 - Username")
print("2 - Email")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    name = input("Enter a username to validate: ")
    valid = username_valid.validate_name(name)
    if valid:
        print("✅ Username is valid.")
    else:
        print("Username is invalid. It must not be empty and must not contain numbers.")

elif choice == "2":
    print("Choose email validation method:")
    print("1 - Using if conditions")
    print("2 - Using try-except")

    email_choice = input("Enter your choice (1 or 2): ")
    email = input("Enter an email to validate: ")

    if email_choice == "1":
        if username_valid.email_validation(email):
            print("✅ Email is valid.")
        else:
            print("❌ Email is invalid.")
    elif email_choice == "2":
        username_valid.valid_email(email)
    else:
        print("❌ Invalid choice for email validation method.")

else:
    print("❌ Invalid main choice. Please enter 1 or 2.")
