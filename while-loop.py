x = float(input("Enter the starting value: "))
threshold = 1

iterations = 0

while x > threshold:
    x /= 2
    iterations += 1

print(f"Loop stopped after {iterations} iterations")
print(f"Final value (<= threshold): {x}")
