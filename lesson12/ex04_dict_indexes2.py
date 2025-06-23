# dictionary.get(key, default=None)
info = {"name": "Alice", "age": 25, "class": "7-A"}
print(info)
print("Ім'я:", info.get("name", "Невідомо"))
print("Адреса:", info.get("address", "Невідомо"))

# Видалення ключа
del info["age"]
print(info)

class_info = info.pop("class", "Клас не знайдено")
print("Клас:", class_info)
print(info)

# Додавання нового ключа
info["hair_color"] = "black"
print(info)

# Заміна значення за ключем
info["hair_color"] = "brown"
info["name"] = "Bob"
print(info)
