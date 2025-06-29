numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 25

for number in numbers:
    if number == target:
        print(f"Знайдено число {target}!")
        break
else:
    print(f"Число {target} не знайдено!")
