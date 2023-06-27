def main():
    height = get_size("height: ")
    width = get_size("width: ")
    area = get_size("area: ")
    build_column(height)
    build_row(width)
    build_grid(area)


# callbacks
def get_size(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")


def build_column(n):
    for i in range(n):
        print("#")


def build_row(n):
    print("?" * n)


def build_grid(n):
    for i in range(n):
        print("*" * n)


main()
