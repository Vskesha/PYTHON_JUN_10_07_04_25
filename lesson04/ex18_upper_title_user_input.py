# Привіт, світ!
import turtle

window = turtle.Screen()
t = turtle.Turtle()

text = window.textinput("Input", "Введи текст:")

t.penup()
t.goto(-250, 50)
t.pendown()
t.write("Original: " + text, font=("Arial", 30, "normal"))

t.penup()
t.goto(-250, 0)
t.pendown()
t.write("Upper case: " + text.upper(), font=("Courier", 30, "italic"))

t.penup()
t.goto(-250, -50)
t.pendown()
t.write("Title case: " + text.title(), font=("TimesNewRoman", 30, "bold"))

window.mainloop()
