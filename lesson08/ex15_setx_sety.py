import turtle
import random

t = turtle.Turtle()
t.speed(0)

t.goto(100, 200)
t.setx(200)
t.sety(100)

screen = t.getscreen()
width = screen.window_width()
height = screen.window_height()

colors = ["red", "green", "blue", "yellow"]

for _ in range(500):
    t.color(random.choice(colors))
    t.forward(random.randint(20, 50))
    t.right(random.randint(0, 360))
    t.penup()
    if t.xcor() > width / 2:
        t.setx(-width / 2)
    if t.xcor() < -width / 2:
        t.setx(width / 2)
    if t.ycor() > height / 2:
        t.sety(-height / 2)
    if t.ycor() < -height / 2:
        t.sety(height / 2)        
    t.pendown()

turtle.done()
