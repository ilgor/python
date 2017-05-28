import inspect
import unittest

from DynamicProgramming.LCS.LCS import LCS


class LCSTest(unittest.TestCase):
    def setUp(self):
        self.lcs = LCS()
        self.X = "ABCBDAB"
        self.Y = "BDCABA"

    def show(self, msg):
        print(inspect.stack()[1][3], msg)

    def test_length(self):
        expected = 4
        actual = self.lcs.length(self.X, self.Y)
        self.assertEqual(expected, actual)
        self.show(actual)

    def test_print(self):
        expected = "BCBA"
        actual = self.lcs.word(self.X, self.Y)
        self.assertEqual(expected, self.lcs.lcs)
        self.show(actual)
