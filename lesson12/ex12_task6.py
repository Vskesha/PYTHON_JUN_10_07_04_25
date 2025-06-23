# -----------------------------
# Завдання 6.
# Створіть словник, що зберігає інформацію про користувачів.
# Ключем буде логін користувача (наприклад, "vasyl123"),
# а значенням — пароль. Реалізуйте логіку перевірки 
# логіну та паролю введених користувачем. 
# Також можна реалізувати логіку реєстрації користувача

from getpass import getpass

# словник з існуючими користувачами
users = {
    "vasyl123": "pass123",
    "anna456": "qwerty",
    "oleg789": "abc123"
}

while True:
    print()
    option = input("Виберіть опцію:" \
                "\n1 - вхід" \
                "\n2 - реєстрація" \
                "\n3 - видалити коритувача" \
                "\nВведи число: "
    )

    if option == "1":
        login = input("Введіть логін: ")
        password = getpass("Введіть пароль: ")

        if login in users and users[login] == password:
            print("✅ Успішний вхід!")
        else:
            print("❌ Невірний логін або пароль.")

    elif option == "2":
        login = input("Введіть логін: ")
        if login in users:
            print("Користувач з таким логіном уже існує")
            continue
        
        password1 = getpass("Введіть пароль: ")
        password2 = getpass("Введіть пароль повторно: ")
        if password1 == password2:
            users[login] = password1
            print("Користувача зареєстровано")
        else:
            print("Паролі не співпадають")

    elif option == "3":
        print("Видалення неможливо буде відновити")
        login = input("Введіть логін: ")
        password = getpass("Введіть пароль: ")
        if login in users and users[login] == password:
            print("👤 Користувача видалено")
        else:
            print("❌ Невірний логін або пароль.")
