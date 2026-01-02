data = [10, 3.5, "DS", True, [1,2], (1,2), {"a":1}, {1,2}, None, bytearray(b"abc"), bytes(b"abc"), frozenset({1, 2})]

mutable_types = (list, dict, set, bytearray)

for i in data: 
    is_mutable = isinstance(i, mutable_types)
    print(i, "->", type(i).__name__, "| Mutable: ", is_mutable)
