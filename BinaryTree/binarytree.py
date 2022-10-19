#binary tree implementation in python

class BinaryTree():
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self,data):
        if data == self.data:
            return
        if data < self.data:
            if not self.left:
                self.left = BinaryTree(data)
            else:
                self.left.add_node(data)
        if data > self.data:
            if not self.right:
                self.right = BinaryTree(data)
            else:
                self.right.add_node(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self,data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def min(self):
        if self.left:
            return self.left.min()
        return self.data

    def max(self):
        if self.right:
            return self.right.max()
        return self.data

    def sum(self):
        sum = self.data
        if self.left:
            sum += self.left.sum()
        if self.right:
            sum += self.right.sum()
        return sum

    def delete(self,data):
        if data == self.data:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                min_val = self.right.min()
                self.data = min_val
                self.right = self.right.delete(min_val)
                return self

        elif data < self.data and self.left:
            self.left = self.left.delete(data)
        elif data > self.data and self.right:
            self.right = self.right.delete(data)

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

def build_binary_tree(list_of_elements):
    root = BinaryTree(list_of_elements[0])
    for element in list_of_elements[1:]:
        root.add_node(element)
    return root

if __name__ == "__main__":
    binary_tree = build_binary_tree([17,4,1,20,9,23,18,34])
    binary_tree.delete(20)
    print(binary_tree.in_order_traversal())
    print(binary_tree.post_order_traversal())
    print(binary_tree.pre_order_traversal())
    print(binary_tree.search(19))
    print(binary_tree.min())
    print(binary_tree.max())
    print(binary_tree.sum())

    binary_tree = build_binary_tree(["India","Pakistan","Germany","USA","China","India","UK"])
    print(binary_tree.in_order_traversal())
    print(binary_tree.search("Germany"))
    print(binary_tree.search("Nepal"))
    print(binary_tree.sum())
