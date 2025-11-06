#print(int("4+8")) it is an error 
print(eval("4+8"))  # what eval does is it examine the input and returns the result accordingly

n=eval(input("enter a number"))  # it will take input as a number not as a string or any other datatype as our input 

'''eval function is used to evaluate the expressions which are passed to it as a string and return the result accordingly.
it can also be used to take input of different datatypes like list, tuple, dictionary etc. without using type casting functions.'''