import unittest
import inspect
from BST import BST


class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.arr = [3,1,2,4,5,0]
        for item in self.arr:
            self.bst.insert(item)

    def show(self, msg=None):
        print(inspect.stack()[1][3], msg)

    def test_insert(self):
        self.assertEqual(len(self.arr), self.bst.size)
        self.show('size=' + str(self.bst.size))

    def test_search(self):
        data = 0
        node, parent = self.bst.search(data)
        self.assertEqual(data, node.data)
        self.assertIsNotNone(parent)
        self.show(str(data) + '==' + str(node.data))

    def test_find_min(self):
        result = self.bst.find_min(self.bst.root)
        self.assertEqual(min(self.arr), result.data)
        self.show(result.data)

    def test_find_max(self):
        result = self.bst.find_max(self.bst.root)
        self.assertEqual(max(self.arr), result.data)
        self.show(result.data)

    def test_in_order(self):
        result = self.bst.in_order()
        self.arr.sort()
        self.assertEqual(self.arr, result)
        self.show(result)

    def test_transplant(self):
        u = self.bst.root
        v, parent = self.bst.search(5)

        self.bst.transplant(u, v)
        self.assertEquals(self.bst.root, v)
        self.show([self.bst.root.data, v.data])

    def test_remove_node_with_no_leaves(self):
        self.bst.remove(0)
        self.arr.sort()
        self.assertEqual(len(self.arr) - 1, self.bst.size)
        self.arr.remove(0)
        self.assertEqual(self.arr, self.bst.in_order())
        self.show(self.bst.in_order)

    def test_remove_node_one_left_leaf(self):
        self.bst.remove(1)
        self.arr.sort()
        self.assertEqual(len(self.arr) - 1, self.bst.size)
        self.arr.remove(1)
        self.assertEqual(self.arr, self.bst.in_order())
        self.show(self.bst.in_order)