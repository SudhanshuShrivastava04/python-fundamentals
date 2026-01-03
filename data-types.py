class CustomObject:
    def __init__(self, value): #constructor
        self.value = value

    def __repr__(self): # string representation of object
        return f"{self.value}"


data = [10, 3.5, 2 + 5j, "DS", True, [1,2], (1,2), {"a":1, "b":2, "c":3}, {1,2}, None, bytearray(b"abc"), bytes(b"abc"), frozenset({1, 2}), CustomObject(10)]

mutable_types = (list, dict, set, bytearray, CustomObject)

for i in data: 
    is_mutable = isinstance(i, mutable_types)
    print(i, "->", type(i).__name__, "| Mutable: ", is_mutable)
