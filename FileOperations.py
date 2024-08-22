name=input("enter your name: ")
# writes name into the file but when ever we rerun the program it overrides old data with new Data
#file=open("names.txt","w")
# append adds new data  to old data
file=open("names.txt","a")
file.write(f"{name}\n")
file.close()
