n=int(input("enter how many elements you want in a array: "))
l=[]
for i in range(0,n):
   el=int(input("enter an element into the array: "))
   l.append(el)
   print(l[i])
print("print the array")
for i in range (n):
   print(l[i],end=" ")
k=int(input("\n enter an element to be searche the from the above array: "))
ans=-1
for i in range(n):
   if(l[i]==k):
      ans=i
print("element found in the array at index ",ans )



