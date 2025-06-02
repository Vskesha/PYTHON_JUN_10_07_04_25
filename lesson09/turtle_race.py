import turtle

# Налаштування програми
fwidth = 800
fheight = 600
border = 20
# -----------------------------------------------------------
hwidth = fwidth // 2
hheight = fheight // 2
finish = hheight - border * 2
start = -finish

screen = turtle.Screen()
screen.title("Черепаші перегони")
screen.bgcolor("lightblue")
screen.setup(fwidth + border * 2, fheight + border * 2)

# Функція для початку гри
def start_game(x, y):
    screen.onscreenclick(None)

    initialize_field()

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

def initialize_field():
    screen.clear()
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-hwidth, -hheight)
    t.pendown()

    t.pensize(3)
    for _ in range(2):
        t.forward(fwidth)
        t.left(90)
        t.forward(fheight)
        t.left(90)

    t.penup()
    t.goto(-hwidth, start)
    t.pendown()
    t.color("blue")
    t.write("Start", font=("Arial", 14, "bold"))
    t.forward(fwidth)

    t.penup()
    t.goto(-hwidth, finish)
    t.pendown()
    t.color("red")
    t.write("Finish", font=("Arial", 14, "bold"))
    t.forward(fwidth)
    t.hideturtle()

# Відслідковування натискання на кнопку
draw_start_button()
screen.onscreenclick(start_game)

turtle.done()
