import turtle

t = turtle.Turtle()

# t.heading()
sides = 8
length = 50

for i in range(8):
    t.forward(length)
    t.stamp()
    t.write(
        t.heading(),
        font=("Arial", 15, "normal")
    )
    t.forward(length)
    t.left(360 / sides)

turtle.done()
