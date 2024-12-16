# Count the number of vowels in a word/sentence

def vowel_count(string):
	
	count = 0
	alpha = 'aeiou'
	for i in string:
		if i in alpha:
			count += 1
		else:
			continue

	return count



string = "Love is blind"


count = vowel_count(string)
print(string)
print("No of Vowels = {}".format(count))


