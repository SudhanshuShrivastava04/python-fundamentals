a = float(input("a = "))
b = float(input("b = "))

o = input("operation = ")

if o == "+":
    c = a + b
elif o == "-":
    c = a - b
elif o == "*":
    c = a * b
elif o == "/":
    if b == 0:
        print("Error: Division by zero")
        exit()
    c = a / b
elif o == "%":
    c = a % b
elif o == "^":
    c = a ** b
else:
    print("Unknown Operation")
    exit()

print(c)
