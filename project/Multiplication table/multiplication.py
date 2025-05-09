def print_multiplication_table():
    print("Multiplication Table using nested loops")
    print("===================================")
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{i}x{j}={i*j}", end="\t")
        print()

def list_multiplication_table():
    print("Multiplication Table using nested lists")
    print("===================================")
    n = int(input("Enter a number: "))
    arr = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        arr.append(row)
    print(arr)