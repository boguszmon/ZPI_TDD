__author__ = 'Monika'

import unittest

from exercise5 import LeastCommonMultipleOfNumbers

class TestLeastCommonMultipleOfNumbers(unittest.TestCase):

    def testLeastCommonMultiple(self):
        result_lcm = LeastCommonMultipleOfNumbers()


if __name__ == "__main__":
    unittest.main()