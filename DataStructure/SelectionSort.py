
"""
Selection Sort:
The selection sort improves on the bubble sort by making only one exchange 
for every pass through the list. 
In order to do this, a selection sort looks for the largest value as it makes a pass and, 
after completing the pass, places it in the proper location.
"""
def selection_sort(alist):

	for fillshot in range(len(alist)-1, 0, -1):
		postionofmax = 0 # setting 0 as the marker position

		# comparing the 1st and 0th element, if element at 1 is greater than 0th, 
		# then exchange the postionofmax marker
		for i in range(1, fillshot+1):
			if alist[i]> alist[postionofmax]:
				postionofmax = i

		# swapping the larger element at the index last
		alist[fillshot], alist[postionofmax] = alist[postionofmax], alist[fillshot]


# Test list
alist = [1,7,8,2]

selection_sort(alist)

print("After selection_sort:")
print(alist)
