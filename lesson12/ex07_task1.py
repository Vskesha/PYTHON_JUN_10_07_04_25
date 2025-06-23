# -----------------------------
#Завдання 1. 
# 
# Створіть словник, який зберігає інформацію про
# дві книги в бібліотеці. Ключем буде ISBN книги, 
# а значенням — словник з назвою книги, автором 
# та роком видання. Додайте третю книгу до 
# словника і виведіть інформацію про них.

# ISBN:   978-3-16-148410-0,    978-3-16-148410-1,    978-3-16-148410-2
# Title:  Python Basics,        Advanced Python,      Learning AI with Python
# Author: John Doe,             Jane Doe,             Alice Smith
# Year:   2021,                 2022,                 2023

library = {
    "978-3-16-148410-0": {
        "title": "Python Basics",
        "author": "John Doe",
        "year": 2021,
    },
    "978-3-16-148410-1": {
        "title": "Advanced Python",
        "author": "Jane Doe",
        "year": 2022,
    }
}

# Додати третю книгу до словника
library["978-3-16-148410-2"] = {
    "title": "Learning AI with Python",
    "author": "Alice Smith",
    "year": 2023,
}

for isbn, book_info in library.items():
    print(f"ISBN: {isbn}")
    for key, value in book_info.items():
        print(f"    {key}: {value}")
