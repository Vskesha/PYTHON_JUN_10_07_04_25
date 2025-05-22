import turtle

t = turtle.Turtle()
t.shape('turtle')

for angle in range(0, 360, 30):
    t.setheading(angle)
    t.stamp()
    t.forward(50)

turtle.done()
