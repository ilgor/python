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

    def search(self, data):
        if data == self.data:
            return self
        if data <= self.data:
            if self.left_child:
                return self.left_child.search(data)
            else:
                return None
        else:
            if self.right_child:
                return self.right_child.search(data)
            else:
                return None

    def remove(self, data):
        node = self.search(data)
        if node:
            if node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            else:
                node = None
            return True
        else:
            return False

    def pre_order(self, rootNode, arr):
        if rootNode != None:
            arr.append(rootNode.data)
            self.pre_order(rootNode.left_child, arr)
            self.pre_order(rootNode.right_child, arr)

    def post_order(self, rootNode, arr):
        if rootNode != None:
            self.post_order(rootNode.left_child, arr)
            self.post_order(rootNode.right_child, arr)
            arr.append(rootNode.data)

    def in_order(self, rootNode, arr):
        if rootNode != None:
            self.in_order(rootNode.left_child, arr)
            arr.append(rootNode.data)
            self.in_order(rootNode.right_child, arr)

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

    def search(self, data):
        if self.root == None:
            return None
        return self.root.search(data)

    def remove(self, data):
        if self.root.remove(data):
            self.size -= 1

    def in_order(self):
        arr = []
        self.root.in_order(self.root, arr)
        return arr

    def pre_order(self):
        arr = []
        self.root.pre_order(self.root, arr)
        return arr

    def post_order(self):
        arr = []
        self.root.post_order(self.root, arr)
        return arr