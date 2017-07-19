# -*- coding:utf-8 -*-

import re

"""
Implement a atoi to convert a string to integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are reponseible to gather all the input requirements up front.
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX = 2 ** 31 - 1
        MIN = 0 - 2 ** 31
        str = str.strip()
        pattern = re.compile(r'^[\+|\-]?[0-9]+|^[0-9]*')
        matchs = pattern.findall(str)
        if len(matchs) > 0 and matchs[0] != '':
            result =  int(matchs[0])
            if result > MAX:
                return MAX
            if result < MIN:
                return MIN
            return result
        else:
            return 0

class SolutionB(object):
    def myAtoi(self, str):
        MAX = 2 ** 31 - 1
        MIN = 0 - 2 ** 31
        str = str.strip()
        if len(str) == 0:
            return 0
        tmp = "0"
        result = 0
        i = 0
        if str[0] in "+-":
            tmp = str[0]
            i = 1
        for i in range(i, len(str)):
            if str[i].isdigit():
                tmp += str[i]
            else:
                break
        if len(tmp) > 1:
            result = int(tmp)
        if result > MAX:
            return MAX
        elif result < MIN:
            return MIN
        else:
            return result




if __name__ == '__main__':
    s = Solution()
    sb = SolutionB()
    testcases = [('+-2', 0), ('-ads23', 0), ('012', 12), ('-012', -12),
                 ('+004500', 4500), ('2147483648', 2147483647),
                 ('-2147483649', -2147483648)]
    for case in testcases:
        assert s.myAtoi(case[0]) == case[1]
        assert sb.myAtoi(case[0]) == case[1]
