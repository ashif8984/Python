# Check Whether a number is prime

def check_prime(num):

	for i in range(2, num):
		if num%i == 0:
			return False
	else:
		return True

# Let the user have 3 attempt to check 
attempt = 0
while (attempt < 3):
	print("Enter a number:")
	num = int(input())
	res = check_prime(num)

	if res == 1:
		print("{} is prime".format(num))
	else:
		print("{} is not prime".format(num))
	attempt +=1

	


