ezan = {
    'name': 'ezan',
    'age': 18,

    'hair': 'brown',
    'cool': True ,
}

print(ezan)

class Person(object): #use class to make object
    def __init__(
    self, name, age ,hair, color, hungry) : #initialize
    #first object inside of a class is self
        self.name = 'ezan'
        self.age = 18

        self.hair = 'brown'
        self.cool = True
    def eat(self,food):
        print("EAT {f}".format(f = food))
        self.hungry = food

    def play(self, game):
        print("Play {p}".format(p = game))
    self.play = game

    def birth(self,person):
        kids = Person(name = " lail", age = 18, hair = 'black', color = 'blue', hungry = True)
ezan = Person( name = "ezan", age = 18,  hair = "black", cool = True, hungry = False)
print(ezan.name)
print('I am hungry')

Austin = Person(name = 'austin', age = 18,  hair = "Shrek", cool = False, hungry = True)
