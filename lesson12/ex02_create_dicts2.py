dog = {"name": "Pes", "age": 2, "place": "house"}
print(dog)

# Змішані типи ключів
mixed_dict1 = {
    42: "integer",
    (1, 2): "tuple",
    "key": "string"
}
print(mixed_dict1)

mixed_dict2 = {
    12: "1",
    12.0: "2",
    'key': "string",
    (12, ): "tuple",
}
print(mixed_dict2)