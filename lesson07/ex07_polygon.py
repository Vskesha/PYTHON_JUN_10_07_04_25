import turtle

screen = turtle.Screen()
t = turtle.Turtle()

sides = screen.textinput(
    "Polygon",
    "Введіть кількість сторін багатокутника: "
)

while not sides.isdigit():
    sides = screen.textinput(
        "Polygon", 
        f"Ви ввели '{sides}'. Це не число!\n"
        f"Введіть кількість сторін багатокутника знову: "
    )

length = screen.textinput(
    "Polygon", 
    "Введіть довжину сторони багатокутника: "
)

while True:
    if length is None:
        t.write("End", font=("Arial", 25, "normal"))
        screen.exitonclick()
    if length.isdigit():
        break
    else:
        length = screen.textinput(
            "Polygon",
            f"Ви ввели '{length}'. Це не число!\n"
            f"Введіть довжину сторони багатокутника знову: "
        )

sides = int(sides)
length = int(length)

for i in range(sides):
    t.forward(length)
    t.right(360 / sides)

turtle.done()
