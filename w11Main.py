import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
def sett2(x,y):
     t2.penup()
     t2.setpos(x,y)
     t2.pendown()
     t2.fd(150)
sett2(100,0)
def keyup():
         t1.fd(50)
         
def keydown():
         t1.backward(50)
def keyright():
         t1.right(90)
def keyleft():
         t1.left(90)
def addKeys():
         wn.onkey(keyup,"Up")
         wn.onkey(keydown,"Down")
         wn.onkey(keyright,"Right")
         wn.onkey(keyleft,"Left")
    
        
def mousegoto(x,y):
          t1.setpos(x,y)
          t1.pos=(x,y)
          if 100<x<250 and y==0:
             print "correct!"
def addmouse():
      wn.onclick(mousegoto)
wn.listen()
addKeys()
addmouse()
turtle.mainloop()
