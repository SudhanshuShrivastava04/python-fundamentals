print("Enter Length & Breadth of Butterly!\n")

l = int(input("Height: "))
b = int(input("Breadth: "))

for i in range(1, l+1):
    for j in range(i):
        print("*", end="")

    for j in range(2*(b - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    
    print()

for i in range(l, 0, -1):
    for j in range(i):
        print("*", end="")

    for j in range(2*(b - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()