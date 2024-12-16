"""
Fibonacci Series
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 

"""

print("Enter the number of terms:")
term = int(input())

first = 0
second = 1
next =0 



for i in range(0,term):
	if i<=1:
		next = i
	else:
		next = first + second
		first =second
		second =next

	print(next, end = " ")


