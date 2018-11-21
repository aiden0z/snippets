"""Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string  is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

    Input: "()"
    Output: true

Example 2:

    Input: "()[]{}"
    Output: true

Example 3:

    Input: "(]"
    Output: false

Example 4:

    Input: "([)]"
    Output: false

Example 5:

    Input: "{[]}"
    Output: true


Refer https://leetcode.com/problems/valid-parentheses
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2  != 0:
            return False

        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ']' and not stack.pop() == '[':
                    return False
                if char == ')' and not stack.pop() == '(':
                    return False
                if char == '}' and not stack.pop() == '{':
                    return False
        if len(stack) > 0:
            return False
        return True
        

if __name__ == '__main__':
    cases = [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True),
        ('((', False),
    ]
    solutions = [Solution]
    for case in cases:
        for solution in solutions:
            print(case[0], case[1], solution().isValid(case[0]))
            assert solution().isValid(case[0]) == case[1]

