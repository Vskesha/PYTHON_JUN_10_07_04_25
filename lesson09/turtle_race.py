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
    

# Відслідковування натискання на кнопку
start_game(0, 0)

turtle.done()
