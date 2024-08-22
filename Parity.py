def parity(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
def main():
    n = int(input("Enter a number: "))
    parity(n)
main()
