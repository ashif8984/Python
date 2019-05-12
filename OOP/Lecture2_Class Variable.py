
# Python OOP Programming

# Source: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=45s
# Corey Scafer
# Lecture 2: Class Variable

"""
 Class Variable : Variable defined inside the class and is common for all instance. eg: raise_amount, num_of_emps
 emp_1.__dict__ : Shows all the namespace of the instance of the class 
 Employee.__dict__ : Shows all the namespace of the class 

"""

class Employee:

	num_of_emps = 0
	raise_amount = 1.04 # Class Variable
	
	# like constructor
	def __init__(self, first,last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.'+last + '@gmail.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
	 
print(Employee.num_of_emps)
emp1 = Employee("Ashif", "Eqbal", 1000)
emp2 = Employee("Sonu", "Satya", 5000)

# print(Employee.__dict__)


# Employee.raise_amount = 1.05
emp1.raise_amount = 1.05 # On instantiating the class, it will become 2 since there 2 instance
# print(emp1.pay)
# emp1.apply_raise()

# print(emp1.pay)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

print(Employee.num_of_emps)

