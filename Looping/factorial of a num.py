#program to print the factorial of a number

n=int(input("Enter the number for which factorial required "))
p=1
for i in range(1,n+1):
    p *=i

print("factorial of ",n,"is ",p)

