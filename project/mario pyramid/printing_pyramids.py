def print_pyramid(h):
    print("printing pyramid using nested loops")
    for i in range(1, h + 1):
        spaces = h - i
        print(" " * spaces + "*" * i)

def pyramid_list(h):
    print("printing pyramid using list")
    p = []
    for i in range(1, h + 1):
        stars = "*" * i
        spaces = " " * (h - i)
        r = spaces + stars
        p.append(r)
    return p