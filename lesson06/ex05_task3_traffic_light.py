# ------------------------------------------
# Завдання 3
# Написати програму, яка імітує рух автомобіля в залежності від 
# кольору світлофора. Програма повинна запитувати у користувача 
# "Введіть колір світлофора (червоний, жовтий, зелений): " 
# і рухати черепашку відповідно до цього кольору.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

traffic_light = screen.textinput(
    "Traffic Light", 
    "Введіть колір світлофора (червоний, жовтий, зелений): "
)
traffic_light = traffic_light.lower()

text_font = ("Arial", 16, "normal")

if traffic_light == "зелений":
    t.forward(100)
elif traffic_light == "жовтий":
    t.forward(50)
elif traffic_light == "червоний":
    t.write("Стій!", font=text_font, align="center")
else:
    t.pencolor("red")
    t.write("Неправильний ввід кольору!", font=text_font, align="center")

turtle.done()
