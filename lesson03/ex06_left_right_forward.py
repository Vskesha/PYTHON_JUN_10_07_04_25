import turtle

window = turtle.Screen()
window.title("Базові команди для руху і поворотів")
window.bgcolor("lightblue")
window.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(90)
t.forward(100)
t.right(45)
t.forward(100)

window.mainloop()
