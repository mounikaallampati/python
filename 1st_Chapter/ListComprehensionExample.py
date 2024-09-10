def main():
    n=10
    squares=[k*k for k in range(1,n+1)]
    print(squares)
    factors=[k for k in range(1,n+1) if n%k==0]
    print(factors)
main()