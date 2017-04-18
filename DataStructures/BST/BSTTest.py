import unittest
import inspect
from BST import BST

class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.arr = [10,20,30]
        for item in self.arr:
            self.bst.insert(item)

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_insert(self):
        self.assertEqual(len(self.arr), self.bst.size)
        self.assertEqual(10, self.bst.root.data)
        self.show(self.bst.size)