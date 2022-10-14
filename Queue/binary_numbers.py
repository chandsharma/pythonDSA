"""
Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.
"""

from queue import Queue

queue = Queue()

queue.enqueue('1')
for i in range(10):
    front = queue.front()
    print(front)
    queue.enqueue(front+"0")
    queue.enqueue(front+"1")
    queue.dequeue()