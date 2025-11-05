# Simple calculator using match-case statement

a=int(input("Enter first number: "))            # Get first number from user using the input function
b=int(input("Enter second number: "))           # Get second number from user using the input function

sym= input("What operation do you want to perform (+, -, *, /): ")       # Get the operation symbol from user  

match sym:                                  # Use match-case to handle different operations {*work same as if-elif-else*}
    case "+":
        print(f"The sum is: {a + b}")
    case "-":
        print(f"The difference is: {a - b}")
    case "*":
        print(f"The product is: {a * b}")
    case "/":
        print(f"The quotient is: {a / b}")
    case _:
        print("Invalid operation.")


