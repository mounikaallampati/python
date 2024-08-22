"""n=3
fact=1
while(n>0):
    fact=fact*n
    n-=1
print(fact)
"""
#fact funtion

def fact(n):
    if n < 0:
        return -1;
    elif n <= 1:
        return 1;
    else:
        return n * fact(n-1);

print(fact(3))