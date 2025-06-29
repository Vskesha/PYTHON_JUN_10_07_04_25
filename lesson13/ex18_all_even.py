numbers = {2, 4, 6, 8, 10}

for number in numbers:
    if number % 2 != 0:
        print("Множина містить непарне число:", number)
        break
else:
    print("Всі числа в сеті парні.")
