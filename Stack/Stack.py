class Stack():
    def __init__(self, max_size=10):
        self.arr = [0] * max_size
        self.head = -1
        self.size = 0

    def push(self, data):
        if self.size+1 == len(self.arr):
            new_arr = [0]*len(self.arr)*2
            for i in range(len(self.arr)):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.head += 1
        self.arr[self.head] = data
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception('Stack is empty')
        removed_item = self.arr[self.head]
        self.head -= 1
        self.size -= 1
        return removed_item