import os
mydir=os.getcwd()
def reccoords():
    aFile='reccoords.txt'
    file=open(aFile,'w')
    file.write('0,0,100,100'+'\n')
    file.write('200,200,150,150'+'\n')
    file.close()
    return aFile

def getRectangleFromFile(aFile):
    frec=open(aFile)
    coords=[]
    for line in frec:
        line1=line.split(',')
        x1=int(line1[0])
        y1=int(line1[1])
        x2=int(line1[2])
        y2=int(line1[3].strip())
        coords.append([(x1,y1),(x2,y2)])
    frec.close()
    return coords

def drawSquareWithCoords(coords):
    x=list()
    y=list()
    for coord in coords:
        x.append(coord[0][0])
        x.append(coord[1][0])
        y.append(coord[0][1])
        y.append(coord[1][1])
        
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    
    t1.goto(x[0],y[0])
    t1.goto(x[0],y[1])
    t1.goto(x[1],y[1])
    t1.goto(x[1],y[0])
    t1.goto(x[0],y[0])
    
    t1.penup()
    t1.goto(x[2],y[2])
    t1.pendown()
    
    t1.goto(x[2],y[3])
    t1.goto(x[3],y[3])
    t1.goto(x[3],y[2])
    t1.goto(x[2],y[2])
    wn.exitonclick()
def Number():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        str="{0}\t".format(i)
        fout.write(str)
        if i%2==0:
            fout.write('\n')
    fout.close()
def append():
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    filename2='ouputNumber.txt'
    myfilename2=os.path.join(mydir,filename2)
    file1=open('python.txt','a')
    file2=open('outputNumber.txt','r') 
    for line in file2:
        file1.write(line)
    file1.close()
    file2.close()
    file1=open('python.txt','r')
    print file1.read()
    file2.close()
    
def lab14():
    Number()
    append()
    aFile=reccoords()
    coords=getRectangleFromFile(aFile)
    drawSquareWithCoords(coords)
    

def main():
    lab14()

main()