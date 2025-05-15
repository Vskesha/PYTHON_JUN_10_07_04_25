import turtle

t = turtle.Turtle()
t.shape("turtle")

sides = 6
length = 150

for i in range(sides):
    t.forward(length)
    t.right(360 / sides)

t.penup()
t.goto(-250, 200)
t.pendown()

i = 0

while i < sides:
    t.forward(length)
    t.right(360 / sides)
    i += 1

turtle.done()
