# print prime numbers:

start = 1
end = 100

for val in range(start, end+1):

	if val >1:
		for num in range(2, val):
			if (val % num)==0:
				break
		else:
			print(val)

