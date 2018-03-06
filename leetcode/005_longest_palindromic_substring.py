# -*- coding:utf-8 -*-

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

Refer: https://leetcode.com/problems/longest-palindromic-substring/
"""

def is_palindrome(s):
    """ 判定是否是回文
    """
    length = len(s)
    if length < 2:
        return False
    mid = length >> 1
    l = mid - 1
    r = mid + 1 if length & 1 else mid
    while l >= 0   and r < length:
        if s[l] != s[r]:
            return False
        l -= 1
        r += 1
    return True


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        O(n^3) time
        O(1) space
        """
        length = len(s)

        if length < 2:
            return s

        max_sub = ''
        max_len = 0
        i = 0
        while i < length:
            j = i + 1
            while j <= length:
                if is_palindrome(s[i:j]) and j-i >= max_len:
                    max_len = j - i
                    max_sub = s[i:j]
                j += 1
            i += 1
        return max_sub


class SolutionB(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype :str


        如果一段字符串是回文，那么以某个字符为中心的前缀和后缀都是相同的
        例如以一段回文串“aba”为例，以b为中心，它的前缀和后缀都是相同的，都是a
        我们是否可以可以枚举中心位置，然后再在该位置上用扩展法，
        记录并更新得到的最长的回文长度。长度为奇数和偶数的两种情况。

        O(n^2) time
        O(1) space
        """
        max_len = 1
        start = 0
        length = len(s)

        low = 0
        high = 0

        for i in range(1, length):
            # longest even length
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 >= max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1

            # longest odd length
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 >= max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1
        return s[start:start+max_len]


class SolutionC(object):

    def longestPalindrome(self, s):
        """ Manacher algorithm
        """
        pass


class SolutionD(object):
    """ 最长回文子串长度
    Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest palindromic subsequence of X[0..n-1].

    If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2.
    Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).

    Following is a general recursive solution with all cases handled.

    // Everay single character is a palindrom of length 1
    L(i, i) = 1 for all indexes i in given sequence

    // IF first and last characters are not same
    If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)}

    // If there are only 2 characters and both are same
    Else if (j == i + 1) L(i, j) = 2

    // If there are more than two characters, and first and last
    // characters are same
    Else L(i, j) =  L(i + 1, j - 1) + 2
    """
    def lengthOfLongestSubstring(self, s):
        def lps(s, i, j):
            if i == j:
                return 1
            if s[i] == s[j] and i + 1 == j:
                return 2
            if s[i] == s[j]:
                return lps(s, i+1, j-1) + 2
            return max(lps(s, i, j-1), lps(s, i+1, j))


if __name__ == '__main__':
    assert is_palindrome('bb')
    assert is_palindrome('aba')
    assert is_palindrome('abba')
    assert is_palindrome('abdabadba')

    for solution in (Solution, SolutionB):
        s = solution()
        assert s.longestPalindrome('babad') == 'aba'
        assert s.longestPalindrome('cbbd') == 'bb'
        assert s.longestPalindrome('ab') == 'a'
        assert s.longestPalindrome('a') == 'a'
        assert s.longestPalindrome('aiiiiii') == 'iiiiii'
        assert s.longestPalindrome('aaabbaaa') == 'aaabbaaa'
