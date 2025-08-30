for i in range(1,1001):
    r=s=0
    num=i
    while(num>0):
        r=num%10
        s=s+r**3
        num=num//10
    if(i==s):
        print(i)
