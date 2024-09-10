from operator import truediv


def main():
    list=['a','c','a','g','s']
    target='a'
    count=Counter(list,target)
    print(count)
    status=contains(list,target)
    if status is True:
        print("item found")
    else:
        print("not found")
def Counter(list,target):
    count=0
    for i in list:
        if i==target:
            count=count+1
    return count
def contains(list,target):
    for i in list:
        if i==target:
            return True
    return False

main()