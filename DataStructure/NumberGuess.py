# Guess Number Game

import random  # import random module

# Generate number
num = random.randint(0, 9)
print(num)

count = 0
guess = 0

while guess!=num and guess!="exit":

    guess = input("Guess a number")
    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess < num:
        print("Guess a higher number")
    
    elif guess > num:
        print("Guess a lower number")
    
    else:
        print("You guess it Right!!")
        print("The Number was {0} and you took {1} attempts to guess".format(num, count))