print("🎯Guess the Number")

low = int(input("Enter lowerbound: "))
high = int(input("Enter upperbound: "))

print("\nThink of a number between", low, " and ", high)

counter = 0
while True:
    guess = (low + high) // 2 
    counter += 1
    print(f"\nIs {guess} is the correct guess?")

    response = input("Enter (h)igher, (l)ower or (c)orrect: ").lower()

    if response == "c":
        print(f"\nYay, {guess} is a correct guess and it took {counter} iterations")
        break 
    elif response == "h":
        low = guess + 1 
    elif response == "l":
        high = guess - 1 
    else:
        print("Invalid Input, Please Enter l, h or c")
