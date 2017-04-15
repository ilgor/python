import unittest
import inspect
from Queue import Queue

class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(5)

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.show(self.queue.arr)
        self.assertEqual(self.queue.count, 1)


    def test_enqueList(self):
        arr = [1,2,3,4,5]
        self.queue.enqueList(arr)
        self.show(self.queue.arr)
        self.assertEqual(self.queue.count, 5)

    def test_deque(self):
        self.queue.enqueue(1)
        poped = self.queue.dequeue()
        self.show(poped)
        self.assertEqual(self.queue.count, 0)
        self.assertEqual(poped, 1)

    def test_deque_empty_queue(self):
        with self.assertRaises(Exception):
            self.queue.dequeue()
