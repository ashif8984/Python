
# insertion sort

"""
Compare each element with its adjacent element.
If element left to the Key Element is greater than then shift the position
This continues till length of the list
"""

def insertion_sort(arr):

	for i in range(1, len(arr)):

		key = arr[i]

		j = i -1
		while j >=0 and key < arr[j]:

			arr[j+1] = arr[j]
			j -=1

		arr[j+1] = key

	return arr



arr = [1,6,7,3,2]

print("Original List: {}".format(arr))
print("After Insertion Sort: {}".format(insertion_sort(arr)))