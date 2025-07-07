# -----------------------------------
# Завдання 2. Напишіть функцію increment_global, 
# яка збільшує значення глобальної змінної counter на 1. 
# Викличте цю функцію кілька разів та виведіть 
# значення лічильника до і після викликів.

counter = 0

def increment_global():
    global counter
    counter += 1

print("Лічильник до викликів функції:", counter)
increment_global()
increment_global()
increment_global()
print("Лічильник після викликів функції:", counter)
