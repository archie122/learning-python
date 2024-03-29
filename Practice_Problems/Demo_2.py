'''This is going to be a simple cookie clicker'''

import turtle

window = turtle.Screen()
window.title("Simple Cookies Clicker")
window.bgcolor("black")

COOKIE_IMG_PATH = "/Users/architchoudhary/Documents/GitHub/Python-Practice/Practice_Problems/images/cookie.gif"

window.register_shape(COOKIE_IMG_PATH)

cookie = turtle.Turtle()
cookie.shape(COOKIE_IMG_PATH)
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks : {clicks}", align="center", font=("Courier New", 32, "normal"))


def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks : {clicks}", align="center", font=("Courier New", 32, "normal"))


cookie.onclick(clicked)

window.mainloop()
