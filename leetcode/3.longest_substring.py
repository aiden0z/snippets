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
        """递归版本
        :type s: str
        :rtype: int
        """
        self.result = 0
        self.sub = ""

        def search(s):
            if len(s) <= self.result:
                return
            sub = ""
            indexes = dict()
            i = -1
            for c in s:
                i += 1
                if c in sub:
                    search(s[indexes[c] + 1:])
                    sub = ""
                else:
                    sub += c
                    l = len(sub)
                    if l > self.result:
                        self.sub = sub
                        self.result = l
                    indexes[c] = i
        search(s)
        return self.result

class SolutionB(object):
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


class SolutionC(object):
    def lengthOfLongestSubstring(self, s):
        """ 动态规划版本
        :type s: str
        :rtype: int

        Analysis:

        dp[i]:     表示到当前下标 i 为止，最长的不重复子串的长度；
        before:    表示下标为 i 的当前元素上一次重复出现的下标；
        lastIndex: 表示上一个最长不重复子串的开始位置；

        那么 dp[i] 的长度可以归结为以下公式：

                > dp[i-1] +1 (before < lastIndex)
        dp[i] = |
                > i - before (before >= lastIndex)

        """
        if len(s) == 0:
            return 0
        last_index = 0
        indexes = {s[0]: 0}
        crt_len = 1
        max_len = 1
        for i in range(1, len(s)):
            c = s[i]
            # 如果字符 c 已经出现过
            if c in indexes:
                # 判断上一个最长子串开始位置
                if last_index > indexes[c]:
                    crt_len += 1
                else:
                    crt_len = i - indexes[c]
                    last_index = indexes[c] + 1
            else:
                    crt_len += 1
            # 记录(更新)字符 c 的索引
            indexes[c] = i
            if crt_len > max_len:
                max_len = crt_len
        return max_len



if __name__ == '__main__':
    start = time.time()
    s = Solution()
    result = s.lengthOfLongestSubstring("abcabcbbk")
    print(time.time() - start, result)
