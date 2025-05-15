import turtle
import random

t = turtle.Turtle()

for _ in range(25):
    t.forward(random.randint(20, 100))
    t.right(random.randint(0, 360))

turtle.done()
