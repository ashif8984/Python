#Turtle Example of Recursion

import turtle

# checking Arun commit
# Sonal comment 


myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, linelen):
    if linelen > 0 :
        myTurtle.forward(linelen)
        myTurtle.left(90)
        drawSpiral(myTurtle,linelen-1)

drawSpiral(myTurtle, 100)
myWin.exitonclick()
'''

def tree(branchlen,t):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15, t)
        t.left(40)
        tree(branchlen-15, t)
        t.right(20)
        t.backward(branchlen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    #t.begin_fill()
    t.pencolor('green')
    t.width(10)
    t.speed(100)
    tree(75, t)
    myWin.exitonclick()
main()
'''
