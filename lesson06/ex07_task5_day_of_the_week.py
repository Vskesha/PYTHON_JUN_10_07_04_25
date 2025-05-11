# ------------------------------------------
# Завдання 5
# Напишіть програму, яка питає у користувача "Введіть день тижня: " 
# та рухає черепашку відповідно до обраного дня. Наприклад, вперед на 
# понеділок, назад на вівторок, тощо.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)

days = ["понеділок", "вівторок", "середа", "четвер", "пятниця", "субота", "неділя"]
t.penup()
for day in days:
    t.forward(200)
    t.write(day, font=("Arial", 20, "normal"), align="center")
    t.backward(200)
    t.left(360 / 7)
t.pendown()

day = screen.textinput("Day input", "Введіть день тижня: ").lower().strip()

if day == "понеділок":
    t.forward(200)
elif day == "вівторок":
    t.left(1 * 360 / 7)
    t.forward(200)
elif day == "середа":
    t.left(2 * 360 / 7)
    t.forward(200)
elif day == "четвер":
    t.left(3 * 360 / 7)
    t.forward(200)
elif day == "пятниця":
    t.left(4 * 360 / 7)
    t.forward(200)
elif day == "субота":
    t.left(5 * 360 / 7)
    t.forward(200)
elif day == "неділя":
    t.left(6 * 360 / 7)
    t.forward(200)
else:
    t.color("red")
    t.write("Такого дня тижня не існує!", font=("Arial", 20, "normal"), align="center")

turtle.done()
