def main():
    number=get_Number()
    meow(number)
def get_Number():
    while True:
        n=int(input("Enter a number: "))
        if n>0:
            break
    return n
def meow(n):
    for i in range(n):
        print("mewo")

main()