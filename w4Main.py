import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def wind(size,turns,sides,angle,bigger):
    for i in range(sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
wind(20,20,10,90,30)
wn.exitonclick()