"""
Given an integer, convert it to roman numberal.

Input is guaranteed to be within the range from 1 to 3999.


罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。

按照下面的规则可以表示任意正整数:

重复数次：一个罗马数字重复几次，就表示这个数的几倍。

右加左减：在一个较大的罗马数字的右边记上一个较小的罗马数字，表示大数字加小数字。
在一个较大的数字的左边记上一个较小的罗马数字，表示大数字减小数字。
但是，左减不能跨越一个位数。比如，99不可以用IC表示，而是用XCIX表示。
此外，左减数字不能超过一位，比如8写成VIII，而非IIX。
同理，右加数字不能超过三位，比如十四写成XIV，而非XIIII。


Refer: https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        pass



if '__name__' == '__main__':
    pass
