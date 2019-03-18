"""
In Josephus Problem, each soldier lined by to form circle
The sword was handed to person in 1st postion
Starting with A...upton n soldiers
A killed B and sword was passed to C
C killed D and Sword was passed to E
and this pattern goes on until last persion was live

This problem helps to find the right postion to stand to be winner
Condition - 1.)you know the starting point
            2.)there is rule to person is out next to other ie alterntively
"""

from pythonds.basic.queue import Queue
import time

def safe_postion(num_soldiers):
    queue_sol = Queue()  # Declare an Empty Queue

    # Adding the list-num_soldiers to Queue using push
    for name in num_soldiers:
        queue_sol.enqueue(name)

    # looping through the soldires and killing the next to it
    # list_a =[]
    print("Original Circle:%s " %(queue_sol.items))
    while queue_sol.size() > 1:
        for i in range(1):

            k = queue_sol.enqueue(queue_sol.dequeue())
            print('-' *30)
            #s = s.join(queue_sol.items)
            print("Remaining Soldier:","".join(queue_sol.items))
            #print("Remaining Soldier:%s" % (queue_sol.items))
            print('-' * 30)
            #print('%s Kills: '%(queue_sol.items[0]))



        n = queue_sol.dequeue()
        print(queue_sol.items[0] + ' Kills: ' + n)
        time.sleep(1)

    return queue_sol.dequeue()


def main():
    print("--"*20)
    print('Josephus Numberphille')
    print("--"*20)
    print('Soldiers form a circle')
    print('First person(A) has the Sword and kills the person next to him')
    print('This is repeated until last person Alive')

    print('')
    soldiers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    res = safe_postion(soldiers)
    print('The person who"ll be alive is:' + res)


if __name__ == '__main__':
    main()



