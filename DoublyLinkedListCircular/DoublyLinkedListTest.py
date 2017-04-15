import unittest
import inspect
from DoublyLinkedList  import LinkedList


class DoublyLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.linkedList = LinkedList()
        arr = [1, 2, 3, 4]
        for item in arr:
            self.linkedList.insert(item)

    def size(self):
        current = self.linkedList.head.next
        count = 0
        arr = []
        while current != self.linkedList.head:
            count += 1
            arr.append(current.data)
            current = current.next
        print(inspect.stack()[1][3], arr)
        return count

    def test_insert(self):
        self.assertEqual(self.size(), 4)

    def test_find(self):
        result = self.linkedList.find(2)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 2)

    def test_remove_middle_element(self):
        node = self.linkedList.find(2)
        self.linkedList.remove(node)
        self.assertEqual(self.size(), 3)

    def test_remove_first_element(self):
        node = self.linkedList.find(4)
        self.linkedList.remove(node)
        self.assertEqual(self.size(), 3)

    def test_remove_last_element(self):
        node = self.linkedList.find(1)
        self.linkedList.remove(node)
        self.assertEqual(self.size(), 3)

    def test_remove_all_element(self):
        self.linkedList.removeAll()
        self.assertEqual(self.size(), 0)

    def test_reverse(self):
        self.linkedList.reverse()
        self.size()
        self.assertEqual(self.linkedList.head.next.data, 1)
        self.assertEqual(self.linkedList.head.prev.data, 4)
