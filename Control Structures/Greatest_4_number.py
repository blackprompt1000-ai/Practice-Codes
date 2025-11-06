a=int(input("enter any positive integer "))
b=int(input("enter any positive integer "))
c=int(input("enter any positive integer "))
d=int(input("enter any positive integer "))
if (a>b and a>c and a>d):
    print(a,"is the greatest")
elif (b>a and b>c and b>d):
    print(b,"is the greatest")
elif (c>a and c>b and c>d):
    print(c,"is the greatest")
else:
    print(d,"is the greatest")  