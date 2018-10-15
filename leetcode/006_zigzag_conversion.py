"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility):

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line like: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a numbr
of rows:

    string convert(string text, int nRows);

`convert("PAYPALISHIRING", 3)` should return "PAHNAPLSIIGYIR"

Refer: https://leetcode.com/problems/zigzag-conversion/
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        base = 2 * numRows - 2
        length = len(s)
        if length <= numRows:
            return s

        upper = int(length/base) + 2
        if length % base == 0:
            upper -= 1

        d = {}
        for x in range(0, numRows):
            d[x] = []

        for x in range(1, upper):
            for i in range(0, base):
                index = (x-1) * base + i
                if index >= length:
                    break
                if i + 1 > numRows:
                    d[2*numRows - i - 2].append(s[index])
                else:
                    d[i].append(s[index])
            else:
                continue
            break
        result = []
        for x in range(0, numRows):
            result.extend(d[x])
        return ''.join(result)

class SolutionB(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        base = 2 * numRows - 2
        length = len(s)

        if length <= numRows:
            return s

        upper = int(length/base) + 2
        if length % base == 0:
            upper -= 1

        result = []
        for i in range(0, numRows):
            for x in range(1, upper):
                index = (x-1) * base + i
                if index < length:
                    result.append(s[(x-1) * base + i])

                if i != 0 and i != numRows - 1:
                    index = (x-1) * base + 2 * numRows -i - 2
                    if index < length:
                        result.append(s[index])
        return ''.join(result)


class SolutionC(object):
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index = 0

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)


if __name__ == '__main__':
    s = Solution()

    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert s.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert s.convert('', 1) == ''
    assert s.convert('A', 1) == 'A'
    assert s.convert('AB', 1) == 'AB'
    assert s.convert('ABCD', 2) == 'ACBD'

    sb = SolutionB()

    assert sb.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert sb.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert sb.convert('', 1) == ''
    assert sb.convert('A', 1) == 'A'
    assert sb.convert('AB', 1) == 'AB'
    assert sb.convert('ABCD', 2) == 'ACBD'
