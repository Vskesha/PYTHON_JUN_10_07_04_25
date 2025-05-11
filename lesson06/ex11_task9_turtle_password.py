# ------------------------------------------
# Завдання 9
# Написати програму, яка запитує пароль і дозволяє 
# черепашці рухатися тільки якщо пароль правильний.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

password = screen.textinput("Password input", "Введи пароль для активації черепашки: ")
text_font = ("Times New Roman", 20, "bold")

if password == "secret":
    t.write("Пароль вірний! Черепашка активована.", align="center", font=text_font)
    t.forward(100)
else:
    t.write("Невірний пароль. Доступ заборонено.", align="center", font=text_font)

turtle.done()
