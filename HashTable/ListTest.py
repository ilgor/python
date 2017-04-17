import unittest
import inspect
from List import List

class ListTest(unittest.TestCase):
    def show(self, msg=None):
        arr = []
        current = self.list.head.next
        while current != None:
            arr.append(current.key)
            current = current.next

        print(inspect.stack()[1][3], msg, arr)

    def setUp(self):
        self.list = List()

    def test_add(self):
        self.list.add(1, 'One')
        self.list.add(2, 'Two')
        self.assertEqual(2, self.list.size)
        self.show()

    def test_find_existing_data(self):
        self.list.add(1, 'One')
        self.list.add(2, 'Two')
        current = self.list.find(1)
        self.assertIsNotNone(current)
        self.show(current)

    def test_find_none_existing_data(self):
        self.list.add(1, 'One')
        self.list.add(2, 'Two')
        current = self.list.find(3)
        self.assertIsNone(current)
        self.show(current)

    def test_remove_existing_data(self):
        self.list.add(1, 'One')
        self.list.add(2, 'Two')
        self.list.remove(1)
        self.assertEqual(1, self.list.size)
        self.show()

    def test_remove_none_existing_data(self):
        self.list.add(1, 'One')
        self.list.add(2, 'Two')
        with self.assertRaises(Exception):
            self.list.remove(3)
        self.assertEqual(2, self.list.size)
        self.show('Exception raised')