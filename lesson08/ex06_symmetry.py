import turtle


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

size = 50
positions = [-size * 2, 0, size * 2]

for y in positions:
    for x in positions:
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.right(90)

screen.mainloop()
