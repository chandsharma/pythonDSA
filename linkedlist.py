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

    def size(self):
        node = self.head
        if not node:
            return 0
        size = 1
        while node.next:
            size += 1
            node = node.next
        return size
    
    def remove_from_end(self):
        node = self.head
        if self.size() <= 1:
            self.remove_from_beginning()
            return
        while node.next.next:
            node = node.next
        node.next = None
    
    def inser_in_batch(self,data_list):
        for data in data_list[::-1]:
            self.insert_at_beginning(data)

    def insert_at_index(self,index,data):
        size = self.size()
        if index<0 or index>=size:
            raise Exception('Index out of bound')
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = 0
        current_node = self.head
        while not itr == index-1: 
            current_node = current_node.next
            itr += 1
        node = Node(data)
        node.next = current_node.next
        current_node.next = node

    def remove_from_index(self,index):
        size = self.size()
        if index<0 or index>=size or self.head is None:
            raise Exception('Invalid Index')
        node = self.head
        if index == 0:
            self.remove_from_beginning()
            return
        itr = 0 
        while not itr == index-1:
            node = node.next
            itr += 1
        node.next = node.next.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(34)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(5)
    ll.insert_at_end(334)
    ll.print()
    ll.inser_in_batch([12,334,456,324,213,56,67,])
    ll.print()
    print(ll.size())
    # ll.remove_from_beginning()
    # ll.insert_at_index(10,99)
    # print(ll.size())
    # ll.remove_from_end()
    ll.remove_from_index(5)
    ll.print()