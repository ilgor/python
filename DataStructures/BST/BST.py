class Node():
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def insert(self, data):
        if data <= self.data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)



class BST():
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
        self.size += 1





