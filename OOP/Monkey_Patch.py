
"""
A MonkeyPatch is a piece of Python code which extends or modifies other code at runtime (typically at startup).

For instance, consider a class that has a method get_data. 
This method does an external lookup (on a database or web API, for example), and various other methods in the class call it. 
However, in a unit test, you don't want to 
depend on the external data source - so you dynamically replace the get_data method with a stub that returns some fixed data
"""
class Employee:

	def emp_func(self):

		print("This Employee function")


def monkey_function():
	print("This is Monkey Fucntion")



Employee().emp_func()

Employee.emp_func = monkey_function # modifying the behviour of emp_func by overwriting with diff fucntion

Employee.emp_func()