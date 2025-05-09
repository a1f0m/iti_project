def sort_list_elements():
    y = []
    x = int(input("Enter the number of elements: "))
    print("Enter the elements:")
    for i in range(x):
        num = int(input(f"Element {i+1}: "))
        y.append(num)
    ascending = sorted(y)
    descending = sorted(y, reverse=True)
    print("Ascending order:", ascending)
    print("Descending order:", descending)
