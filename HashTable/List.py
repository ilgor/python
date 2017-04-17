class Node():
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class List():
    def __init__(self):
        self.head = Node()
        self.size = 0

    def add(self, key, value):
        new_node = Node(key, value)

        if self.head.next == None:
            self.head.next = new_node
        else:
            next_node = self.head.next
            self.head.next = new_node
            new_node.next = next_node
        self.size += 1

    def find_both(self, key):
        prev = self.head
        current = prev.next
        while current != None and current.key != key:
            prev = current
            current = current.next
        return prev, current

    def find(self, key):
        prev, current = self.find_both(key)
        return current

    def remove(self, key):
        prev, current = self.find_both(key)
        if current == None:
            raise Exception('Given value is not in the list')
        prev.next = current.next
        self.size -= 1
