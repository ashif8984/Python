# Python OOP Programming

# Source: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=45s
# Corey Scafer
# Lecture 1: Class

"""
 Class - Blueprint for creating Object- eg: Employee
 Object - Instance of the class. eg: emp1, emp2...
 Method- Function associated within a class. eg : fullname(), average_salary()

-
__init__ : Method used to intialize your instance of the class
           So you do not have to write emp1.name, emp1.salary etc for each and every employee(instance) you create
           Now each varible inside __init__ becomes class variable
Fullname() : Class Method

Employee.Fullname(emp1): This actually happens in background. You have to pass the instance name as arg to the method
emp1.Fullname() : You do not have to pass the arg here.

"""

class Employee:
	
	# like constructor
	def __init__(self, first,last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.'+last + '@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


'''
# instance of Employee CLass

emp1 = Employee()
emp2 = Employee()

# Instance variable- unique to each instance
emp1.first = "Ashif"
emp1.last = "Eqbal"
emp1.email ="ashif898@gmail.com"
emp1.pay =1000

emp2.first = "Sonu"
emp2.last = "Sataya"
emp2.email ="sonu@gmail.com"
emp2.pay =2000

print(emp1.email) 
print(emp2.email)

'''
emp1 = Employee("Ashif", "Eqbal", 1000)
emp2 = Employee("Sonu", "Satya", 5000)

print(emp1.email)
print(emp1.fullname())
print(emp2.fullname())

print(Employee.fullname(emp1))

#print full name
#print('{} {}'.format(emp1.first, emp1.last))







