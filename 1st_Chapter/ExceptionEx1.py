import  math
def main():
    x=int(input("enter a numeric number"))
    sq=sqrt(x)
    print(f"square root of {x} is",sq)

def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError("x must be numeric")
    elif x<0:
        raise ValueError("x can't be negative")

    else:
        sq=math.sqrt(x)
    return sq

main()