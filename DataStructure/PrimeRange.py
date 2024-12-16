# to print prime number in the range

start = 50
end = 100

for val in range(start,end+1):
	if val>1:
		for i in range(2, val):
			if val % i == 0:
				break
		else:
			print(val)
