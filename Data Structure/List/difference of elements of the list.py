#difference btw the successive elements of the list
n=eval(input("enter the list "))
n.sort()
l2=[]
print("the sorted list :",n)
for i in range(len(n)-1):
    l2.append(n[i+1]-n[i])

print("the obtained list is ", l2)