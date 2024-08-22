def main():
    l1=[1,2,3,4]
    l2=[5,6,7,8]
    l3=union_Of_Two_Lists(l1,l2)
    print(l3)
def union_Of_Two_Lists(l1,l2):
    l3=[]
    for i in l1:
       l3.append(i)
    for i in l2:
        l3.append(i)
    return l3
main()













