# print prime numbers:


def print_prime(start, end):
	for val in range(start, end+1):

		if val >1:
			for num in range(2, val):
				if (val % num)==0:
					break
			else:
				print(val)

def check_prime(num):
	
	if num > 1:
		for i in range(1, num):
			if (num % i) == 0:
				return ("Number is not prime")
			else:
				return ("Number is prime")

start = 1
end = 100
# print_prime(start, end)

result = check_prime(13)
print(result)
