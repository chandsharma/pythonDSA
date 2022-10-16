class Tree():
    def __init__(self,name,designation,parent=None):
        self.parent = parent
        self.children = []
        self.name = name
        self.designation = designation

    def add_child(self,name,designation):
        child = Tree(name,designation,self)
        self.children.append(child)
        return child

    def print_tree(self,criteria, level,current_level=0,indentation=0):
        if criteria == "both":
            to_print = self.name+" ({}) ".format(self.designation)
        elif criteria == "designation":
            to_print = self.designation
        else:
            to_print = self.name
        print(" "*indentation*2,to_print)
        if level == current_level:
            return
        for child in self.children:
            child.print_tree(criteria,level,current_level+1,indentation+2)


def build_management_tree():
    ceo = Tree("Nipul", "CEO")
    cto = ceo.add_child("Chinmay","CTO")
    hrh = ceo.add_child("Gels","HR Head")

    ih = cto.add_child("Viswa","Infrastructure Head")
    ah = cto.add_child("Aamir","Application Head")
    ih.add_child("Dhaval","Cloud Manager")
    ih.add_child("Abhijit","App Manager")

    hrh.add_child("Peter","Recruitment Manager")
    hrh.add_child("Waqas","Policy HManageread")

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name",1)
    print("\n\n")
    root_node.print_tree("designation",2)
    print("\n\n")
    root_node.print_tree("both",0)