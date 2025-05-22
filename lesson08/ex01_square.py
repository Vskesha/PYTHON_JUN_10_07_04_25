import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.goto(-50, 0)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.right(90)

screen.mainloop()
