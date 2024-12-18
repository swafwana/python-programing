class Fruits:
    def eat(self):
        print("We can eat fruits")
class orange(Fruits):
    pass
class apple(Fruits):
    def eat(self):
        print("Apple is sweet")
orange1=orange()
orange1.eat()
apple1=apple()
apple1.eat()
