numbers = [1, 2, 3, 4]
print("Початковий список", numbers)

numbers.remove(3)
print("Список після видалення числа", numbers)

num = 6
if num in numbers:
    numbers.remove(num)
    print("Список після видалення числa", numbers)
