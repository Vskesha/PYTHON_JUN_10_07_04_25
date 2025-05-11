age = int(input("Введи свій вік: "))

if age < 18:
    print("Ви неповнолітній")
elif age >= 65:
    print("Ви пенсіонер")
else:
    print("Ви дорослий")
