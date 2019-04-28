
# Binary Search

"""
       Search a sorted array by repeatedly dividing the search interval in half.
       Begin with an interval covering the whole array.
       If the value of the search key is less than the item in the middle of the interval,
       narrow the interval to the lower half. Otherwise narrow it to the upper half.
       Repeatedly check until the value is found or the interval is empty.''
"""



# Function to calculate the binary search element
def binary_search(list, num):
    lower = 0
    upper = len(list)-1

    while lower <= upper:
        mid = (lower+upper) // 2
        if list[mid] == num:
            global pos
            pos = mid
            return True
        else:
            if list[mid]<num:
                lower = mid
            else:
                upper = mid




print("-"*15)
print ("Binary Search")
print("-"*15)

# User to input the list element
print ("Enter a list element separated by space ")

# Converting the list of type int
lista = [int(x) for x in input().split()]

#Display the Orginal List
print(lista)

lista.sort()
#Display the Sorted List
print("After Sorting")
print(lista)

# Select the number you want to search from the list
num = int(input("Select any number from your list:"))

if binary_search(lista, num):
    print("Found at", pos+1)
else:
    print("Not Found")
