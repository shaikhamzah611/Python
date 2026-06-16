import turtle

screen = turtle.Screen
screen = turtle.bgcolor("brown")

pen = turtle.Turtle()
pen.pensize(3)

pen.color("sky blue")

for _ in range(4):
    pen.forward(100)
    pen.right(90)
    
