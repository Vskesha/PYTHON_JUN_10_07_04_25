from turtlegridutil import draw_grid
import turtle

wn = turtle.Screen()
draw_grid(wn, 
          major_line_color="grey", 
          minor_line_color="yellowgreen", 
          minor_line_step=20)
wn.title("Базові команди для руху і малювання")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.pensize(3)
t.shape("turtle")
t.speed(1)

t.goto(100, 200)

t.penup()
t.goto(200, 100)

t.pendown()
t.goto(100, -100)

t.backward(200)

wn.mainloop()
