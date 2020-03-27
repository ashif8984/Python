
"""
This program explains Lambda(), Map(), Filter() and Reduce()
"""

"""
Lambda Function :

    In Python, anonymous function is a function that is defined without a name.
    While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.
    Hence, anonymous functions are also called lambda functions.

    Syntax of Lambda Function in python
        lambda arguments: expression

"""
print("---"*15)
print(" Lambda Example")
print("---"*15)
# A function to return cube of a number
def cube(y): 
    return y*y*y; 

num = 7
print("Cube of {0} using Normal Function is {1}".format(num, cube(num)))

# Lambda to return the cube of a number
g = lambda x: x*x*x 
print("Cube of {0} using Lamda Function is {1}".format(num, g(num)))


# another example of lamnda to add 10 to number

a = 5
x = lambda a : a + 10
# print(x(a))
print("Adding  10 to {0} become {1}".format(a, x(a)))

print("---"*15)
# --------------------------------------------

"""
Map() - Allows you to inject a function (a lambda func)to each element of the list
"""

print("---"*15)
print("Map() Example")
print("---"*15)
# lambda with map()

# A function to return square of each element of a list. List is important here. Unlike above cube fucntion
# this applies cube function to each element
def square(numlist):
    result = []
    for i in numlist:
        result.append(i ** 2)

    return result

alist = [1,3,5]
print("Original List {0}".format(alist))
print("Square of list elements using normal function:" , square(alist))

# using single line map
result = list(map(lambda x: x**2, alist))
# print(result)
print("Square of list elements using Lambda function: {0}".format(result))

print("---"*15)
# ------------------------------------------------

"""
Filter() - is used to return a list of number/strings for which your lambda function holds TRUE
           It will filter only those elements which your lambda func returns True
"""
print("---"*15)
print("Filter() Example")
print("---"*15)
# lambda with filter()
blist = range(-5,5) # list to print element from -5 to 5
print("Original List {0}".format(blist))

result2 = list(filter(lambda x: x>0, blist))
print("List having elements >0 elements{0}".format(result2))

# Another example
clist = ["Ashif", "Arun", "Biswa", "Sachin", "Orange"]
print("Orignal List {0}".format(clist))

# Returns only those element from clist whose name starts with letter- "A"
result3 = list(filter(lambda x: True if x.startswith('A') else False , clist))
print("List having elements/names which starts with A {0}".format(result3))


# Another example for filter
# print the Odd number form the list
li = [2,3,4,5,6,23,445,67]
print("Original List {0}".format(li))

finalli = list(filter(lambda x: (x%2 != 0), li))

print("List of only Odd number from the orig list {0}".format(finalli))

print("---"*15)
# ------------------------------------------------

"""
Reduce() - Reduce is useful function for performing some computation on a list items and returning the result. 
           It applies a rolling computation to sequential pairs of values in a list. 
           For example, if you wanted to compute the product of a list of integers from the list items.
           Unlike Map() and Filter() you have to import Reduce() from functools
"""
print("---"*15)
print("Reduce() Example")
print("---"*15)
# lambda with reduce()

# Function to find product of a list of integers from the list items ie multply all elements from list

product = 1
list = [2,3,4,5]
for i in list:
    product *=  i

print("Product of all the elements from the list- {0}".format(product))

# using reduce()

from functools import reduce
result4 = reduce(lambda x,y : x * y, list)
print("Product of all the elements from the list-using Reduce() {0}".format(result4))

print("---"*15)
"""
References:
https://www.programiz.com/python-programming/anonymous-function
https://book.pythontips.com/en/latest/map_filter.html
https://www.w3schools.com/python/python_lambda.asp
"""