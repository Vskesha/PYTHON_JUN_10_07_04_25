import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.color("red", "green")
t.pensize(10)
t.begin_fill()
t.pendown()
t.forward(100)
t.penup()

t.goto(0, 100)
t.right(90)
t.pendown()
t.forward(100)
t.end_fill()

turtle.done()
