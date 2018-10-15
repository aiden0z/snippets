"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some example:
isMatch("aa", "a") ? false
isMatch("aa", "aa") ? true
isMatch("aaa", "aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true

Refer: https://leetcode.com/problems/regular-expression-matching/description/
"""

class Solution(object):
    """递归解法

    referer: http://www.jianshu.com/p/85f3e5a9fcda
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)

        if p_len == 0:
            return len(s) == 0

        if p_len == 1 or p[1] != '*':
            if s_len == 0 or (p[0] != '.' and p[0] != s[0]):
                return False
            else:
                return self.isMatch(s[1:], p[1:])

        while (s_len != 0 and (s[0] == p[0] or p[0] == '.')):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
            s_len = len(s)

        return self.isMatch(s, p[2:])


class SolutionB(object):
    """ DP 解法
    This problem has a typical solution using Dynamic Programming.
    We define the state P[i][j] to be true if s[0..i) matches p[0..j) and
    false otherwise. Then the state equations are:

    P[i][j] = P[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
    P[i][j] = P[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 times;
    P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] == '*' 
    and the pattern repeats for at least 1 times.

    Referer: http://xiaohuiliucuriosity.blogspot.com/2014/12/regular-expression-matching.html

    """
    def isMatch(self, s, p):
        s_len = len(s)
        p_len = len(p)

        m = [[False for i in range(p_len + 1)] for j in range(s_len + 1)]
        m[0][0] = True
        for i in range(s_len + 1):
            for j in range(1, p_len + 1):
                if p[j-1] == '*':
                    m[i][j] = m[i][j-2] or ( i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.') and m[i-1][j])
                else:
                    m[i][j] = i > 0 and m[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return m[s_len][p_len]


if __name__ == '__main__':
    cases = [('aa', 'a', False), ('aa', 'aa', True), ('aaa', 'aa', False),
             ('aa', 'a*', True), ('aa', '.*', True), ('ab', '.*', True),
             ('aab', 'c*a*b', True)]

    s = Solution()
    sb = SolutionB()
    for case in cases:
        assert s.isMatch(case[0], case[1]) == case[2]
        assert sb.isMatch(case[0], case[1]) == case[2]
