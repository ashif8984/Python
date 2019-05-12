
'''
Bubble- Sort: 
The bubble sort make
s multiple passes through a list. 
It compares adjacent items and exchanges those that are out of order. 
Each pass through the list places the next largest value in its proper place. 
In essence, each item “bubbles” up to the location where it belongs.
'''


def bubble_sort(alist):
	# Traverse from last to first through the list
	for passnum in range(len(alist)-1, 0, -1):

		# Each for loop below goes 1 round and places the largest element in the last and continues
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i] # swapping


# Sample List
alist = [1,6,7,8,3,2]
alist2 = [99,34,123,1,5]

# Function call
bubble_sort(alist)
print(" The Sorted list using Bubble Sort:")
print(alist)


