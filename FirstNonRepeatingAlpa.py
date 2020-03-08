# This program calcualtes the 1st non-repeating alphabet in a given string

"""
Example: 
str1 = "aaaabcccdeee" # Answer: b
str2 = "abbbbcdeee" # Answer: a
str3 = "abc" # Answer: a

"""
def count_alpha(str):
    
    count_words =[] # List to store only unqiue/distinct values
    dict_words ={} # Empty dictonary for storing alphabet and their count


    for i in str:
        if i in dict_words:
            dict_words[i] += 1
        else:
            dict_words[i] = 1
            count_words.append(i)
    
    # print(count_words)
    #print(dict_words)

    for elem in count_words:
        if dict_words[elem] == 1:
            return elem

# Driver Code

str1 = "aaaabcccdeee" 
str2 = "abbbbcdeee" 
str3 = "abc" 


print("--" *15)
print("Orginal String1", str1)
result1 = count_alpha(str1)
print("First Non Repeating Letter",result1)

print("--" *15)
print("Orginal String1", str2)
result2 = count_alpha(str2)
print("First Non Repeating Letter",result2)

print("--" *15)
print("Orginal String1", str3)
result3 = count_alpha(str3)
print("First Non Repeating Letter",result3)