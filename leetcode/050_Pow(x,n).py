"""Pow(x, n)
Implement pow(x,n), which calculates x raised to the the power n (x^n).

Example 1:

    Input: 2.00000, 10
    Output: 1024.00000

Example 2:

    Input: 2.10000, 3
    Output: 9.26100

Example 3:

    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25


Note:
    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [-2^31, 2^31 - 1]
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1 / x, -n)
        return x**n


if __name__ == '__main__':
    cases = [
        ((2.00000, 10), 1024.00000),
        ((2.10000, 3), 9.261000),
        ((2.00000, -2), 0.25000)
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().myPow(*case[0]) == case[1]
