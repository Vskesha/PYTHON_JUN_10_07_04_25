# -----------------------------------
# Завдання 3. Напишіть функцію greet_user, 
# яка приймає два аргументи: name та greeting, 
# причому greeting має значення за замовчуванням "Hello". 
# Функція повинна виводити привітання у форматі 
# "[greeting], [name]!". Викличте цю функцію 3 рази 
# з різними значеннями та виведіть результати.


def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet_user("Alice")
greet_user("Bob", "Hi")
greet_user("Charlie", "Good morning")
