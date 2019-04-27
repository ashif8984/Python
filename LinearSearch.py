
"""
Linear Search Algorithm
"""

def linearSearch(alist, num):
	global pos
	pos = 0
	found = False

	while pos < len(alist) and not found:
		if alist[pos] == num:
			found = True
		else:
			pos += 1

	return found

# Enter the list elements
test_list = [1,6,7,3,4]

# num to search for 
num = 3

if linearSearch(test_list,num):
	print("Found at %d" %(pos))
else:
	print("not Found")

#print(linearSearch(test_list,num))