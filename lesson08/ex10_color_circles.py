import turtle

t = turtle.Turtle()
t.shape("circle")

size = 2
t.shapesize(size)
t.penup()

colors = ["red", "blue", "green", "yellow", "purple"]

i = 0
for color in colors:
    t.color(color)
    t.goto(size * 20 * i, 0)
    t.stamp()
    i += 1

turtle.done()
