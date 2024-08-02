import turtle

screen = turtle.Screen()
turtle.speed(6)
turtle.bgcolor('white')
turtle.pensize(2)

t = turtle.Turtle()

def rectangle(x,y,w,h,c):
    t.penup()
    t.goto(x,y)
    t.color(c)
    t.pendown()

    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def circle(x,y,r,c):
    t.penup()
    t.goto(x,y-r)
    t.pendown()
    t.color(c)
    t.circle(r)

def translate(x,y,tx,ty):
    t.penup()
    t.goto(x+tx,y+ty)
    t.pendown()

def rotate(x,y,a):
    t.penup()
    t.goto(x,y)
    t.setheading(a)
    t.pendown()

def scale(x,y,sx,sy):
    t.penup()
    t.goto(x*sx,y*sy)
    t.pendown()

rectangle(-200,0,100,50,"red")

translate(-200,0,200,0)
rectangle(0,0,100,50,"red")

rotate(0,0,60)
rectangle(0,0,100,50,"yellow")

scale(0,0,2,2)
rectangle(0,0,100,50,"blue")

circle(100,100,50,"green")

translate(100,100,200,0)
circle(300,100,50,"green")

rotate(300,100,60)
circle(300,100,50,"yellow")

scale(300,100,2,2)
circle(300,100,50,"blue")

turtle.done()