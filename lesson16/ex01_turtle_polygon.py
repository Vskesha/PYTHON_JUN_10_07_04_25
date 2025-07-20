import turtle


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(1)

shapes = ["arrow", "turtle", "circle", "triangle", "square"]

for shape in shapes:
    t.shape(shape)
    t.forward(100)
    t.right(360/len(shapes))

turtle.done()
