# -----------------------------
# Завдання 3.
# Створіть словник, який зберігає країни як ключі
# та їхні столиці як значення. Додайте три країни.
# Потім:
# 1. Виведіть столицю однієї з країн.
# 2. Додайте ще одну країну.
# 3. Видаліть одну країну зі словника.
# Приклад:
# "France" — "Paris", "Germany" — "Berlin", "Italy" — "Rome"

# Створюємо словник з країнами та столицями
countries = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome"
}

# Виводимо столицю Німеччини
print("Столиця Німеччини:", countries["Germany"])

# Додаємо ще одну країну
countries["Spain"] = "Madrid"

# Видаляємо одну країну (наприклад, Італію)
del countries["Italy"]

# Виводимо оновлений словник
print("Оновлений список країн:", countries)
