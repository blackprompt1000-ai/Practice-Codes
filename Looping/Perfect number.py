n=int(input("eneter any numebr "))
s=0
i=1
while (i<n):
    if(n%i==0):
        s += i
    i+=1
if (s==n):
    print("perfect num ")
else:
    print("not a perfect num")