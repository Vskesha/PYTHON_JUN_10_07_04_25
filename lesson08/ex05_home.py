import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-50, -50)
t.pendown()
t.color("brown")

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(-60, -50)
t.pendown()
t.color("black")

for _ in range(3):
    t.forward(120)
    t.left(120)

screen.mainloop()
