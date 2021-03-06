class Color():
    BLACK = 1
    RED = 2


class Node():
    def __init__(self, data=None, parent=None, color=Color.RED):
        self.data = data
        self.parent = parent
        self.color = color
        self.left = self.right = None


class RBT():
    def __init__(self):
        self.NIL = Node(None, None, Color.BLACK)
        self.root = self.NIL
        self.size = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, data):
        parent = self.NIL
        current = self.root
        while current != self.NIL:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        new_node = Node(data, parent)
        if parent == self.NIL:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.left = self.NIL
        new_node.right = self.NIL
        self.insert_fix_up(new_node)

    def insert_fix_up(self, new_node):
        while new_node.parent.color == Color.RED:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.color == Color.RED:
                    new_node.parent.color = uncle.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                elif new_node == new_node.parent.right:
                    new_node = new_node.parent
                    self.left_rotate(new_node)
                new_node.parent.color = Color.BLACK
                new_node.parent.parent.color = Color.RED
                self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.color == Color.RED:
                    new_node.parent.color = uncle.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.left_rotate(new_node.parent.parent)
        self.root.color = Color.BLACK

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, node):
        temp_node = node
        temp_node_original_color = temp_node.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            temp_node = self.minimum(node.right)
            temp_node_original_color = temp_node.color
            x = temp_node.right
            if temp_node.parent == node:
                x.parent = temp_node
            else:
                self.transplant(node, temp_node)
                temp_node.right = node.right
                temp_node.right.parent = temp_node
            self.transplant(node, temp_node)
            temp_node.left = node.left
            temp_node.left.parent = temp_node
            temp_node.color = node.color
        if temp_node_original_color == Color.BLACK:
            self.delete_fix_up(x)

    def minimum(self, node):
        current = node
        while current.left != self.NIL:
            current = current.left
        return current

    def delete_fix_up(self, x):
        pass