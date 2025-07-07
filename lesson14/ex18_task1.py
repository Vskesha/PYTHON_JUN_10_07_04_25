# -----------------------------------
# Завдання 1. Напишіть функцію calculate_statistics, 
# яка приймає список чисел і повертає їх середнє значення, 
# мінімальне та максимальне значення. Використовуйте цю 
# функцію з різними значеннями та виведіть результати.

def calculate_statistics(numbers):
    average = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return average, minimum, maximum


numbers = [4, 8, 15, 16, 23, 42]
average, min_val, max_val = calculate_statistics(numbers)

print("Середнє значення:", average)
print("Мінімальне значення:", min_val)
print("Максимальне значення:", max_val)
