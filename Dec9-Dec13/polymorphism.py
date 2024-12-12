class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        print("Area of circle",self.pi*self.radius**2)
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        print("Area of rectangle",self.length*self.width)
def area(shape):
    shape.calculate_area()
circle=Circle(2)
rectangle=Rectangle(4,5)
area(circle)
area(rectangle)
