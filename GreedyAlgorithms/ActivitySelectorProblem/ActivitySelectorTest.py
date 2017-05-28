import inspect
import unittest

from GreedyAlgorithms.ActivitySelectorProblem.ActivitySelector import ActivitySelector


class ActivitySelectorTest(unittest.TestCase):
    def setUp(self):
        self.activity_selector = ActivitySelector()
        self.activities = {
            'A1' : (0, 6),
            'A2' : (3, 4),
            'A3' : (1, 2),
            'A4' : (5, 9),
            'A5' : (5, 7),
            'A6' : (8 ,9)
        }

    def show(self, msg=None):
        print(inspect.stack()[1][3], msg)

    def test_sort(self):
        expected = ['A3','A2','A1','A5','A4','A6']
        actual_activities, actual_times = self.activity_selector.sort(self.activities)
        self.assertEqual(expected, actual_activities)
        self.show(actual_activities)


    def test_show_activities(self):
        expected = ['A3', 'A2', 'A5', 'A6']
        actual = self.activity_selector.show_activities(self.activities)
        self.assertEqual(expected, actual.keys())
        self.show(actual)

