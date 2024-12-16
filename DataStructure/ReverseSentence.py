# Reverse the word in a sentence


def rev_func(str):

	str = str.split(' ')
	new_str = str[::-1]
	new_str = ' '.join(new_str)
	return new_str


def find_word(str, sub_str):

	if str.find(sub_str) == -1:
		print("No")
	else:
		print("Yes")


# str = "My name is Ashif"

str  = str(input("Enter any sentence: "))


print("--"*10)
print("Original sentence:   {}".format(str))


res = rev_func(str) # Function Call

print("Reversed sentence:   {}".format(res))

print("--"*10)


# word = "dog"
word = input("Enter any word from the string or anything: ")
print("Is {} present in the string? ".format(word))
find_word(str, word)
