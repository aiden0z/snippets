# -*- coding:utf-8 -*-

"""
Reverse digits of an iteger.
Example1: x = 123, return 321
Example1: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.

Refer: https://leetcode.com/problems/reverse-integer/
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        upper = 2**31 -1
        lower = - 2**31

        if x > upper or x < lower:
            return 0
        string = '%s' % x
        if x < 0:
            result = int('-' + string[1:][::-1])
        else:
            result =  int(string[::-1])
        if result < lower or result > upper:
            return 0
        return result

class SolutionB(object):
    def reverse(self, x):
        rev = 0
        xx = abs(x)
        while xx != 0:
            t = xx % 10
            rev = rev * 10 + t
            xx = xx // 10
        if x < 0:
            result = -1 * rev
        else:
            result = rev
        if result < -2 ** 31 or result > 2 ** 31 -1:
            return 0
        else:
            return result


if __name__ == '__main__':
    s = Solution()
    assert s.reverse(19223372036854775807) == 0
    assert s.reverse(2**31) == 0
    assert s.reverse(-1-2**31) == 0
    assert s.reverse(0) == 0
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321

    sb = SolutionB()
    assert sb.reverse(19223372036854775807) == 0
    assert sb.reverse(2**31) == 0
    assert sb.reverse(-1-2**31) == 0
    assert sb.reverse(0) == 0
    assert sb.reverse(123) == 321
    assert sb.reverse(-123) == -321
