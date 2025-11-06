#find the frequency of the word in the string
text=(input("Enter the string: "))
word=(input("Enter the word: "))
words=text.split()  
count=0                 
for i in words:
    if i==word:
        count+=1        
print(f"The word '{word}' occurs {count} times in the given string.")       

'''s1="good book good book sleep read good book"
s2=s1.split()
print(s2)
d1={}
for i in s2:
    if i not in d1.keys():
        d1[i]=1
    d1[i]+=1
print(d1)'''