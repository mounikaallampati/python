def main():

    n=100
    facts=factors(n)
    for fact in facts:
        print(fact,end=" ")

def factors(n):
    k=1
    while k*k<n:
        if n%k==0:
            yield k
            yield n//k
        k+=1
    if k*k==n:
        yield k
main()