import turtle
import random

def random_walk():
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "green", "blue", "yellow"]
    
    for _ in range(200):
        t.color(random.choice(colors))
        t.forward(random.randint(20, 50))
        t.right(random.randint(0, 360))

random_walk()
turtle.done()
