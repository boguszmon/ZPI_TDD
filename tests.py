__author__ = 'Monika'

import unittest

from exercise5 import LeastCommonMultipleOfNumbers

class TestLeastCommonMultipleOfNumbers(unittest.TestCase):

    def testLeastCommonMultiple(self):
        result_lcm = LeastCommonMultipleOfNumbers()

    def testLeastCommonMultipleHasInitialDivisible(self):
        result_lcm = LeastCommonMultipleOfNumbers()
        assert result_lcm.divisible is not None, "result_lcm divisible is None"


if __name__ == "__main__":
    unittest.main()