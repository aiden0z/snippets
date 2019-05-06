"""Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

    Input: 1
    Output: "1"

Example 2:

    Input: 4
    Output: "1211"

n = 1，输出字符串 1；
n = 2，上次字符串中各个数值的个数，因为上个数字字符串中有 1 个 1，所以输出 11；
n = 3，由于上个字符串是 11，有 2 个 1，所以输出 21；
n = 4，由于上个数字的字符串是 21，有 1 个 2 和 1 个 1，所以输出 1211，依次类推......
"""


class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.calculate(self.countAndSay(n - 1))

    def calculate(self, s: str) -> str:
        if len(s) == 0:
            return ''

        result = ''

        pre_char = s[0]
        count = 1
        for char in s[1:]:
            if char == pre_char:
                count += 1
                continue

            result += '{}{}'.format(count, pre_char)
            count = 1
            pre_char = char

        result += '{}{}'.format(count, pre_char)

        if len(result) == 0:
            return '{}{}'.format(count, pre_char)

        return result


if __name__ == '__main__':
    cases = [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
    ]

    for case in cases:
        result = Solution().countAndSay(case[0])
        assert result == case[1]
