class Node():
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def inser_at_beginning(self,data):
        head = self.head
        if not head:
            node = Node(data)
            self.head,self.tail = node,node
            return
        node = Node(data,None,head)
        head.prev = node
        self.head = node

    def print_forward(self):
        node = self.head
        while node:
            print(node.data,'-->',end=' ')
            node = node.next
        print()

    def print_backward(self):
        node = self.tail
        while node:
            print(node.data,'<--',end=' ')
            node = node.prev
        print()

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.inser_at_beginning(42)
    dll.inser_at_beginning(2553)
    dll.inser_at_beginning(263)
    dll.inser_at_beginning(215)
    dll.inser_at_beginning(225)
    dll.inser_at_beginning(245)
    dll.inser_at_beginning(244)
    dll.print_forward()
    dll.print_backward()