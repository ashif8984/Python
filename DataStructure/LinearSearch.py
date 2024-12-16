#Linear Search



def linear_search(list, num):
	
	for i in range(0, len(list)):
		
		if list[i] == num:
			global result
			result = i
			return True
		

list = [1,2,3,4,56,7,8]
print(list)

count = 0
while count< 4:

	num = int(input("Enter a number"))
	res = linear_search(list, num)


	if res ==True:
		print("Item {} at {}".format(num, result))
			
	else:
		print("Item {} not found".format(num))
			

	count +=1
	print("--" *10)






