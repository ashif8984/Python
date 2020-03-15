# Palindrome Chekcer
# to Check if the string reads same from back and front both
# example - radar, madam, Malayalam

'''
We will be using DEQUEUE data strucute as insertion/Deletion hapens both ends
Step 1: Get the input sting from user
Step 2: Create an empty Dequeue
Step 3: Push each item inot the dequeue like normal queue
step 4: Until the Queue is empty(size > 1) take one item out from back and front both
step 5: compare each item
    step 5.1: if they equal = return True(Palindrome)
    step 5.2: Not equal = return False
'''

from pythonds.basic.deque import Deque

def palindrome_checker(newString):
    aDeqeue = Deque()
    for item in newString:
        aDeqeue.addRear(item)

    Status = "String is Palindrome"

    while aDeqeue.size() > 1  and Status:
        front = aDeqeue.removeFront()
        rear = aDeqeue.removeRear()

        if front != rear:
            Status = "String NOT Palindrome"

    return Status

def palindrome_checker2(str):

    newstr = str[::-1]
    # print(newstr)

    if newstr == str:
        print ("Palindrome")
    else:
        print ("Not-Palindrome")

def palindrome_checker3(string):
    
    right = len(string) -1
    left  = 0

    while right >= left:
        if not string[left] == string[right]:
            return False
        else:
            right = right -1
            left = left + 1

        return True


# Driver Code
i =0
print ("--You will be 3 chance to check--")
while i < 3:
    print("Enter your String to check")
    random_string = str(input())

    print(palindrome_checker3(random_string))
    i += 1
