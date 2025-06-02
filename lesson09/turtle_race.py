import turtle

# Налаштування програми

# -----------------------------------------------------------

screen = turtle.Screen()
screen.title("Черепаші перегони")
screen.bgcolor("lightblue")

# Функція для початку гри
def start_game(x, y):
    t = turtle.Turtle()
    t.write(
        "Гра розпочалася",
        font=("Arial", 30, "bold"),
        align="center"
    )

# Функція для малювання кнопки "Почати гру"
def draw_start_button():
    w = 200
    h = 50
    t = turtle.Turtle()
    t.speed(8)
    t.penup()
    t.goto(-w // 2, h)
    t.pendown()
    t.color("black", "green")
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

    t.color("white")
    t.forward(w // 2)
    t.write(
        "Start game",
        font=("Arial", h // 2, "bold"),
        align="center"
    )
    t.hideturtle()

# Відслідковування натискання на кнопку
draw_start_button()
screen.onscreenclick(start_game)

turtle.done()
