import turtle
t1=turtle.Turtle()
wn=turtle.Screen()
def drawSquareAtSave(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks
import turtle
t1=turtle.Turtle()
wn=turtle.Screen()
def drawSquareAtSave(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks
def drawSquareFrom(tracks):
    t1.penup()
    t1.setpos(tracks[0])
    t1.pendown()
    for i in range(0,4):
        t1.forward(100)
        t1.right(90)
def lab7a():
    size=100
    pos=(0,0)
    mytrack=drawSquareAtSave(size,pos)
    print mytrack
def lab7b():
    tracks=[(12.00,10.00), (65.00,10.00), (65.00,-40.00), (12.00,-40.00)]
    mydrawSquareFrom(tracks)
def main():
    lab7a()
    lab7b()
main()
def lab7b():
    tracks=[(12.00,10.00), (65.00,10.00), (65.00,-40.00), (12.00,-40.00)]
    drawSquareFrom(tracks)
def main():
    lab7a()
    lab7b()
main()