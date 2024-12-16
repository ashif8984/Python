# Binary Search


def binary_search(list, num):
	
	lower = 0
	upper = len(list)
	global mid
	
	while (lower<=upper):

		mid = (lower+upper) // 2

		if list[mid] == num:
			global pos
			pos = mid
			return True
		else:
			if list[mid] < num:
				lower = mid
			else:
				upper = mid
	return False


list = [1,2,3,4,5]
list.sort()


print("Original list : {}".format(list))
print("--" * 10)

count = 0
while (count < 4):
	# print("--"*10)
	num = int(input("Enter any number: "))
	print()
	if num in list:
		result = binary_search(list, num)
		print("Item {} is at {} postion".format(num, pos))
	else:
		print("item {} not found".format(num))

	print("--"*10)
	count += 1

