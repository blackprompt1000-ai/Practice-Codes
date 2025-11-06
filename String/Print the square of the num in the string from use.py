a=input("Enter a alphanumeric string: ")
for i in a:
    if i.isnumeric():
        print(int(i)*int(i))
        