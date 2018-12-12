"""Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid
(well-formed) parentheses substring.

Example 1:

    Input: "(()"
    Output: 2
    Explannation: The longest valid parentheses substring is "()"

Example 2:

    Input: ")()())"
    Output: 4
    Explannation: The longest valid parentheses substring is "()()"

"""
class Solution:
    """O(n) 堆栈解法"""

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []

        i, start, length = 0, 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        length = max(length, i - start + 1)
                    else:
                        length = max(length, i - stack[-1])
        return length


class SolutionSimple:
    """O(n)堆栈解法，简化版本"""
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] 
        stack.append(-1) 
  
        result = 0
  
        for i in range(len(s)): 
            if s[i] == '(': 
                stack.append(i) 
            else:
                stack.pop() 
                if len(stack) != 0: 
                    result = max(result, i - stack[-1])
                else: 
                    stack.append(i) 
        return result

class SolutionDP:
    """DP 解法

    1) Create an array longest of length n (size of the input string) initialized to zero.
    The array will store
    the length of the longest valid substring ending at that index.

    2) Initialize result as 0.

    3) Iterate through the string from second character
       a) If the character is '(' set longest[i]=0 as no valid sub-string will end with '('.
       b) Else
          i) if s[i-1] = '('
                set longest[i] = longest[i-2] + 2
          ii) else
                set longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

    4) In each iteration update result as the maximum of result and longest[i]

    5) Return result.
    """

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if  len(s) <= 1:
            return 0

        longest = [0] * len(s)
        result = 0

        for i in range(len(s)):
            if s[i] == ')' and i - longest[i-1] -1 >= 0 and s[i - longest[i-1] - 1] == '(':
                if i - longest[i-1] -2 >= 0:
                    longest[i] = longest[i-1] + 2 + longest[i-longest[i-1] - 2] 
                else:
                    longest[i] = longest[i-1] + 2
                result  = max(result, longest[i])
        return result


class SolutionWithoutSpace:
    """使用 O(1) 的空间

    左右各遍历一次，寻找所有情况
    """
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, l, r = 0, 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if r > l:
                l = r = 0
            elif r == l:
                result = max(result, r * 2)
        l = r = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1

            if r < l:
                r = l = 0
            elif r == l:
                result = max(result, r * 2)

        return result


class SolutionSlow:
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

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                # 若干优化，避免入栈
                if (j+1 -i) % 2 != 0 or s[i] == ')' or s[j] == '(':
                    continue
                sub = s[i:j+1]
                if self.isValid(sub) and len(sub) > length:
                    length = len(sub)
        return length


if __name__ == '__main__':

    cases = [
        ('()()', 4),
        ('(()', 2),
        (')()())', 4),
        (')()()(', 4),
        (')()(()', 2),
        ('()(()', 2),
        ("())()()(())((()(()()(((()))((((())((()(())()())(()((((()))()(()))(())()(())(()(((((())((((((()())())(()(()((())()))(()))))))()(()))((((())()()()))()()()(((()(()())(()()(()(()()(((()))))))()()))())())((()()))))))((()))(((()((())()(()()))((())))()()())))))))()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))((())((((()))(()(()(()()()(((())()(((((()))((()(((((())(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))((()))(((((()))))())))()((()))()))))())))))((())(((((()()))((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())(", 310)
    ]

    solutions = [SolutionDP, SolutionWithoutSpace]

    for case in cases:
        for S in solutions:
            result = S().longestValidParentheses(case[0])
            assert result == case[1]
