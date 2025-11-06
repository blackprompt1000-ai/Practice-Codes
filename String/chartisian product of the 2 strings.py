#take two strings and taek their chartisian product and print them out
s1=input("Enter first string: ")
s2=input("Enter second string: ")   
l=[]
e=()
for i in s1:
    for j in s2:
        e=(i,j)
        l.append(e)
print(l)