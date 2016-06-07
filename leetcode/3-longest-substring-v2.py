# coding:utf-8

"""
Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the
answer must be a substring, "pwke" is a subsequence and not a substring.

"""

import time


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """ 非递归版本
        :type s: str
        :rtype: int
        """
        self.result = 0
        self.sub = ""

        while len(s) > self.result:
            sub = ''
            indexes = dict()
            i = -1
            for c in s:
                i += 1
                if c in sub:
                    sub = ''
                    s = s[indexes[c] + 1:]
                    break
                else:
                    sub += c
                    l = len(sub)
                    if l > self.result:
                        self.sub = sub
                        self.result = l
                    indexes[c] = i

        return self.result


if __name__ == '__main__':
    input = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
    start = time.time()
    s = Solution()
    result = s.lengthOfLongestSubstring(input)
    print(time.time() - start, result)
