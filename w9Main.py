import matplotlib
import matplotlib.pyplot as plt
def charCount():
    sentence=raw_input(" input word: ")
    d=dict()
    for i in sentence:
        if i in d:
            d[i]=d[i]+1  
        elif i not in d:
            d[i]=1
    print d,
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()  

    
def countDigitalsLatters(word):
    d=dict()
    d={"word":0, "number":0}
    for i in word:
        if i.isdigit()==True:
            d["number"]=d["number"]+1
        elif i.isdigit()==False:
            d["word"]=d["word"]+1
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()  

def foundappliances():
    myh={ 'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    friendh={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
    print "only mine : " ,myh.difference(friendh)
    print "only friend's:" , friendh.difference(myh)
    print  "how many: ",len(myh)+len(friendh-myh)
    print "both : ", myh.intersection(friendh)
    print "all: ", myh.intersection(friendh)

def lab8():
    charCount()
    word=raw_input("input word")
    countDigitalsLatters(word)
    foundappliances()
def main():
    lab8()
main()
raw_input("20")
