n=int(input("enter any number"))
r=s=0
p=n
while(n>0):
    r=n%10
    s=s+r**3
    n=n//10
if(s==p):
    print("armstrong number")
else:
    print("not a armstrong number")
