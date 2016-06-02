class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "My dog name is ",self.name
        
    def talk(self,name):
        print "mung mung"
        
class ShihTzuDog(object):
    def talk(self,name):
        print "si si"

class Maltese(object):
    def talk(self,name):
        print "mal mal"
mydog.getName()
mydog.talk('dog')
shi=ShihTzuDog()
shi.talk('ShihTzuDog')
mal=Maltese()
mal.talk('Maltese')
raw_input("ddd")