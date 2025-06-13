# Завдання 3

# Створіть список імен учасників події.
# Використовуйте метод append() для додавання імен нових учасників.
# remove() для видалення імен учасників, які відмовилися від участі, 
# та sort() для організації списку учасників за алфавітом.

visitors = ["Ivan", "Oleg", "Andriy", "Yulia", "Sasha"]
new_visitors = ["Maryna", "Natalia", "Volodymyr"]

# Видалити двох учасників зі списку (одного за значенням, а іншого за індексом)
# Додати ще 3 нові імена зі списку new_visitors до списку visitors

visitors.pop(1)
visitors.remove("Sasha")

visitors.extend(new_visitors)
visitors.sort()

print(visitors)
