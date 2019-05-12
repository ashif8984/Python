
# Python OOP Programming

# Source: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=45s
# Corey Scafer
# Lecture 4: Inheritance
"""
Developer and Manager classes
Inheriting from Employee class

If you instantiate from Child Class(Developer class)
python Looks 1st in Developer class the init method
and if not finds one- it walks to be parent employee class

|  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object

"""
class Employee:

	raise_amount = 1.04
	
	# like constructor
	def __init__(self, first,last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.'+last + '@gmail.com'

	

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


# class developer inherits from Employee class
class Developer(Employee):
	raise_amount =1.05


	def __init__(self, first,last, pay, prog_lang):
		super().__init__(first, last, pay) #let main class handles rest of the variblae
		
		self.prog_lang = prog_lang


class Manager(Employee):

	def __init__(self, first,last, pay, employees= None):
		super().__init__(first, last, pay) #let main class handles rest of the variblae
		
		if employees is None:
			self.employees = []
		else:
			self.employees = employees


	def add_emp(self, emp):
		if emp in self.employees:
			self.employees.append(emp)



	def remove_emp(self, emp):
		if emp not in self.employees:
			self.employees.remove(emp)


		
	def print_emp(self):
		for emp  in self.employees:
			print('-->', emp.fullname())		

"""
dev1 = Employee("Ashif", "Eqbal", 1000)
dev2 = Employee("Sonu", "Satya", 5000)

"""
dev1 = Developer("Ashif", "Eqbal", 1000,"Python")
dev2 = Developer("Sonu", "Satya", 5000, "Java")


mgr1= Manager("Dinesh", "Kuamr", 9000, [dev1])

print(mgr1.email)
mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.print_emp()


# To check if the mgr1 is instance of particular class. Remember mg1 instance can be instance of Employee(base) & Manager class
# but not Developer class

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))


# To check Subclass of Base Class
print(issubclass(Developer, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
# printdev1(.pay)
# dev1.apply_raise()
# print(dev1.pay)
# # print(help(Developer))


# print(dev1.email)
# print(dev1.prog_lang)




# print(dev1.email)
# print(dev2.email)
