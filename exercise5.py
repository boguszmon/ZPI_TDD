__author__ = 'Monika'

class LeastCommonMultipleOfNumbers():
    def __init__(self):
        self.divisible = 1

    # Least common multiple of more than two numbers (any amount of numbers) - is the smallest positive
    # number that is evenly divisible by all of the numbers in a given range.
    # Each iteration of the loop uses the method of least common divisor.
    #
    # max divisor - the last number is in the sequence
    #
    # Examples
    #
    #       for each of the numbers from 1 to 5:
    #           lcm(2, 1) = 2
    #           lcm(3, 2) = 6
    #           lcm(4, 6) = 12
    #           lcm(5, 12) = 60
    #               => 60
    #
    #       for each of the numbers from 1 to 10:
    #               => 2520
    #
    # Returns the smallest positive number that is evenly divisible by all of the numbers in the selected range
    def find_divisible_by_numbers(self, max_divisor):
        for i in range(2, max_divisor + 1):
            self.divisible = self.least_common_multiple(i, self.divisible)
        return self.divisible

    # Least common multiple of two integers - is the smallest positive integer that is divisible by both numbers.
    # It is calculated by the greatest common divisor. Formula: lcm (a, b) = a*b / gcd(a,b)
    #
    # a, b - the numbers of which is calculated least common multiple
    #
    # Example
    #
    #       lcm(4, 6) = 4 * 4 / gcd(4,6) = 12
    #
    # Returns the number of which is least common multiple of two integers.
    def least_common_multiple(self, a, b):
        return int(a * b / self.greatest_common_divisor(a, b))

    # Static method: Greatest common divisor of two integers - is the largest positive
    # integer that divides the numbers without a remainder.
    # Calculations use the Euclidean algorithm, which uses a division algorithm such as long division
    # in combination with the observation that the gcd of two numbers also divides their difference.
    # Formally the algorithm can be described as: gcd(a, b) = gcd (b, a mod b). This operation is performed
    # during each iteration of the loop, as long as b>0.
    #
    # a, b - the numbers of which is calculated greatest common divisor
    #
    # Example
    #
    #       gcd (4, 6) = gcd (6, 4%6)
    #       gcd (6, 4) = gcd (4, 6%4)
    #       gcd (4, 2) = gcd (2, 4%2)
    #       gcd (2, 0)
    #               => 2
    #
    # Returns the number of which is greatest common divisor of two numbers.
    @staticmethod
    def greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a