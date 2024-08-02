import turtle

def bres(x1,y1,x2,y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x_step = 1 if x1<x2 else -1
    y_step = 1 if y1<y2 else -1

    error = 2 * (dy-dx)

    line_points = []

    x , y = x1 , y1 

    for _ in range (dx+1):
        line_points.append((x,y))

        if error>0:
            y += y_step
            error -= 2 * dx
        
        x += x_step
        error += 2 * dy

    return line_points

turtle.setup(500,500)
turtle.speed(0)

x1 , y1 = 0 , 0
x2 , y2 = 200 , 150

lines = bres(x1,y1,x2,y2)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

for x,y in lines:
    turtle.goto(x,y)

turtle.exitonclick()

