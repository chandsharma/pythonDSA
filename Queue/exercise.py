"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
"""

from queue import Queue
from threading import Thread
from time import sleep

queue = Queue()

def place_order(orders):
    global queue
    for order in orders:
        queue.enqueue(order)
        print("order placed for ",order)
        sleep(0.5)

def serve_order():
    global queue
    sleep(1)
    while not queue.is_empty():
        sleep(2)
        print(queue.dequeue()," served")

orders = ['pizza','samosa','pasta','biryani','burger']

t1 = Thread(target=place_order,args=(orders,))
t2 = Thread(target=serve_order)

t1.start()
print("\n\nOrder placing Start\n\n")
t2.start()
print("\n\nOrder serving Start\n\n")
