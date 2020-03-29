
# program to find smallest n greatest form the list

def max_min(list):
    list.sort()
    max = max(list)
    min = min(list)
    print("Min value {0}:".format(min))
    print("Max value {0}:".format(max))

def max_min2(list):
    list.sort()
    max , min = list[-1], list[0]
    print("Max Value: {0}".format(max))
    print("Min Value: {0}".format(min))


length = int(input("Enter the length your list"))
list = []
for e in range(1, length + 1):
    num = int(input("Enter your {0} list element".format(e)))
    list.append(num)
    
# list = [1,2,5,67,98,23,45]2

print(list)
# max_min(list) # function-1
max_min2(list)  # function-2



