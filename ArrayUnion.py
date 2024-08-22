"""a={1,2,2,3,5}
b={3,4,5,6}
#uninon
c=a|b
print(c)
#intersection
d=a&b
print(d)
#dierence
e=a-d
print(e)
"""
a=[1,2,3,4,5]
start=0
end=len(a)-1
while start<end:
    temp=a[end]
    a[end]=a[start]
    a[start]=temp
    start+=1
    end-=1
print(a)







