import turtle

wn = turtle.Screen()
wn.title("Проєкт коробка")
wn.bgcolor("lightgreen")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

width = 300
height = 200
depth = 150
angle = 60

t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)

t.left(angle)

t.penup()
t.goto(0, 0)
t.pendown()
t.forward(depth)

t.penup()
t.goto(0, -height)
t.pendown()
t.forward(depth)

t.penup()
t.goto(-width, -height)
t.pendown()
t.forward(depth)

t.penup()
t.goto(-width, 0)
t.pendown()
t.forward(depth)

t.right(angle)

t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)

wn.mainloop()
