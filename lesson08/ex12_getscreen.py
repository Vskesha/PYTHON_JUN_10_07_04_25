import turtle
from time import sleep

t = turtle.Turtle()

sleep(5)

screen = t.getscreen()
screen.setup(width=600, height=400)
screen.title("Getscreen method")

turtle.done()
