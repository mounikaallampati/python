import collections



def main():
    values=[1,1.2,5,6,7]
    s=sum(values)
def sum(values):
    if not isinstance(values,collections.Iterable):
        raise TypeError("values must be iterable")
    total=0
    for v in values:
        if not isinstance(v,(int,float) ):
            raise ValueError("v must be numeric")
        else:
            total=total+v
    return total
main()