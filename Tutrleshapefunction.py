from turtle import*
penup()
backward(650)
pendown()

def lea_shape(distance, number_of_sides, color):
    begin_fill()
    for i in range(number_of_sides):
        pencolor(color)
        fillcolor(color)
        forward(distance)
        right(360/number_of_sides)
    penup()
    end_fill()
    forward(120)
    pendown()
        
        
lea_shape(50, 3, 'red')
lea_shape(50, 4, 'blue')
lea_shape(50, 5, 'green')
lea_shape(50, 6, 'purple')
lea_shape(40, 7, 'orange')
lea_shape(40, 8, 'yellow')

penup()
forward(120)
pendown()

def draw_star(size, color):
    angle = 120
    begin_fill()
    fillcolor(color)
    for side in range(5):
        forward(size)
        right(angle)
        forward(size)
        right(72-angle)
    end_fill()

draw_star(50, 'black')
