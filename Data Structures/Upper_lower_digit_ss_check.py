ch = input("Please Enter Your Own Character : ")

if(ch >= 'A' and ch <= 'Z'):
    print("is an Uppercase Alphabet") 
elif(ch >= 'a' and ch <= 'z'):
    print("is a Lowercase Alphabet")
elif(ch>='0' and ch<='9'):
    print("digits")
else:
    print("special symbol")
