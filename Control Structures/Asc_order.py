a=int(input())
b=int(input())
c=int(input())
if(a>c and a>b):
    if(b>c):
        print(c,b,a)
    else:
        print(b,c,a)
elif(b>c):
    if(a>c):
        print(c,a,b)
    else:
        print(a,c,b)
elif(c>a):
    if(a>b):
        print(b,a,c)
    else:
        print(a,b,c)
else:
    print("all are equal")
        
