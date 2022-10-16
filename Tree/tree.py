#implementation of tree structure in python 

class Tree():
    def __init__(self,data,parent=None):
        self.parent = parent
        self.children = []
        self.data = data

    def add_child(self,data):
        child = Tree(data,self)
        self.children.append(child)
        return child

    def print(self,indent=0):
        print(" "*indent*2,self.data)
        for child in self.children:
            child.print(indent+2)

def populate_tree():
    root = Tree("Electronics")
    
    tv = root.add_child("TV")
    phone = root.add_child("Phone")
    ac = root.add_child("AC")

    phone.add_child("Pixel")
    phone.add_child("Mi")
    phone.add_child("iPhone")

    tv.add_child("Samsung")
    tv.add_child("T-Series")
    tv.add_child("DoorDarshan")

    ac.add_child("Voltas")
    ac.add_child("Whirlpool")
    ac.add_child("Blue Star")

    return root

if __name__ == "__main__":
    tree = populate_tree()
    tree.print()