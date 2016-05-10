import turtle
wn=turtle.Screen()

def milk():
    allData=list()
    allData=[ ["Coffee","Water","Milk","Icecream"],
        ["Espresso","No","No","No"],
        ["Long Black","Yes","No","No"],
        ["Flat White","No","Yes","No"],
        ["Cappuccino","No","Yes - Frothy","No"],
        ["Affogato","No","No","Yes"],
    ]
    for i in range(len(allData)-1):
        print allData[i+1]
    data=allData[1:]
    percent=0
    for c in data:
        if c[2]=="Yes":
            percent+=1
            percent=float(percent)
            per=str(percent/5*100)
    print "Using Milk percent is "+per+"%"

def grade():
    grade=list()
    grade=[["English" ,100],
        ["Math" ,200],
        ["English" ,200],
        ["Math" ,200],
        ["English" ,100],
        ["Math" ,300],
    ]
    sum=dict()
    sum={"English":0,"Math":0}
    en=0
    ma=0
    for i in grade:
        if i[0]=="English":
            en+=1
        elif i[0]=="Math":
            ma+=1
    for i in grade:
        if i[0]=="English":
            sum["English"]+=i[1]
        elif i[0]=="Math":
            sum["Math"]+=i[1]
    print "Math sum is "+str(sum['Math'])
    print "English average is "+str(sum['English'])
    print "Math average is "+str(sum['Math']/ma)
    print "English average is "+str(sum['English']/en)

def letitbe():
    lycs=list()
    lycs=[
    "When I find myself in times of trouble",
    "Mother Mary comes to me",
    "Speaking words of wisdom let it be",
    "And in my hour of darkness",
    "She is standing right in front of me",
    "Speaking words of wisdom let it",

    "Let it be let it be",
    "Let it be let it be",
    "Whisper words of wisdom let it be",

    "And when the broken-hearted people",
    "Living in the world agree",
    "There will be an answer let it be",
    "For though they may be parted",
    "There is still a chance that they will see",
    "There will be an answer let it be",

    "Let it be let it be",
    "Let it be let it be",
    "Yeah there will be an answer let it be",
    "Let it be let it be",
    "Let it be let it be",
    "Whisper words of wisdom let it be",

    "Let it be let it be",
    "Ah let it be yeah let it be",
    "Whisper words of wisdom let it be",

    "And when the night is cloudy",
    "There is still a light that shines on me",
    "Shine on until tomorrow let it be",
    "I wake up to the sound of music",
    "Mother Mary comes to me",
    "Speaking words of wisdom let it be",

    "Let it be let it be",
    "Let it be yeah let it be",
    "Oh there will be an answer let it be",
    "Let it be let it be",
    "Let it be yeah let it be",
    "Whisper words of wisdom let it be"
    ]
    doc=lycs
    d=dict()
    for i in range(len(doc)):
        for c in doc[i].split():
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
    a=list()
    for i in d.values():
        a.append(i)
    b=list()
    for i in d.keys():
        b.append(i)
    for i in range(len(a)):
        if a[i]>=20:
            print b[i]

def lab10():
    letitbe()
    milk()
    grade()
def main():
    lab10()

main()
wn.exitonclick()