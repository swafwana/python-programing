class Employee:
	Basic=0
	TA=0
	DA=0
	def salary(self):
		print("Salary ",self.Basic+self.TA+self.DA)
emp1=Employee()
emp1.Basic=2000
emp1.TA=1000
emp1.DA=1500
emp1.salary()

emp2=Employee()
emp2.Basic=22000
emp2.TA=1050
emp2.DA=1550
emp2.salary()

emp3=Employee()
emp3.Basic=25000
emp3.TA=1950
emp3.DA=1850
emp3.salary()

