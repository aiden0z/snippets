"""Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

Refer https://leetcode.com/problems/longest-common-prefix
"""


class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''

        # 查找最短字符串
        shortest = min(strs, key=lambda x: len(x))
        i, length = 1, len(shortest)
        prefix = ''
        while i <= length:
            if all([item.startswith(shortest[:i]) for item in strs]):
                prefix = shortest[:i]
            else:
                break
            i += 1
        return prefix


class SolutionB:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]  # stop until hit the split index
        return s1


if __name__ == '__main__':
    cases = [(["flower", "flow", "flight"], 'fl'), (["dog", "racecar", "car"], ''), ([], '')]

    s = Solution()
    sb = SolutionB()
    for case in cases:
        print(s.longestCommonPrefix(case[0]), case[1])
        assert s.longestCommonPrefix(case[0]) == case[1]
        assert sb.longestCommonPrefix(case[0]) == case[1]
