def main():
    l1=[1,2,3,4]
    l2=[5,3,9,2]
    l3=Intersection_Of_Two_Lists(l1,l2)
    print(l3)

def Intersection_Of_Two_Lists(l1,l2):
    l3=[]
    common=False
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i]==l2[j]:
                common=True
                l3.append(l1[i])

    return l3

main()

