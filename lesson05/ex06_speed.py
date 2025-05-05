import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")

t.speed(1)
t.forward(100)

t.shape("circle")

t.speed(5)
t.right(90)
t.forward(100)

t.shape("triangle")

t.speed(10)
t.right(90)
t.forward(100)

turtle.done()
