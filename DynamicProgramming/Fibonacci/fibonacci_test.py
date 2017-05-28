import unittest
import inspect

from fibonacci import Fibonacci

class fibonacci_test(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_method(self):
        self.show("test method")

    def test_get_nth_fibonacci_number_shouldRaiseException(self):
        n = -1
        with self.assertRaises(Exception):
            self.fib.get_nth_fibonacci_number(n)
        self.show("Exception raised")

    def get_nth_fibonacci_number(self):
        n = 5
        expected = 3
        actual  = self.fib.get_nth_fibonacci_number(n)
        self.show(actual)
        self.assertEqual(expected, actual)

    def test_generate_fibonacci_sequence_for(self):
        n = 5
        expected = [0,1,1,2,3]
        actual = self.fib.generate_fibonacci_sequence_for(n)
        self.show(expected)
        self.assertEqual(expected, actual)

    def test_big_seq(self):
        n = 500000
        actual = self.fib.generate_fibonacci_sequence_for(n)
        self.show(actual[n-1])

        