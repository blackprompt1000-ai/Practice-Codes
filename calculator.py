a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=input("enter the function that you want to apply between the variable")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
elif(c=="%"):
    print(a%b)
else:
    print("not a certified function")
