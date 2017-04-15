class Node():
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node()
        self.head.prev = self.head.next = self.head

    def insert(self, data):
        new_node = Node(self.head, data, None)
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node

    def find(self, data):
        current = self.head.next
        while current != self.head and current.data != data:
            current = current.next
        return current

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeAll(self):
        current = self.head.next
        while current != self.head:
            self.remove(current)
            current = current.next

    def reverse(self):
        current = self.head.next
        prevNode = current.prev
        while current != self.head:
            nextNode = current.next
            current.next = prevNode
            current.prev = nextNode
            prevNode = current
            current = nextNode
        self.head.prev = self.head.next
        self.head.next = prevNode

