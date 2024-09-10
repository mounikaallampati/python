def main():
    n=int(input("enter n value"))
    factors=fact(n)
    for factor in factors:
        print(factor,end=" ")

def fact(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k

main()