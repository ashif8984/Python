
# Python OOP Programming

# Source: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=45s
# Corey Scafer
# Lecture 3: Class Methods and Static Methods

"""
By default regular methods takes up instance and first arg(self)
Class Method: Take class(cls) as the first arg
Class Method starts with decorator: @classmethod

Static Method: dont pass anything- class or instance
Doesnt depend on Class or instance


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


	@classmethod

	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@staticmethod

	def is_working(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



emp1 = Employee("Ashif", "Eqbal", 1000)
emp2 = Employee("Sonu", "Satya", 5000)

#Employee.set_raise_amt(1.05)


# print(Employee.raise_amount)
# print(emp1.raise_amount)

import datetime

my_date  = datetime.date(2018, 6, 10)
print(Employee.is_working(my_date))
