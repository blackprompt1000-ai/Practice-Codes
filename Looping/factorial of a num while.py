#program to print the factorial of a number

n=int(input("Enter the number for which factorial required "))
p=1
i=1
while (i<=n):
    p *= i
    i+=1
    
print("factorial of ",n,"is ",p)