# Enter a sentence and remove the repeated word



def RemoveIthWord(list, word, N): 
    count = 0
      
    for i in range(0, len(list)): 
        if (list[i] == word): 
            count = count + 1
              
            if(count == N): 
                del(list[i]) 
                return True
                  
    return False
  
# Driver code 
input_string = input("Enter a sentence separetd by space: ") 
list = input_string.split()
word = str(input("Choose the repeated word: "))
print(list)
N = 2
  
flag = RemoveIthWord(list, word, N) 
  
if (flag == True): 
    print("Updated list is: ", list) 
else: 
    print("Item not Updated")