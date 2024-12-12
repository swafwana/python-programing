from Mathoperations.Basic_operations import arithmetic
from Mathoperations.Geometry import area
print("Arithmetic Operations:")
print("5+3= ",arithmetic.add(5,3))
print("10-7=",arithmetic.substract(5,3))
print("5*3= ",arithmetic.multiply(5,3))
print("8/2= ",arithmetic.divide(8,2))
print("8/0= ",arithmetic.divide(8,0))
#Area Calculations
print("\n Area Operations: ")
print("Rectangle(length=5,width=3):",area.rectangle_area(5,3))
print("Circle(radius=7):",area.circle_area(7))
print("Triangle(base=4,height=5): ",area.triangle_area(4,5))
