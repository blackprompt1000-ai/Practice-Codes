n=input("enter any string  ")
s=''
l=len(n)
for i in range(-1,(-l-1),-1):
    s=s+n[i]

if (n!=s):
    print("not a palindrome")
else:
    print("palindrome")
    

