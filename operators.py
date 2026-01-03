a = 10
b = 3

x = True
y = False

lst = [1, 2, 3]
lst2 = lst
lst3 = [1, 2, 3]

print("1. ARITHMETIC OPERATORS")
print("Addition (+)        -->", a + b)
print("Subtraction (-)     -->", a - b)
print("Multiplication (*)  -->", a * b)
print("Division (/)        -->", a / b)
print("Floor Division (//) -->", a // b)
print("Modulus (%)         -->", a % b)
print("Exponent (**)       -->", a ** b)

print("\n2. LOGICAL OPERATORS")
print("AND (x and y)  -->", x and y)
print("OR  (x or y)   -->", x or y)
print("NOT x          -->", not x)
print("NOT y          -->", not y)

print("\n3. BITWISE OPERATORS")
print("AND (a & b) -->", a & b)
print("OR  (a | b) -->", a | b)
print("XOR (a ^ b) -->", a ^ b)
print("LEFT SHIFT (a << 1) -->", a << 1)
print("RIGHT SHIFT (a >> 1) -->", a >> 1)
print("COMPLEMENT -->", ~a)

print("\n4. COMPARISON OPERATORS")
print("Equal (a == b)        -->", a == b)
print("Not Equal (a != b)    -->", a != b)
print("Greater Than (a > b) -->", a > b)
print("Less Than (a < b)    -->", a < b)
print("Greater or Equal     -->", a >= b)
print("Less or Equal        -->", a <= b)

print("\n5. IDENTITY OPERATORS")
print("lst is lst2     -->", lst is lst2)
print("lst is lst3     -->", lst is lst3)
print("lst is not lst3 -->", lst is not lst3)

print("\n6. MEMBERSHIP OPERATORS")
print("2 in lst        -->", 2 in lst)
print("5 in lst        -->", 5 in lst)
print("5 not in lst    -->", 5 not in lst)
