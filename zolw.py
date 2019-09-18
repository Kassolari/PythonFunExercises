import turtle
import time
import random

window = turtle.Screen()    # creates a graphics window
pen = turtle.Turtle()      # create a turtle named alex

colors = ["green","red","blue","black"]

for i in range(4):
    pen.color(random.choice(colors))
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(180)

window.exitonclick()