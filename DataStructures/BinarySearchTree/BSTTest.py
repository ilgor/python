import unittest
import inspect
from BST import BST


class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def show(self, msg=None):
        print(inspect.stack()[1][3], msg)

    def test_insert_root(self):
        self.bst.insert(10)
        self.assertEqual(1, self.bst.size)
        self.assertEqual(10, self.bst.root.data)
        self.show([('size', self.bst.size), ('root value', self.bst.root.data)])

    def test_insert_left(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.assertEqual(2, self.bst.size)
        self.assertEqual(10, self.bst.root.data)
        self.assertEqual(5, self.bst.root.left.data)
        self.show([('size', self.bst.size), ('root value', self.bst.root.data), ('left child', self.bst.root.left.data)])

    def test_insert_right(self):
        self.bst.insert(10)
        self.bst.insert(19)
        self.assertEqual(2, self.bst.size)
        self.assertEqual(10, self.bst.root.data)
        self.assertEqual(19, self.bst.root.right.data)
        self.show([('size', self.bst.size), ('root value', self.bst.root.data), ('right child', self.bst.root.right.data)])

    def test_search_existing_item(self):
        self.populate()
        node = self.bst.search(6)
        self.show(self.bst.in_order())
        self.assertIsNotNone(node)
        self.assertEqual(6, node.data)
        # self.show('Found!')

    def test_search_none_existing_item(self):
        self.populate()
        node = self.bst.search(100)
        self.assertIsNone(node)
        self.show('Not Found!')

    def test_remove_existing_item(self):
        self.populate()
        size = self.bst.size
        expected_size = size - 1
        self.bst.remove(5)
        result = self.bst.search(5)
        self.assertIsNotNone(result)
        self.assertEqual(expected_size, size)

    def test_remove_none_existing_item(self):
        self.populate()
        with self.assertRaises(Exception):
            self.bst.remove(5)

    def test_pre_order(self):
        self.populate()
        result = self.bst.pre_order()
        self.show(result)

    def test_post_order(self):
        self.populate()
        result = self.bst.post_order()
        self.show(result)

    def test_in_order(self):
        self.populate()
        result = self.bst.in_order()
        self.show(result)

    def populate(self):
        for i in [10,5,19,1,6,17]:
            self.bst.insert(i)
