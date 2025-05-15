import turtle

t = turtle.Turtle()

t.color("red")
t.speed(10)

for _ in range(360):
    t.forward(2)
    t.right(1)

turtle.done()
