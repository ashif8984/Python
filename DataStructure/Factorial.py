# Factorial of a number

def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num-1)


print("Enter a number")
num = int(input())
res = factorial(num)

print("Factorial of {0} = {1}".format(num, res))

