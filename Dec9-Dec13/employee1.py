class Employee:
    company_name="Abcd"
    location="calicut"
    def __init__(self,ID,name,salary):
        self.emp_id = ID
        self.emp_name =name
        self.emp_salary = salary
    def display_details(self):
        return f" {self.emp_id} {self.emp_name} {self.emp_salary}"
emp1=Employee(101,"Nithin",50000)
emp2=Employee(102,"Jango",70000)
print("Details of first employee is",emp1.display_details())
print("Details of second employee is",emp2.display_details())


       
