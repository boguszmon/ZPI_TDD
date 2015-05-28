__author__ = 'Monika'

class LeastCommonMultipleOfNumbers():
    def __init__(self):
        self.divisible = 1

    @staticmethod
    def greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a