n=int(input("enter an array : "))
l=[]
for i in range(n):
    l.append(int(input("enter elements of an array: ")))
print(l)
  
start = 0;
end = len(l) - 1;

while(start < end):
    temp = l[end];
    l[end] = l[start];
    l[start] = temp;
    start += 1;
    end -= 1;


print("reversed array is : ",l)







