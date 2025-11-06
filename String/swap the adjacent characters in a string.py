#swap the adjacent characters in a string
s=input("Enter a string: ")
for i in range(0,len(s)-1,2):
    s=s[:i]+s[i+1]+s[i]+s[i+2:]
print(s)