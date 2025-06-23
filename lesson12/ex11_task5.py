# -----------------------------
# Завдання 5.
# Створіть словник, що зберігає інформацію про користувачів.
# Ключем буде логін користувача (наприклад, "vasyl123"),
# а значенням — словник з ім’ям, прізвищем та email.
# Додайте двох користувачів.
# Оновіть email одного з них.
# Додайте третього користувача.
# Виведіть усі логіни користувачів.

# Створюємо словник користувачів
users = {
    "vasyl123": {
        "first_name": "Vasyl",
        "last_name": "Boliukh",
        "email": "vasyl@example.com"
    },
    "anna456": {
        "first_name": "Anna",
        "last_name": "Shevchenko",
        "email": "anna@oldmail.com"
    }
}

# Оновлюємо email одного з користувачів
users["anna456"]["email"] = "anna@newmail.com"

# Додаємо третього користувача
users["oleg789"] = {
    "first_name": "Oleg",
    "last_name": "Ivanov",
    "email": "oleg@example.com"
}

# Виводимо список логінів
print("Список логінів:", list(users.keys()))
