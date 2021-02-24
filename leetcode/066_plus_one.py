""" Plus One
Given a non-empty array of decimal digits representing a non-negative integer, increment
one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

Example 3

    Input: digits = [0]
    Output: [1]

Constraints:
* 1 <= digits.length <= 100
* 0 <= digits[i] <= 9
"""

from typing import List


class Solution:

    def plus_one(self, digits: List[int]) -> List[int]:

        digits = digits[:]
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                digits[i] += 1
                continue
            if digits[i + 1] < 10:
                return digits
            digits[i + 1] -= 10
            digits[i] += 1

        if digits[0] > 9:
            digits[0] -= 10
            digits.insert(0, 1)
        return digits

    def plus_one_2(self, digits: List[int]) -> List[int]:

        n = len(digits)
        digits[n - 1] += 1

        if digits[n - 1] < 10:
            return digits

        carry = 0
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0

        if digits[0] > 9 or carry == 1:
            if digits[0] > 9:
                digits[0] -= 10
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':

    cases = [([4, 3, 2, 1], [4, 3, 2, 2]), ([1, 2, 3], [1, 2, 4]), ([0], [1]), ([9], [1, 0]),
             ([0], [1]), ([9, 8, 9], [9, 9, 0])]

    for case in cases:
        assert Solution().plus_one(case[0]) == case[1]
        assert Solution().plus_one_2(case[0]) == case[1]
