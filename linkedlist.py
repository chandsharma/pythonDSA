class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        if not node:
            print('empty linked list')
            return
        while node:
            print(node.data,'-->',end=' ')
            node = node.next
        print()

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        node = self.head
        if node is None:
            self.insert_at_beginning(data)
            return
        while node.next:
            node = node.next
        new_node = Node(data)
        node.next = new_node

    def remove_from_beginning(self):
        node = self.head
        if not node:
            print('underflow')
            return
        self.head = node.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(34)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(5)
    ll.insert_at_end(334)
    ll.print()
    ll.remove_from_beginning()
    ll.print()