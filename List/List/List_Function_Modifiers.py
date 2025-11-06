a=[1,2,3,[67,88,"hello"],6,8]

print(a.index(6)) #print index number of the given elemental value

print("\n")

a.append(90)  #add the given value in the end of the list
print(a)

#   SLICING  {BY DEFAULT VALUE IS 0}
print("\n")
print(a[:3])    #print elements from index 0 to 2
print(a[3:])    #print elements from index 3 to end
print(a[:-2])   #print elements from start to index -3
print(a[-3:])   #print elements from index -3 to end 

# TRAVEL
print("\n")
for i in a:
    print(i)

#   CONCAT
print("\n")
b=[56,79]
print(a + [100, 200])  # Concatenate a new list to the end of a
print(a+b)
print(a) 
''' a is unchanged as if the concatenation was done and a new list is
         formed for that the original list remains the same'''

print("\n")

#   REPLICATING
c=[1,2,3]
print(c * 3)  # Replicate the list 3 times

print("\n")

#  NESTED INDEXING
print(a[3][2])        # Accessing "hello" from the nested list
print(a[3][2][1])     # Accessing "e" from the string "hello"
print(a[3][2][-1])    # Accessing "o" from the string "hello"
                      #  print(a[3,2,2]) error

print("\n")

# LENGTH
print(len(a))  # Get the length of the list
print(a)       # The list inside the list is counted a single element only
print("\n")

# COMPREHENSIONS
d=[2,4,6,8] 
e=[i/2 for i in d]  # create a new list with the half of each element in d
print(e)
f=[i*2 for i in d]  # create a new list with the double of each element in d
print(f)

print("\n")

# REMOVE & DELETE & CLEAR & REPLACE
a[1]=90              # replace the element at index 1 with 90
print(a)
a.remove(90)         # remove the given value from the list  {it removes the first occurrence}
print(a)  
'''since there were 2 values having 90, only the first one is removed'''

del a[2]             # delete the element at index 2
print(a)
a.clear()            # clear the entire list
print(a , "it is empty")
