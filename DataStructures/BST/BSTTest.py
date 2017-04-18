import unittest
import inspect
from .BST import BST

class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_insert(self, data):
        self.bst.insert(data)
        self.assertEqual(1, self.bst.size)