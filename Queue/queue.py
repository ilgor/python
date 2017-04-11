class Queue():
    def __init__(self, max_size):
        self.count = 0
        self.head = 0
        self.tail = -1
        self.arr = [0] * max_size

    def enqueue(self, val):
        if self.count == len(self.arr):
            raise Exception('Queue is full')

        self.tail += 1
        if self.tail == len(self.arr):
            self.tail = 0
        self.arr[self.tail] = val
        self.count += 1

    def enqueList(self, l):
        for item in l:
            self.enqueue(item)

    def dequeue(self):
        if self.count == 0:
            raise Exception('Queue is Empty')
        item = self.arr[self.head]
        self.head += 1
        if self.head == len(self.arr):
            self.head = 0
        self.count -= 1
        return item