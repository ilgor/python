import unittest

from Knapsack import Knapsack


class KnapsackTest(unittest.TestCase):

    def setUp(self):
        self.knapsack = Knapsack()
        self.items = (
             ('clock', 175, 10),
             ('painting', 90, 9),
             ('radio', 20, 4),
             ('vase', 50, 2),
             ('book', 10, 1),
             ('computer', 200, 20)
        )

    def test_chooseBest(self):
        expected = (275, (('book', 10, 1), ('painting', 90, 9), ('clock', 175, 10)))
        actual = self.knapsack.calculate(items=self.items, max_weight=20)
        self.assertEqual(expected, actual)