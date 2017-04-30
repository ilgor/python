class Node():
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None


class RBT():
    def __init__(self):
        self.size = 0
        self.root = None

