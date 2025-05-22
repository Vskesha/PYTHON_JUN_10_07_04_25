import turtle
import random

from settings import size, colors


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

for x in range(-5 * size, size * 5, size):
    t.color(random.choice(colors))
    for y in range(-5 * size, size * 5, size):
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(size - 3)
            t.right(90)

screen.mainloop()
