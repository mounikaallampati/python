def main():
    n=int(input("enter  n value: "))
    fact=facts(n)
    print(fact)
def facts(n):
    f=[]
    for k in range(1,n+1):
        if n%k==0:
            f.append(k)

    return f
main()