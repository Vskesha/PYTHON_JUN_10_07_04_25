import turtle

wn = turtle.Screen()
wn.title("Паралельні лінії")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

t.forward(200)

t.penup()
t.goto(0, -50)
t.pendown()
t.forward(200)

wn.mainloop()
