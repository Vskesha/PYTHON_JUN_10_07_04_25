# ------------------------------------------
# Завдання 8
# Створіть програму, яка вимагає від користувача 
# "Введи колір (червоний, зелений, синій): " 
# і змінює колір черепашки відповідно до введеного кольору.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

color = screen.textinput(
    "Distance input", 
    "Введи колір (червоний, зелений, синій): "
).lower()

if color == "червоний":
    t.color("red")
elif color == "зелений":
    t.color("green")
elif color == "синій":
    t.color("blue")
else:
    t.write(
        "Неправильний колір!", 
        align="center", 
        font=("Arial", 20, "bold")
)

t.forward(100)

turtle.done()
