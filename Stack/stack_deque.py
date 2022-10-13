#implementation of STACK using python collections.deque

from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    stack = Stack()
    stack.push('first')
    stack.push('second')
    stack.push('third')
    stack.push('fourth')
    stack.push('last')
    print(stack.stack)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.stack)