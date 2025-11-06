for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()

print("\n")

for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()

print("\n")

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

print("\n")

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print("\n")

for i in range(5,0,-1):
    for j in range(i-1,5):
        print(i, end=" ")
    print()

print("\n")

for i in range(6,1,-1):
    for j in range(i-1,6):
        print(j, end=" ")
    print()

print("\n")

A=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(A), end=" ")
        A+=1
    print()

print("\n")

B=65
for i in range(1,6):
    for j in range(1,6):
        print(chr(B), end=" ")
        B+=1
    print()