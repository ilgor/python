class Node():
    def __init__(self, data=None, parent=None):
        self.parent = parent
        self.data = data
        self.left_child = None
        self.right_child = None


class BST():
    def __init__(self):
        self.size = 0
        self.root = None

    def search(self, data):
        parent = None
        current = self.root
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left_child
            else:
                current = current.right_child
        return current, parent

    def insert(self, data):
        parent = None
        current = self.root
        while current:
            parent = current
            if data < current.data:
                current = current.left_child
            else:
                current = current.right_child
        new_node = Node(data, parent)
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left_child = new_node
        else:
            parent.right_child = new_node
        self.size += 1

    def find_min(self, node):
        parent = None
        current = node
        while current:
            parent = current
            current = current.left_child
        return parent

    def find_max(self, node):
        parent = None
        current = node
        while current:
            parent = current
            current = current.right_child
        return parent

    def in_order(self):
        arr = []
        return self.in_order_helper(self.root, arr)

    def in_order_helper(self, node, arr):
        if node:
            self.in_order_helper(node.left_child, arr)
            arr.append(node.data)
            self.in_order_helper(node.right_child, arr)
        return arr

    def remove(self, data):
        current, parent = self.search(data)
        if current is None:
            raise Exception(str(data)+' doesnt exit')
        if current.left_child is None and current.right_child is None:
            if parent.left_child and parent.left_child.data == data:
                parent.left_child = None
            else:
                parent.right_child = None
        elif current.left_child and current.right_child is None:
            parent.left_child = current.left_child
            current = None

        self.size -= 1