class Node():
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        newNode = Node(self.head, data, None)
        if self.head.next != None:
            self.head.next.prev  = newNode
            newNode.next = self.head.next
        self.head.next = newNode

    def find(self, data):
        current = self.head.next
        while current is not None and current.data != data:
            current = current.next
        return current

    def remove(self, node):
        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
        else:
            node.prev.next = None