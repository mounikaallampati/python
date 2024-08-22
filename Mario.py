def main():
    size=int(input("What size do you want? "))
    width=int(input("What width do you want? "))
    print_square(size)
    print_Row(width)
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
def print_Row(width):
    for i in range(width):
        print("#", end="")
main()