def main():
    n=int(input("Enter a number: "))
    if isEven(n):
        print("Even")
    else:
        print("Odd")
def isEven(n):
    """if n%2==0:
        return True
    else:
        return False
        """
    return n%2==0
main()


