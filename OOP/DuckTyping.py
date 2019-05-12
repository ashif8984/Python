# Duck Typing

"""
If it quacks like a duck and fly like a duck- It definately has to be duck
No matter which class object you create, it has to have the method called fly or quack

"""

class Duck:
	def quack(self):
		print("Quack-Quack")

	def fly(self):
		print("Fly-Fly")

class Chicken:
	def quack(self):
		print("I am Chicken but can Quack Quack")

	def fly(self):
		print("I am Chicken but can Fly-Fly")


class Bird:
	def behavoiur(self, object):
		object.quack()
		object.fly()


# duck1 = Duck()
duck1 = Duck()
chic1 = Chicken()


bird1 = Bird()
# bird1.behavoiur(duck1)
bird1.behavoiur(chic1)

