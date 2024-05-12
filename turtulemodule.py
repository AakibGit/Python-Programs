import turtle

turtle.bgcolor("black")

t = turtle.Turtle()
t.color("white")

t.speed(0)

while True:
    for i in range(10):
        t.forward(100)
        t.left(50)
    t.right(-50)
