"""Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.

Refer https://leetcode.com/problems/palindrome-number/description/
"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverse = 0
        xx = x
        while xx != 0:
            t = xx % 10
            reverse = reverse * 10 + t
            xx = xx // 10
        if reverse == x or reverse == 0:
            return True
        else:
            return False


class SolutionB(object):

    def isPalindrome(self, x):
        x_str = str(x)
        return False if x_str[0] == '-' else x_str == x_str[::-1]


if __name__ == '__main__':
    cases = [(0, True), (12, False), (121, True), (11, True), (-1, False)]
    s = Solution()
    sb = SolutionB()
    for case in cases:
        assert s.isPalindrome(case[0]) == case[1]
        assert sb.isPalindrome(case[0]) == case[1]
