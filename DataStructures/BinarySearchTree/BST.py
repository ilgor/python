class Node():
    def __init__(self, parent=None, data=None):
        self.parent = parent
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BST():
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, data):
        self.root = self.insert_helper(self.root, data)
        self.size += 1

    def insert_helper(self, rootNode, data):
        if rootNode == None:
            return Node(data)
        if data < rootNode.data:
            rootNode.left = self.insert_helper(rootNode.left, data)
        else:
            rootNode.right = self.insert_helper(rootNode.right, data)
        return rootNode

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, rootNode, data):
        if rootNode == None or rootNode.data == data:
            return rootNode
        if data < rootNode.data:
            self.search_helper(rootNode.left, data)
        else:
            self.search_helper(rootNode.right, data)

    def remove(self, data):
        node = self.search(data)
        if node.left:
            node.data = node.left.data
            node.left = None
        elif node.right:
            node.data = node.right.data
            node.right = None



    def pre_order(self):
        arr = []
        self.pre_order_helper(self.root, arr)
        return arr

    def pre_order_helper(self, rootNode, arr):
        if rootNode != None:
            arr.append(rootNode.data)  # print(rootNode.data)
            self.pre_order_helper(rootNode.left, arr)
            self.pre_order_helper(rootNode.right, arr)

    def post_order(self):
        arr = []
        self.post_order_helper(self.root, arr)
        return arr

    def post_order_helper(self, rootNode, arr):
        if rootNode != None:
            self.post_order_helper(rootNode.left, arr)
            self.post_order_helper(rootNode.right, arr)
            arr.append(rootNode.data)  # print(rootNode.data)

    def in_order(self):
        arr = []
        self.post_order_helper(self.root, arr)
        return arr

    def in_order_helper(self, rootNode, arr):
        if rootNode != None:
            self.in_order_helper(rootNode.left, arr)
            arr.append(rootNode.data)  # print(rootNode.data)
            self.in_order_helper(rootNode.right, arr)
