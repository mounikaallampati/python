"""n=int(input("enter list size :"))
l1=[]
l2=[]
l3=[]
for i in range(n-1):
    l1.append(input("enter list elements : "))
for i in range(n-1):
    l2.append(input("enter list elements :"))
    """
def main():
    array1=[1,2,3,4]
    array2=[2,4,7,8]
    arr3 = Set_def(array1,array2)
    print(arr3)

def Set_def(array1,array2):
    array3 = []
    for i in range(len(array1)):
        found = False
        for j in range(len(array2)):
            if array1[i]==array2[j]:
                found = True
                break;
        if not found:
            array3.append(array1[i])


    return array3

main()