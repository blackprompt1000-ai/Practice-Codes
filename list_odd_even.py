A = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("enter element of list"))
    A.append(ele)
E=[]
O=[]
for i in range(0,n):
    if(A[i]%2==0):
        E.append(A[i])
    else:
        O.append(A[i])

print("even list",E)
print("odd list",O)
        
