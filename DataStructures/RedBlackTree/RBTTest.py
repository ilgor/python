import unittest
import inspect
from RBT import RBT

class RBTTest(unittest.TestCase):
    def setUp(self):
        self.rbt = RBT()

    def show(self, msg=None):
        print(inspect.stack()[1][3], msg)

    def test_method(self):
        self.show('size should be zero == ' + str(self.rbt.size))