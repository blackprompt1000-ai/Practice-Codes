#to count all the number which are divisible by 3 in a given list
n=eval(input("Enter the elements in the list: "))

count=0
for i in n:
    if i%3==0:
        count+=1
print("The count of numbers divisible by 3 is:", count) 