'''#write a program to take footballer names and find length of their name 
n=int(input("Enter number of footballers: "))

for i in range(n):
    name=input("Enter footballer name: ")
    print(f"Length of {name} is {len(name)}")   '''



name = input("Enter footballer name seperated by comma: ")
name_split = name.split(",")  # Split the name into parts
l=[]
for i in name_split:
    l.append(len(i.strip()))  #strip is used to remove extra spaces if any
for j,names in enumerate(l):
    print(f"Length of the string {name_split[j].strip()} is {names}")