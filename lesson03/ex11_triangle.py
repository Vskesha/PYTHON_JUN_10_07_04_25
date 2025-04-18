import turtle

wn = turtle.Screen()
wn.title("Трикутник")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

wn.mainloop()
