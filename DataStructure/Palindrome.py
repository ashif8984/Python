# Check if the string/number is palindrome or not

"""
Palindrome string: malayalam, madam, mam etc
Palindrome number : 121, 232, 554455 etc
"""


def check_palindrome(str):
	
	rev = str[::-1]
	print(rev)

	if rev == str:
		return True
	else:
		return False




print("Enter any word: ")
input_string = str(input())

result = check_palindrome(input_string)

if result:
	print("Palindrome")
else:
	print("Not a plaindrome")




