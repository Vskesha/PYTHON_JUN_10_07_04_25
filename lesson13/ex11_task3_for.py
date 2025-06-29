# -----------------------------------
# Завдання 3.
# Вивести спеціальне повідомлення, "Знайдено [слово]"
# коли зустрічається слово "python" у будь-якому регістрі.

words = ["hello", "world", "python", "is", "awesome", "pyTHon"]

for word in words:
    if word.lower() == "python":
        print("Знайдено", word)
