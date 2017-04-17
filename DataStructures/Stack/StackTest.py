import unittest
import inspect
from Stack import Stack

class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_stack_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.show(self.stack.arr)
        self.show("head= " + str(self.stack.head))

        self.assertEqual(self.stack.size, 2)
        self.assertEqual(self.stack.head, 1)

    def test_stack_push_overflow(self):
        arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] * 5
        for i in arr:
            self.stack.push(i)
        self.show(self.stack.arr)
        self.show("head= " + str(self.stack.head))

        self.assertEqual(self.stack.size, len(arr))
        self.assertEqual(self.stack.head, len(arr)-1)

    def test_stack_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.show("head= " + str(self.stack.head))
        self.show("value= " + str(self.stack.arr[self.stack.head]))
        removed_item = self.stack.pop()
        self.show(self.stack.arr)

        self.assertEqual(removed_item, 2)
        self.assertEqual(self.stack.size, 1)

    def test_empty_stack_pop(self):
        with self.assertRaises(Exception):
            self.stack.pop()