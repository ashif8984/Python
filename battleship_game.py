#BattleShip
"""
The Ship is randomly placed in (x,y)position where x= row, y =col
You have been given 3 attempts to Identify the locaiton
Lastly answer will be provided to you about the location of ship

#If you detect the ship co-ordinate, my ship sinks

"""

import random

print("--" *20)
print ("--Welcome to the BattleShip game")
print("--" *20)


# Declare an Emtpy Board
board =[]

for i in range(0,5):
    board.append(["O"]*5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)
   
def random_row(board):
    return random.randint(0,len(board)-1)
def random_col(board):
    return random.randint(0,len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)
#Un-Comment the below 2 lines if you want to know the pos before hand
#print (ship_row)
#print (ship_col)

for chance in range(3):
    print ("-"*10)
    print("Chance :", + chance)
    print ("-"*10)
    print ("Guess the row")
    choice_row = int(input())
    print ("Guess the column")
    choice_col = int(input())
    if choice_row == ship_row and choice_col == ship_col:
        print ("Congratulation!! you sank my ship")
        break
    else:
        print("Better Luck Next time!")
print ("The location of my ship was :")
print (ship_row)
print (ship_col)

board[ship_row][ship_row] ='X'
print_board(board)
print('Thank you for playing this game!')

