"""Divide Two Integers

Given two integers dividend and dvisor, divide two integer without using multiplication,
dvision and mod perator.

Return the quotient after dividing dividend by dvisor.

The integer division should truncate toward zero.

Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3

Example 2:

    Input: divident = 7, divisor = -3
    Output: -2

Note:
    * Both divident and divisor will be 32-bit signed integers.
    * The divisor will never be 0.
    * Assume we are dealing with the environment which could only sotre integers with 32-bit
      singed integers range: [-2**31, 2**31-1]. For the purpose of this problem, assume that
      you function returns 2**31 -1 when the division result overflows.

Reference https://leetcode.com/problems/divide-two-integers/

"""


class Solution:
    """每次2倍增长"""

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend

        if divisor == -1:
            result = -dividend
            if result >= 2**31 - 1:
                return 2**31 - 1
            else:
                return result
        if dividend < 0:
            a = -dividend
        else:
            a = dividend

        if divisor < 0:
            b = -divisor
        else:
            b = divisor

        def divide(a, b):
            if a < b:
                return 0
            x = b
            result = 1

            while a >= (x << 1):
                x <<= 1
                result <<= 1

            return divide(a - x, b) + result

        result = divide(a, b)

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return result
        else:
            return -result


class SolutionBasedSubtraction:

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend

        if divisor == -1:
            result = -dividend
            if result >= 2**31 - 1:
                return 2**31 - 1
            else:
                return result

        if dividend < 0:
            a = -dividend
        else:
            a = dividend

        if divisor < 0:
            b = -divisor
        else:
            b = divisor

        result = 0
        while a >= b:
            a -= b
            result += 1

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return result
        else:
            return -result


if __name__ == '__main__':
    cases = [(10, 3, 3), (7, -3, -2), (-2147483648, -1, 2147483647), (2147483647, 2, 1073741823)]

    solutions = [Solution]

    for case in cases:
        for s in solutions:
            result = s().divide(case[0], case[1])
            print(case, result)
            assert case[2] == result
