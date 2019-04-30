"""Implement strStr()

Imporment strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of
haystack.

Example 1:

    Input: haystack = "hello", needle = "ll
    Ouput: 2

Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Clarification:

What should we return when needle is an empty string? This is a greate question to ask during an
interview.

For the purpose of this problem, we will return 0 when dle is an empty string. This is consistent
to C's strStr() and Java's indexOf().

Reference https://leetcode.com/problems/implement-strstr/
"""


class Solution:

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        if len(haystack) == 0:
            return -1

        i, n = 0, len(haystack)
        while i < n:
            if i + len(needle) > n:
                return -1

            if haystack[i] != needle[0]:
                i += 1
                continue

            found = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False
                    break

            if not found:
                i += 1
                continue
            else:
                return i
        return -1


if __name__ == '__main__':
    cases = [
        ('hello', 'h', 0),
        ('hello', 'ell', 1),
        ('hello', 'll', 2),
        ('aaaaa', 'bba', -1),
        ('', 'a', -1),
        ('aa', '', 0),
    ]

    solutions = [Solution]
    for case in cases:
        for s in solutions:
            print(case, s().strStr(case[0], case[1]))
            assert s().strStr(case[0], case[1]) == case[2]
