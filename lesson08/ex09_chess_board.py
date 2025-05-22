import turtle

t = turtle.Turtle()
t.shape("square")
t.penup()

for y in range(8):
    for x in range(8):
        t.goto(x * 20, y * 20)
        if (x + y) % 2 == 0:
            t.color("black")
        else:
            t.color("white")
        t.stamp()

turtle.done()
