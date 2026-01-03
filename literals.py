# Numeric Literals
print("Numeric Literals\n")

a = 0b1010 # binary
b = 100 # decimal
c = 0o310 # octal
d = 0x12c #hexadecimal

float_1 = 1.5 
flaot_2 = 1.5e2
flaot_3 = 1.5e-2

x = 5+4j

print(f"Decimal -> {a, b, c, d}")
print(f"Float -> {float_1, flaot_2, flaot_3}")
print(f"Complext -> {x, x.imag, x.real}")

# String Literals
print("String Literals\n")

string_1 = "Hello World"
string_2 = 'Hello World'
char = 'X'
multiline_str = """Hello World""" 
unicode = u"\U0001f600 \U0001f606 \U0001f923"
raw_str = "Hello\nWorld"

print(string_1, "->", type(string_1).__name__)
print(string_2,"->", type(string_2).__name__)
print(char, "->", type(char).__name__)
print(multiline_str, "->", type(multiline_str).__name__)
print(unicode, "->", type(unicode).__name__)
print(raw_str, "->", type(raw_str).__name__)

# Boolean Literals 
print("Boolean Literals\n")

x = True
y = False

print("LOGICAL OPERATIONS")
print("AND ->", x and y)
print("OR ->", x or y)
print("NOT x ->", not x)
print("NOT y ->", not y)
print("NAND ->", not (x and y))
print("NOR ->", not (x or y))
print("XOR ->", x ^ y)
print("XNOR ->", not (x ^ y))

print("\nBITWISE OPERATIONS")
print("AND ->", x & y)
print("OR  ->", x | y)
print("XOR ->", x ^ y)

# None 
print("\nNone or NA\n")

var = None 
print(var)






