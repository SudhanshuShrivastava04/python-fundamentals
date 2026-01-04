x = float(input("Enter the starting value: "))
threshold = float(input("Enter Threashold: "))
decay = float(input("Enter Decay constant: "))

iterations = 0

while x > threshold:
    x /= decay
    iterations += 1

print(f"It took {iterations} iterations to reach below threshold")
print(f"Final value : {x}")
