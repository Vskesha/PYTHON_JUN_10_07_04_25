random_numbers = [42, 23, 8, 16, 4, 15]
print("Початковий несортований список:", random_numbers)

# Сортування списку в порядку зростання

print("Список в порядку зростання:", sorted(random_numbers))
print("Оригінальний список не змінений:", random_numbers)

random_numbers.sort()
print("Оригінальний список в порядку зростання:", random_numbers)
