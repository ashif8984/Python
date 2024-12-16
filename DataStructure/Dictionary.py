'''
x = {
	1: "A",
	2: "B",
	3: "C",
	4: "D"
}

# Values
print("Values :")
for i in x:
	print(x[i])
	

# Keys
print("Keys :")
for i in x:
	print (i)

# Keys and Values

for i in x:
	print("{},{}".format(i, x[i]))

for k,v in x.items():
	print(k,v, sep=":")



Create a dictionary and display its keys alphabetically.
Display both the keys and values sorted in alphabetical order by the key.
Same as part (ii), but sorted in alphabetical order by the value.
'''

dict = {
	5:"B",
	6:"A",
	7:"D",
	1:"E",
	2:"C"

}

for k,v in dict.items():

	print(k,v)

for i in sorted(dict.keys()):
	print(i)

for i in sorted(dict.values()):
	print(i)

for i in sorted(dict):
	print(i, dict[i])




