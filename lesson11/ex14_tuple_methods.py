# Індекси в списку кортежів
list_of_tuples = [
    ("Arial", 18, "italic"),
    ("TimesNewRoman", 25, "bold"),
    ("Sans", 10, "normal")
]
print("Список кортежів:", list_of_tuples)

first_font = list_of_tuples[0]
print("Перший елемент списку кортежів:", first_font)

style_of_second_font = list_of_tuples[1][2]
print("Стиль другого елемента списку кортежів:", style_of_second_font)

# Методи index() та count() для кортежів
numbers = (1, 3, 1, 5, 5, 2, 3, 4, 5)

first_occurence_of_five = numbers.index(5)
print("Індекс першої п'ятірки:", first_occurence_of_five)

second_occurence_of_five = numbers.index(5, first_occurence_of_five + 1)
print("Індекс другої п'ятірки:", second_occurence_of_five)

amount_of_threes = numbers.count(3)
print("Кількість трійок у кортежі:", amount_of_threes)
