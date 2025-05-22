import turtle

t = turtle.Turtle()
t.speed(0)

screen = t.getscreen()
screen.tracer(0)

for i in range(36):
    t.circle(100)
    t.right(10)
    t.forward(10)

screen.update()

turtle.done()
