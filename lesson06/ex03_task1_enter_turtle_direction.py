# ------------------------------------------
# Завдання 1
# Написати програму, яка запитує у користувача, 
# в якому напрямку повинна рухатися черепашка 
# "Введи напрямок руху (вліво, вправо, вперед, назад): "
# і рухає черепашку відповідно до цього вводу.

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

direction = screen.textinput(
    "Direction input", 
    "Введи напрямок руху (вліво, вправо, вперед, назад): "
)
direction = direction.lower().strip()

if direction == "вліво":
    t.left(90)
    t.forward(100)
elif direction == "вправо":
    t.right(90)
    t.forward(100)
elif direction == "вперед":
    t.forward(100)
elif direction == "назад":
    t.backward(100)
else:
    t.write(
        "Невірний напрямок руху!", 
        font=("TimesNewRoman", 20, "bold"), 
        align="center"
    )

turtle.done()
