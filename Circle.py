import turtle
from  turtle import *

turtle.bgcolor("black")

i = 1

t = Turtle()

t.color("yellow")
t.shape("turtle")
t.speed(50)

while i<=10:
    for i in range(5):
        t.circle(100)
        t.right(-10)
    t.right(20)
