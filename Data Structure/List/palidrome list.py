#fill the list from n to 1 and then [n,...1,...n]
n=int(input("enter the number till which u want "))
l1=[]
l2=[]
for i in range(n,0,-1):
    l1.append(i)
for i in range(2,n+1):
    l2.append(i)
print(l1+l2)