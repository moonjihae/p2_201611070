import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t=turtle.Turtle()
wn.bgcolor("pink")
global tposSave
width=t1.window_width()
w3=(width-30)/3
x1=-w3
x2=0
x3=+w3
height=t1.window_height()
h3=(height-40)/3
y1=-h3
y2=0
y3=+h3
def circleRed(pos):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.fillcolor("Red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
def circleBlue(pos):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
tposSave=list()
t.penup()
t.goto((x1,y3))
tposSave.append(t.pos())
t.goto((x1,y2))
tposSave.append(t.pos())
t.goto((x1,y1))
tposSave.append(t.pos())
t.goto((x2,y3))
tposSave.append(t.pos())
t.goto((x2,y1))
tposSave.append(t.pos())
t.goto((x3,y3))
tposSave.append(t.pos())
t.goto((x3,y2))
tposSave.append(t.pos())
t.goto((x3,y1))
tposSave.append(t.pos())
for i in range(0,len(tposSave)):
        print tposSave[i]
t.home()
t.clear()
def circlechangered():
    for i in range(0,len(tposSave)):
        circleRed(tposSave[i])
def circleChange():
    circle=input("Which circle write number(0~7) : ")
    t1.penup()
    t1.goto(tposSave[circle])
    circleBlue(tposSave[circle])
circlechangered()
circleChange()
wn.exitonclick()