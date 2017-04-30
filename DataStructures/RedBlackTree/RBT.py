class Color():
    BLACK = 1
    RED = 2


class Node():
    def __init__(self, data=None, parent=None, color=Color.BLACK):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color


class RBT():
    def __init__(self):
        self.size = 0
        self.root = None

