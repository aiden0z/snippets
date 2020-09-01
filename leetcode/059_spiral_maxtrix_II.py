""" Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements
from 1 to n2 in spiral order.

Example:

    Input: 3
    Output:
    [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
    ]
"""

from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        startRow = 0
        endRow = n
        startColumn = 0
        endColumn = n

        value = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        while (startRow < endRow and startColumn < endColumn):
            # first row in remaining rows
            for i in range(startColumn, endColumn):

                matrix[startRow][i] = value
                value += 1

            startRow += 1

            # last column in remaining columns
            for i in range(startRow, endRow):
                matrix[i][endColumn - 1] = value
                value += 1

            endColumn -= 1

            # last row in remaining rows
            if startRow < endRow:
                for i in range(endColumn - 1, startColumn - 1, -1):
                    matrix[endRow - 1][i] = value
                    value += 1

                endRow -= 1

            # first column in remaining columns
            if startColumn < endColumn:
                for i in range(endRow - 1, startRow - 1, -1):
                    matrix[i][startColumn] = value
                    value += 1
                startColumn += 1
        return matrix


if __name__ == '__main__':
    cases = [
        (1, [[1]]),
        (2, [[1, 2], [4, 3]]),
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().generateMatrix(case[0]) == case[1]
