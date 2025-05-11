# ------------------------------------------
# Завдання 6
# Створіть програму, яка запитує у користувача 
# "Введіть слово: " та змінює швидкість черепашки 
# в залежності від довжини слова: 
# швидше для коротших слів та повільніше для довших.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()

word = screen.textinput("Введення", "Введіть слово: ")

if len(word) < 5:
    t.speed(1)
elif len(word) < 10:
    t.speed(3)
else:
    t.speed(5)

t.forward(200)

turtle.done()
