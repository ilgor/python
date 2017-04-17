import unittest
import inspect
from DoublyLinkedList import LinkedList


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()
        arr = [1, 2, 3, 4]
        for item in arr:
            self.linkedList.insert(item)

    def test_insert(self):
        self.assertEqual(self.size(), 4)

    def test_find(self):
        result = self.linkedList.find(2)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 2)

    def test_remove_middle_node(self):
        node = self.linkedList.find(3)
        self.linkedList.remove(node)
        self.assertEqual(self.size(), 3)

    def test_remove_first_node(self):
        node = self.linkedList.find(4)
        self.linkedList.remove(node)
        self.assertEqual(self.size(), 3)

    def test_remove_last_node(self):
        node = self.linkedList.find(1)
        self.linkedList.remove(node)
        self.assertEqual(self.size(), 3)

    def size(self):
        current = self.linkedList.head.next
        count = 0
        arr = []
        while current != None:
            count += 1
            arr.append(current.data)
            current = current.next
        print(inspect.stack()[1][3] ,arr)
        return count