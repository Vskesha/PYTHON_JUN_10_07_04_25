import turtle

wn = turtle.Screen()
wn.title("Прямокутник")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)

wn.mainloop()
