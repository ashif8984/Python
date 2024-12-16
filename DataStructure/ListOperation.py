# Basic List operation

def decorator():
	print("----"* 10)

def list_count(list1, item):

	count = 0
	for i in list1:
		if i == item:
			count +=1


	return count

list1 = [1,2,5,6,7,4,5,2,2,3]
print("Original List: {}".format(list1))

# reverse list
list1.reverse()


decorator()
print("Reverse list : {}".format(list1))
decorator()



# Count the element occurence
print(list1)
item = int(input("Enter a element:"))
res = list_count(list1, item)
print("Number of occurence: {}".format(res))
decorator()





