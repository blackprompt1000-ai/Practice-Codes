#create a list of all even btw 1 and 20 and not diivisible by 4
n=[]

for i in range(1,20):
    if (i%2==0) and (i%4!=0):
        n.append(i)
print(n)