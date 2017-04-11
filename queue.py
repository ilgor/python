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
        print item

    def show(self):
        print(self.arr)


try:
    queue = Queue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
except Exception as e:
    print e
queue.show()

try:
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
except Exception as e:
    print e
try:
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
except Exception as e:
    print e

queue.show()

try:
    queue.dequeue()
    queue.enqueue(11)
    queue.dequeue()
    queue.enqueue(12)
    queue.dequeue()
    queue.enqueue(13)
    queue.dequeue()
    queue.enqueue(14)
    queue.dequeue()
    queue.enqueue(15)
except Exception as e:
    print e
queue.show()
