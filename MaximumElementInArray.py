arr=[3,8,5,7,12,15,6,2]
for i in range(len(arr)):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
            
print("maximum element in array is",max)



