""" Valid Number
A valid number can be split up into these components (in order):

    1. A decimal number or an integer.
    2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

    1. (Optional) A sign character (either '+' or '-' ).
    2. One of the following formats:
        1. At least one digit followed by a dot '.'.
        2. At least one digit, followed by a dot '.', followed by at least one digit.
        3. A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):

    1. (Optional) A sign chracter (either '+' or '-' ).
    2. At least one digit.


For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.",
 "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the
 following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

    Input: s = "0"
    Output: true

Example 2:

    Input: s = "e"
    Output: false

Example 3:

    Input: s = "."
    Output: false

Example 4:

    Input: s = ".1"
    Output: true

Constraints:

* 1 <= s.length <= 20
* s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+',
  minus '-', or dot '.'.
"""

import re


class Solution:

    def isNumber(self, s: str) -> bool:
        decimal_patterns = [r'[\+-]?[0-9]+\.', r'[\+-]?[0-9]+\.[0-9]+', r'[\+-]?\.[0-9]+']
        integer_patterns = [r'[\+-]?[0-9]+']

        for p in decimal_patterns + integer_patterns:
            if re.match(p + '$', s):
                return True

        for p1 in decimal_patterns:
            for p2 in integer_patterns:
                p = p1 + r'[eE]{1}' + p2 + '$'
                if re.match(p, s):
                    return True
                p = p2 + r'[eE]{1}' + p2 + '$'
                if re.match(p, s):
                    return True
        return False


class SolutionB:

    def isNumber(self, s: str) -> bool:
        s = s.lower().strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif char == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit


if __name__ == '__main__':
    cases = [("0", True), ("0089", True), ("-0.1", True), ("+3.14", True), ("-.9", True),
             ("2e10", True), ("-90E3", True), ("3e+7", True), ("+6e-1", True), ("+6e-1", True),
             ("53.5e93", True), ("-123.456e789", True), ("e", False), ("abc", False), ("1a", False),
             ("1e", False), ("e3", False), ("99e2.5", False), ("--6", False), ("-+3", False),
             ("95a54e53", False), ("6+1", False)]

    for case in cases:
        assert Solution().isNumber(case[0]) == case[1]
        assert SolutionB().isNumber(case[0]) == case[1]
