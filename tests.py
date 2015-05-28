__author__ = 'Monika'

import unittest

from exercise5 import LeastCommonMultipleOfNumbers

class TestLeastCommonMultipleOfNumbers(unittest.TestCase):

    def setUp(self):
        self.result_lcm = LeastCommonMultipleOfNumbers()

    def testLeastCommonMultipleHasInitialDivisible(self):
        assert self.result_lcm.divisible is not None, "result_lcm divisible is None"

    def testGreatestCommonDivisor(self):
        assert self.result_lcm.greatest_common_divisor(4, 6) == 2, "result_lcm is not correct"

    def testLeastCommonMultiple(self):
        assert self.result_lcm.least_common_multiple(4, 6) == 12, "result_lcm is not correct"

    def testFindDivisibleByIntegers(self):
        assert self.result_lcm.find_divisible_by_numbers(10) == 2520, "result_lcm is not correct"


if __name__ == "__main__":
    unittest.main()