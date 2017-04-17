from List import List


class HashTable():
    def __init__(self, table_size):
        self.slots = [ List() for _ in range(table_size) ]
        self.table_size = table_size

    def hash(self, key):
        sum = 0
        for i in range(1, len(key)+1):
            sum += ord(key[i-1]) * i
        return sum % self.table_size

    def put(self, key, value):
        hash_value = self.hash(key)
        if self.slots[hash_value].find(key):
            raise Exception('Key already exists')
        self.slots[hash_value].add(key, value)

    def update(self, key, value):
        hash_value = self.hash(key)
        self.slots[hash_value].find(key).value = value

    def remove(self, key):
        hash_value = self.hash(key)
        slot = self.slots[hash_value]
        slot.remove(key)
        
    def show(self):
        arr = []
        for slot in self.slots:
            current = None
            if slot != None:
                current = slot.head.next
            while current != None:
                arr.append((current.key, current.value))
                current = current.next
        print(arr)
        return arr