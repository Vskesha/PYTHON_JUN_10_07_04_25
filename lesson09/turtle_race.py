import turtle

# Налаштування програми


# -----------------------------------------------------------
screen  = turtle.Screen()
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


# Відслідковування натискання на кнопку
start_game(0, 0)

turtle.done()
