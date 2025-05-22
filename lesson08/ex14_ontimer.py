import turtle

t = turtle.Turtle()
t.speed(1)

def write_text():
    t.write(
        "This command is first.   ",
        font=("Arial", 20, "normal"),
        align="right"
    )

def draw_square():
    for _ in range(4):
        t.forward(200)
        t.right(90)

turtle.ontimer(write_text, 5000)
turtle.ontimer(draw_square, 2000)
t.write(
    "End of the program", 
    font=("Arial", 20, "normal")
)

turtle.done()
