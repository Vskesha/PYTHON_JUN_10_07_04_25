# -----------------------------------
# Завдання 3. 
# Напишіть функцію update_temperature, яка оновлює значення 
# глобальної змінної temperature на основі переданого 
# аргументу new_temperature. Якщо нове значення перевищує 100, 
# встановіть temperature на 100. Якщо менше 0, встановіть 
# temperature на 0. В іншому випадку встановіть temperature 
# на нове значення. Викличте цю функцію з різними значеннями 
# та виведіть результати.

temperature = 20

def update_temperature(new_temperature):
    global temperature
    if new_temperature > 100:
        temperature = 100
    elif new_temperature < 0:
        temperature = 0
    else:
        temperature = new_temperature

print("Температура до оновлення:", temperature)
update_temperature(105)
print("Температура після оновлення:", temperature)
update_temperature(-50)
print("Температура після оновлення:", temperature)
update_temperature(50)
print("Температура після оновлення:", temperature)
