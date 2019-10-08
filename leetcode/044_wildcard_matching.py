"""Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for
'?' and '*'.

    '?' Matches any single chracter.
    '*' Matches any sequence of characters ( including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
    s could be empty and contains only lowercase letters a-z;
    p could be empty and contains only lowercase letters a-z, and chracters like ? or *.

Example 1:

    Input:
        s = "aa"
        p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:

    Input:
        s = "aa"
        p = "*"
    Output: true
    Explanation: '*' matches any sequence.

Example 3:

    Input:
        s = "cb"
        p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

    Input:
        s = "abceb"
        p = "*a*b"
    Output: true
    Explanation: The first '*' matches the empty sequence, while the second '*' matches the
                 substring "dce".

Example 5:

    Input:
        s = "acdcb"
        p = "a*c?b"
    Output: false
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        sp, pp = 0, 0
        match = 0
        start = -1

        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':
                start = pp
                match = sp
                pp += 1
            elif start != -1:
                pp = start + 1
                match += 1
                sp = match
            else:
                return False
        # 处理连续 * 情况
        while pp < len(p) and p[pp] == '*':
            pp += 1
        return pp == len(p)


class SolutionDP:

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # 状态数组，dp[i][j] 表示字符串 s[0:i-1] 是否和 p[0:j-1] 匹配
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]

        # s 和 p 都为空时表示匹配
        dp[0][0] = True

        # # 当 s 为空，p 为连续的星号时的情况。
        # # 由于星号是可以代表空串的，所以只要 s 为空，那么连续的星号的位置都应该为 true，
        # # 所以我们现将连续星号的位置都赋为 true。
        # for i in range(1, n + 1):
        #     if p[i - 1] == '*':
        #         dp[0][i] = dp[0][i - 1]

        # 当 s 为空时，p 必需有 * 才能匹配，且他的真值一定和去掉 * 后的前面字符串匹配情况相同
        for i in range(1, n + 1):
            dp[0][i] = p[i - 1] == '*' and dp[0][i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 当 p 上一个字符串为 '?' 后者 p 上一个字符串等于 s 上一个字符串，则当前真值与上一位相同
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # p 上一个字符串为 * 时，则表示 p 往后走一位或者 s 往后走一位
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[m][n]


if __name__ == '__main__':

    cases = [
        ('aa', 'a', False),
        ('aa', '*', True),
        ('cb', '?a', False),
        ('abceb', '*a*b', True),
        ('acdcb', 'a*c?b', False)
    ]  # yapf: disable

    for case in cases:
        for S in [Solution, SolutionDP]:
            assert S().isMatch(case[0], case[1]) == case[2]
