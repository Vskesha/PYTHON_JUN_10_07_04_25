info = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}

keys = info.keys()
print(keys)

values = info.values()
print(values)

items = info.items()
print(items)

for key in info.keys():
    print(f"{key=}")

for value in info.values():
    print(f"{value=}")

for key, value in info.items():
    print(f"{key=}, {value=}")