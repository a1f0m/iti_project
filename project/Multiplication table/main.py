import multiplication

# Ask the user to choose the method
print("Choose how to print the multiplication table:")
print("1 - Using nested loops")
print("2 - Using nested lists")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    multiplication.print_multiplication_table()
elif choice == "2":
    multiplication.list_multiplication_table()
else:
    print("❌ Invalid choice. Please select 1 or 2.")
