class Employee:
	Basic=0
	TA=0
	DA=0
	def salary(self):
		return f" {self.Basic+self.TA+self.DA} "
emp1=Employee()
emp1.Basic=2000
emp1.TA=1000
emp1.DA=1500
print("Salary of first employee is ",emp1.salary())

emp2=Employee()
emp2.Basic=22000
emp2.TA=1050
emp2.DA=1550
print("Salary of second employee is", emp2.salary())

emp3=Employee()
emp3.Basic=25000
emp3.TA=1950
emp3.DA=1850
print("Salary of third employee is", emp3.salary())

