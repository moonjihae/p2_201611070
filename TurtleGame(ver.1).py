﻿import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t=turtle.Turtle()
t3=turtle.Turtle()
wn.bgcolor("pink")
t1.speed(7)
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
def circleRed(pos1,pos2):
    t1.speed(3)
    t1.penup()
    t1.goto(pos1,pos2)
    t1.pendown()
    t1.fillcolor("Red")
    t1.begin_fill()
    t1.circle(50)
    t1.end_fill()
def circleBlue(pos1,pos2):
    t1.speed(3)
    t1.penup()
    t1.goto(pos1,pos2)
    t1.pendown()
    t1.fillcolor("Blue")
    t1.begin_fill()
    t1.circle(50)
    t1.end_fill()
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
Afile=raw_input("input your file :tposSave.txt:")
frec=open(Afile)
tposSave=list()
for line in frec:
    line1=line.split(',')
    tposSave.append([(line1[0],line1[1]),(line1[2],line1[3]),(line1[4],line1[5]),(line1[6],line1[7]),(line1[8],line1[9]),(line1[10],line1[11]),(line1[12],line1[13]),(line1[14],line1[15].strip())])
    print tposSave
frec.close()

def drawRed(tposSave):
    for coord in tposSave:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        x3=int(coord[2][0])
        x4=int(coord[3][0])
        x5=int(coord[4][0])
        x6=int(coord[5][0])
        x7=int(coord[6][0])
        x8=int(coord[7][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        y3=int(coord[2][1])
        y4=int(coord[3][1])
        y5=int(coord[4][1])
        y6=int(coord[5][1])
        y7=int(coord[6][1])
        y8=int(coord[7][1])
        circleRed(x1,y1)
        circleRed(x2,y2)
        circleRed(x3,y3)
        circleRed(x4,y4)
        circleRed(x5,y5)
        circleRed(x6,y6)
        circleRed(x7,y7)
        circleRed(x8,y8)
drawRed(tposSave)
t1.penup()
t1.home()
t1.pendown()
file2=raw_input("input your file: circlepos.txt : ")
circle=open(file2)
circlepos=list()
for line in circle:
    line1=line.split(',')
    circlepos.append([(line1[0],line1[1]),(line1[2],line1[3]),(line1[4],line1[5]),(line1[6],line1[7]),(line1[8],line1[9]),(line1[10],line1[11]),(line1[12],line1[13]),(line1[14],line1[15].strip())])
    print circlepos 
circle.close()
def circleChange(circlepos):
    global x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8
    for coord in circlepos:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        x3=int(coord[2][0])
        x4=int(coord[3][0])
        x5=int(coord[4][0])
        x6=int(coord[5][0])
        x7=int(coord[6][0])
        x8=int(coord[7][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        y3=int(coord[2][1])
        y4=int(coord[3][1])
        y5=int(coord[4][1])
        y6=int(coord[5][1])
        y7=int(coord[6][1])
        y8=int(coord[7][1])
   
def blueChange():
    
    (x,y)=t1.pos()
    d=math.sqrt(math.pow((x1-x),2) + math.pow((y1-y),2))
    d1=math.sqrt(math.pow((x2-x),2) + math.pow((y2-y),2))
    d3=math.sqrt(math.pow((x3-x),2) + math.pow((y3-y),2))
    d4=math.sqrt(math.pow((x4-x),2) + math.pow((y4-y),2))
    d5=math.sqrt(math.pow((x5-x),2) + math.pow((y5-y),2))
    d6=math.sqrt(math.pow((x6-x),2) + math.pow((y6-y),2))
    d7=math.sqrt(math.pow((x7-x),2) + math.pow((y7-y),2))
    d8=math.sqrt(math.pow((x8-x),2) + math.pow((y8-y),2)) 
    if d<=30:
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    
    if d1<=30:
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    if d3<=30:
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    if d4<=30:
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    if  d5<=30:
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    if  d6<=30 :
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    if d7<=30:
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
    if d8<=30 :
        t1.setheading(0)
        t1.fillcolor("Blue")
        t1.circle(50)
circleChange(circlepos)
blueChange()
def keyup():
    t1.forward(50)
    blueChange()


    
def keydown():
    t1.backward(50)
    blueChange()


    
def keyleft():
    t1.left(90)


def keyright():
    t1.right(90)


def mousegoto(x,y):
    t1.setpos(x,y)
    blueChange()
 
def addKeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")

def addMouse():
    wn.onclick(mousegoto)
def gamePlay():
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()

gamePlay()