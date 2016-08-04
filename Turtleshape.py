import turtle
lea = turtle.Turtle ()
lea.pendown ()
for i in range(4):
    lea.forward (100)
    lea.right(90)
lea.penup()
lea.forward(200)
lea.pendown()
for i in range(3):
    lea.forward(100)
    lea.left(120)
lea.circle(100)
