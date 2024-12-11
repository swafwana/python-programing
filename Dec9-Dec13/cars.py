class Car:
    company="a"
    price=0
    color="b"
    def printer(self):
        return f"{self.company},{self.price},{self.color}"
car1=Car()
car1.company="MaruthiSuzuki"
car1.price=600000
car1.color="Black"
print("Details of car1 is ",car1.printer())

car2=Car()
car2.company="Benz"
car2.price=1000000
car2.color="Blue"
print("Details of car1 is ",car2.printer())

car3=Car()
car3.company="Nano"
car3.price=100000
car3.color="Yellow"
print("Details of car1 is ",car3.printer())

car4=Car()
car4.company="Brezza"
car4.price=1200000
car4.color="Grey"
print("Details of car1 is ",car4.printer())
    

