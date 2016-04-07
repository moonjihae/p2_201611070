def year():
    year=raw_input("get year:")
    year=int(year)
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "leap year!"
    else:
        print "normal year!"



def updown():
    import random
    number=raw_input("input number(range 1~n) :")
    n=int(number)
    num=-1
    rn=random.randrange(1,n+1)
    guess=0
    print "number's range is 1~%f"%n
    while (rn !=num):
        num=int(input("input number :"))
        if (num >rn):
            print ("down")
        elif (num <rn):
            print ("up")
        guess +=1
    print (guess,"right")


def lab6():
      year()
      updown()
      
def main():
      lab6()
      

if __name__=="__main__" :
       main()