#print prime number btw 30 and 50

for i in range(30,50):
    c=0
    for j in range (2,i+1):
        if (i%j==0):
            c+=1
    if (c==1):
        print(i)
