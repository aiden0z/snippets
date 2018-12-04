""" Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all 
starting indices of substring(s) in s that is a concatenation of each word in words exactly once 
and without any intervening characters.

Example 1:

    s = "barfoothefoofarman",
    workds = ["foo", "bar"]

    Ouput: [0, 9]
    Examplanation: Substring starting at index 0 and 9 are "barfoo" and "foobar" respectively. The 
    ouput order does not matter, returning [9, 0] is fine too.

Example 2:

    s = "wordgoodsstudentgoodword",
    words = ["words", "student]

    Ouput: []
"""

import itertools


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if len(s) == 0 or len(words) == 0:
            return []

        size = len(words[0])
        count = len(words)
        n = size * count

        result = []

        if n > len(s):
            return result

        words_count = {}
        for word in words:
            if word not in words_count:
                words_count[word] = 1
            else:
                words_count[word] += 1
        
        i = 0

        while i <= len(s) - n:

            tmp = dict(words_count.items())
            j = i

            # 遍历子串中的所有单词
            # 如果单词出现则将出现次数减1，最热如果所有单词都出现了相同的次数，则代表
            # 子串符合需求
            while (j < i + n):
                word = s[j:j+size]
                if word not in tmp:
                    break
                else:
                    tmp[word] -= 1
                j += size


            count = 0
            for value in tmp.values():
                if value > 0:
                    count += 1
            
            if count == 0:
                result.append(i)
            i += 1

        return result




class SolutionSlow:
    """穷举
    1. 获取所有单词的排列组合；
    2. 搜索字符串获取子串的位置；
    """

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
                return  -1

            if haystack[i] != needle[0]:
                i += 1
                continue

            found = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            if found:
                yield i
            i += 1

        return -1

    def getAllString(self, words):
        result = set()
        for item in itertools.permutations(words):
            s = ''.join(item)
            if s not in result:
                result.add(s)
        return list(result)
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        strings = self.getAllString(words)

        result = []
        for sub in strings:
            for i in self.strStr(s, sub):
                if i >= 0:
                    result.append(i)
        return result


if __name__ == '__main__':
    cases = [
        ('', [], []),
        ('barfoothefoobarman', ['foo', 'bar'], [0, 9]),
        ('wordgoodsstudentgoodword', ['words', 'student'], []),
        ('catbatatecatatebat', ['cat', 'ate', 'bat'], [0, 3, 9]),
        ('abcdababcd', ['ab', 'ab', 'cd'], [0, 2, 4]),
        ('abcdababcd', ['ab', 'ab'], [4]),
        ('foobarfoobar', ['foo', 'bar'], [0, 3, 6])
    ]

    solutions = [Solution]

    for case in cases:
        for S in solutions:
            result = S().findSubstring(case[0], case[1])
            assert set(result) == set(case[2])
