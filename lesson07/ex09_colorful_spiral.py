import turtle
import colorsys

def draw_spiral():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    screen.bgcolor("black")
    n = 36

    for i in range(360):
        color = colorsys.hsv_to_rgb(i / n, 1.0, 1.0)
        t.pencolor(color)
        t.forward(i * 3 / n + i)
        t.right(59)

draw_spiral()
turtle.done()
