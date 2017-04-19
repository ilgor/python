import unittest
import inspect
from random import random

from BST import BST

class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.arr = [30,20,30,5,6]
        for item in self.arr:
            self.bst.insert(item)

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_insert(self):
        self.assertEqual(len(self.arr), self.bst.size)
        self.assertEqual(self.arr[0], self.bst.root.data)
        self.show(self.bst.size)

    def test_search(self):
        for item in [10,20,30,5,6,7,11,13,19]:
            if self.bst.search(item):
                self.assertIsNotNone(self.bst.search(item))
                self.show(str(item) + ' exists')
            else:
                self.assertIsNone(self.bst.search(item))
                self.show(str(item) + ' does not exist')

    def test_remove(self):
        size = self.bst.size
        self.assertTrue(self.bst.remove(5))
        self.assertEqual(size-1, self.bst.size)


    def test_pre_order(self):
        result = self.bst.pre_order()
        self.show(result)

    def test_post_order(self):
        result = self.bst.post_order()
        self.show(result)

    def test_in_order(self):
        result = self.bst.in_order()
        self.show(result)