# ------------------------------------------
# Завдання 7
# Написати програму, яка запитує у користувача 
# "Введи число: " та переміщує черепашку на відповідну 
# відстань вперед, якщо число додатнє, 
# або назад, якщо число від'ємне.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

number = int(screen.textinput("Distance input", "Введи число: "))

if number > 0:
    t.forward(number)
else:
    t.backward(-number)


turtle.done()
