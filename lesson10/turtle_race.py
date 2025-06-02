import turtle
import random
import time

# Налаштування програми
fwidth = 800
fheight = 600
border = 20
max_move = 10
number_of_obstacles = 35
number_of_boosts = 30
delay = 0.1
boosts_color = "lightgreen"
colors = ["red", "blue", "green", "gray", "yellow", "orange", "purple", "brown"]
turtles = []
obstacles = []
boosts = []
# -----------------------------------------------------------
hwidth = fwidth // 2
hheight = fheight // 2
finish = hheight - border * 2
start = -finish

screen = turtle.Screen()
screen.title("Черепаші перегони")
screen.bgcolor("lightblue")
screen.setup(fwidth + border * 2, fheight + border * 2)

status_pen = turtle.Turtle()
status_pen.penup()
status_pen.hideturtle()
status_pen.goto(0, finish + border // 2)

# Функція для початку гри
def start_game(x, y):
    screen.onscreenclick(None)

    initialize_field()

    generate_obstacles()

    generate_boosts()

    num_players = get_number_of_players()

    generate_turtles(num_players)

    start_race()

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

def get_number_of_players():
    count = screen.numinput(
        "Кількість гравців",
        "Введіть кількість гравців (2 - 8): ",
        minval=2,
        maxval=8
    )
    return int(count)

def generate_turtles(num_players):
    turtles.clear()
    interval = fwidth // (num_players + 1)
    start_x = -hwidth + interval

    for i in range(num_players):
        bot = turtle.Turtle()
        bot.color(colors[i])
        bot.shape("turtle")
        bot.speed(5)
        bot.penup()
        bot.goto(start_x + i * interval, start)
        bot.setheading(90)
        bot.pendown()
        turtles.append(bot)

def start_race():
    turtle.tracer(0)
    game_in_progress = True
    while game_in_progress:
        for bot in turtles:
            
            for boost in boosts:
                if bot.distance(boost) < 20:
                    bot.setheading(90)
                    bot.pensize(5)
                    bot.forward(random.randint(40, 60))
                    bot.pensize(1)

            direction = 90
            for obs in obstacles:
                if bot.distance(obs) < 20:
                    if bot.xcor() < obs.xcor():
                        direction = 135
                    else:
                        direction = 45
                    break
            bot.setheading(direction)

            bot.forward(random.randint(1, max_move))

            if bot.ycor() >= finish:
                game_in_progress = False
                declare_winner(bot)
                break
        
        update_status()
        turtle.update()
        time.sleep(delay)
    
    status_pen.clear()
    turtle.update()

def declare_winner(winner):
    winner.penup()
    winner.goto(0, 0)
    winner.write(
        f"Переможець {winner.color()[0]}",
        font=("Arial", 25, "bold"),
        align="center"
    )
    # winner.hideturtle()
    winner.shapesize(3)
    winner.goto(0, -60)

def update_status():
    leading_turtle = turtles[0]
    for current_turtle in turtles:
        if current_turtle.ycor() > leading_turtle.ycor():
            leading_turtle = current_turtle
        
    leader_color = leading_turtle.color()[0]

    distance_to_finish = int(finish - leading_turtle.ycor())

    status_pen.clear()
    status_pen.write(
        f"Лідирує {leader_color:<10} Дистанція до фінішу: {distance_to_finish:>4}",
        align="center",
        font=("Arial", 16, "bold")
    )

def generate_obstacles():
    obstacles.clear()
    for _ in range(number_of_obstacles):
        x = random.randint(-hwidth + border, hwidth - border)
        y = random.randint(start + border, finish - border)
        obs = turtle.Turtle()
        obs.speed(0)
        obs.shape("circle")
        obs.color("black")
        obs.penup()
        obs.goto(x, y)
        obstacles.append(obs)

def generate_boosts():
    boosts.clear()
    for _ in range(number_of_boosts):
        x = random.randint(-hwidth + border, hwidth - border)
        y = random.randint(start + border, finish - border)
        boost = turtle.Turtle()
        boost.speed(0)
        boost.shape("triangle")
        boost.setheading(90)
        boost.color(boosts_color)
        boost.penup()
        boost.goto(x, y)
        boosts.append(boost)
        
# Відслідковування натискання на кнопку
draw_start_button()
screen.onscreenclick(start_game)

turtle.done()
