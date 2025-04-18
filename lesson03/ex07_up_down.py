import turtle

wn = turtle.Screen()
wn.title("Базові команди для руху up and down")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")

t.forward(100)

t.up()
t.forward(50)

t.down()
t.forward(100)

wn.mainloop()
