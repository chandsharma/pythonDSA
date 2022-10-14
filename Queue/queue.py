#python implementation of queue

from collections import deque

class Queue():
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self,data):
        self.queue.appendleft(data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
