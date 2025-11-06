#create a new list form the earlier existing list containg the sqrt of the old elements
import math
n=eval(input("Enter the lsit of which you want to print the sqrt "))
l2=[]
for i in range(len(n)):
    l2.append(math.sqrt(n[i]))

print(l2)