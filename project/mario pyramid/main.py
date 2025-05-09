import printing_pyramids
print("Welcome to the Pyramid Printing Program!")
height = int(input("Enter the height of the pyramid: "))

# Ask user to choose the method
print("Choose the method to print the pyramid:")
print("1 - Using nested loops")
print("2 - Using a list")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    printing_pyramids.print_pyramid(height)
elif choice == "2":
    lines = printing_pyramids.pyramid_list(height)
    for line in lines:
        print(line)
else:
    print("❌ Invalid choice. Please select 1 or 2.")
