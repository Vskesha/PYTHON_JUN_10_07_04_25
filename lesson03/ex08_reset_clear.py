import turtle

wn = turtle.Screen()
wn.title("Базові команди для очистки і скидання налаштувань")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

t.forward(100)

t.up()
t.forward(50)

t.down()
t.forward(100)

# t.reset()
t.clear()

wn.mainloop()
