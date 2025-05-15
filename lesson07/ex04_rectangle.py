import turtle

t = turtle.Turtle()
t.speed(1)
t.shape("turtle")

for _ in range(4):
    t.forward(200)
    t.right(90)

turtle.done()
