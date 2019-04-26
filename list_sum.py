
# Sum of elements of the list
"Get the Sum of the number in the list and return the name of script"

#import the sys and os modules
import sys    
import os

#get the name of the script
file_name =  os.path.basename(sys.argv[0])

# Enter the Integers with space separation
str = str (input ("Enter number(s) with space: "))

# convert to the list
list = str.split (" ")


# convert each element as integers and add to array
li = []
for i in list:
	li.append(int(i))

# add the elements of the array
sum = 0
for e in li:
    sum += e

# display the sum
print("Sum of the numbers: %d" %int(sum))

# display name of file and intergers enterred
print("Name of the script:%s \nNumber provided:%s" %(file_name, str))


