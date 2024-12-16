# List Sum


string_ip=input("Enter list element seprated by space: \n")
list1 = list(string_ip.split())


sum = 0
for i in list1:
	sum += int(i)

print("Sum is {}".format(sum))

list1.sort()

print("Largest element in the list : {}".format(list1[-1]))
print("Smallest element in the list : {}".format(list1[0]))
print("Second Largest element in the list : {}".format(list1[-2]))
