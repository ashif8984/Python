

# Swap function
def swap_func1(a,b):
    c = 0
    c = a
    a = b
    b = c
    return (a,b) # Return type (mulitple values) using Tuple
    
def swap_func2(a,b):

    a,b = b,a # swap logic
    return (a,b)


a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))


print("Before Swap a={0} and b={1}".format(a,b))

# a,b = swap_func1(a,b) # Function call
a,b = swap_func2(a,b) # Function call

print("After Swap a={0} and b={1}".format(a,b))
# Comment : To Test Slack Integration

