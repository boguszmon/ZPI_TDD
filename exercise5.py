__author__ = 'Monika'

class LeastCommonMultipleOfNumbers():
    def __init__(self):
        self.divisible = 1

    @staticmethod
    def greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    def least_common_multiple(self, a, b):
        return int(a * b / self.greatest_common_divisor(a, b))

    def find_divisible_by_numbers(self, max_divisor):
        for i in range(2, max_divisor + 1):
            self.divisible = self.least_common_multiple(i, self.divisible)
        return self.divisible