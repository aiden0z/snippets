"""
Given an integer, convert it to roman numberal.

Input is guaranteed to be within the range from 1 to 3999.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is 
written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is 
XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral 
for four is not IIII. Instead, the number four is written as IV. Because the one is before the 
five we subtract it making four. The same principle applies to the number nine, which is written 
as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 
1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Refer: https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        ""[summary]
        """
        stack = []

        n = num
        # 最大值为 3999，所以不必对千位数做处理
        if num >= 1000:
            m = num // 1000
            n = num % 1000
            if m > 0:
                stack.append('M' * m)
        
        if n >= 100:
            m = n // 100
            n %= 100
            if m == 9:
                stack.append('CM')
            elif m >= 5 and m <= 8:
                stack.append('D' + (m-5)*'C')
            elif m == 4:
                stack.append('CD')
            else:
                stack.append('C' * m)

        if n >= 10:
            m = n // 10
            n %= 10
            if m == 9:
                stack.append('XC')
            elif m >= 5 and m <= 8:
                stack.append('L' + (m-5)*'X')
            elif m == 4:
                stack.append('XL')
            else:
                stack.append('X' * m)

        if n == 9:
            stack.append('IX')
        elif n >= 5 and n <= 8:
            stack.append('V'+ (n-5)*'I')
        elif n == 4:
            stack.append('IV')
        else:
            stack.append('I'* n)

        return ''.join(stack)


class SolutionB:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[(num%10000)//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]


if __name__ == '__main__':
    cases = [
        (3, 'III'), (4, 'IV'), (9, 'IX'), (58, 'LVIII'), (1994, 'MCMXCIV'), (1776, 'MDCCLXXVI'),
        (2014, 'MMXIV'), (1954, 'MCMLIV')]
    s = Solution()
    sb = SolutionB()

    for case in cases:
        print(s.intToRoman(case[0]), case[0])
        assert s.intToRoman(case[0]) == case[1]
        assert sb.intToRoman(case[0]) == case[1]