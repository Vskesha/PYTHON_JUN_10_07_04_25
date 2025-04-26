import turtle

wn = turtle.Screen()
t = turtle.Turtle()

user_text = wn.textinput("Введення", "Введіть текст, який потрібно вивести:")
t.write(user_text, font=("Courier", 18, "italic"))

wn.mainloop()
