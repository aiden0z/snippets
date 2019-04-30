"""Generate Parentheses

Given n pairs of parenthese, write a function to generate all combinations of well-formed
parentheses.

For example, given n = 3, a solution set is:
    [
        '((()))',
        '(()())',
        '(())()',
        '()(())',
        '()()()',
    ]

Refer https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    """穷举解法"""

    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')' and stack.pop() != '(':
                    return False
        if len(stack) > 0:
            return False
        return True

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []

        # 获取所有可能的组合
        def generate(s):
            if len(s) == n * 2:
                if self.isValid(s):
                    results.append(s)
                return
            generate(s + '(')
            generate(s + ')')

        generate('(')
        return results


class SolutionRecursive:
    """非穷举递归解法
    符号总是成对出现，且 ')' 总是应出现在 '(' 右边
    """

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        para = []
        self.findmatch('', para, n, 0, 0)
        return para

    def findmatch(self, s, para, n, left, right):
        if right == n:
            return para.append(s)
        if left < n:
            self.findmatch(s + '(', para, n, left + 1, right)
        if right < left:
            self.findmatch(s + ')', para, n, left, right + 1)


class SolutionDP:
    """动态规划解法"""

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                # print(i, j, dp[i], dp[j], dp[i-j-1])
        return dp[n]


if __name__ == '__main__':
    cases = [(2, ['(())', '()()']), (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
             (4, [
                 '(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()',
                 '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'
             ])]
    solutions = [Solution, SolutionRecursive, SolutionDP]
    for case in cases:
        print('generate {} paris'.format(case[0]))
        for s in solutions:
            assert set(case[1]) == set(s().generateParenthesis(case[0]))
