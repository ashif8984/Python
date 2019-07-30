# Dunder methods:

"""
__init__
__repr__
__str__

These are called dunder method
__repr__ : Always work as fallback method for __str__. If __str__ not present this gets executed.Used for debugging
__str__ : Is more readable form and prints string as per user-friendly readable format

"""



class Employee:

	def __init__(self, fname, lname, pay):
		self.fname= fname
		self.lname= lname
		self.pay= pay
		self.email = fname + "."+lname+'@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	def __repr__(self):
		return "Employee('{}','{}',{})".format(self.fname, self.lname,self.pay)

	def __str__(self):
		return "{}-{}".format(self.fname, self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())


emp1 = Employee("Ashif","Eqbal",25000)
emp2 = Employee("Sonu","Satya", 50000)

# print(emp1.lname)
# print(emp1.fname)
# print(emp1.pay)
print(emp1.fullname())

# print(emp1.__str__())
print(emp1.__repr__())

print(repr(emp1))
print(str(emp1))

# print(3+4) # will print 3 because they use special method called dunder add: __add__()
# print(int.__add__(3,4)) # Will give the same result

# print(str.__add__('3','4')) # add dunder with string

# So we can customize how the dunder add method works for our objects
# Our python program doesnot know how to add objects
# you can do so by making use of __add__ method
# Ex: add the 2 emp objects to reutn their salry?
# more: https://docs.python.org/3/reference/datamodel.html#special-method-names
print(emp1 + emp2)
print(emp1.__add__(emp2))


# print(len("test")) # print the length of the string
# By default in the background this also uses a dunder method called: __len__()

# print("test".__len__())

#lets use this in our objects
# Lets suppose len when passed, should return lenght of fullname
# we have define __len__ method

print(len(emp1))
print(emp1.__len__())

