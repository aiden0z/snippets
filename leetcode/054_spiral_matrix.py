"""Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in
spiral order.

Example 1:

    Input:
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 2:

    Input:
        [
            [1, 2,  3,  4],
            [5, 6,  7,  8],
            [9, 10, 11, 12]
        ]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

"""

from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        startRow = 0
        endRow = len(matrix)
        startColumn = 0
        endColumn = len(matrix[0])

        result = []

        while (startRow < endRow and startColumn < endColumn):
            # first row in remaining rows
            for i in range(startColumn, endColumn):
                result.append(matrix[startRow][i])

            startRow += 1

            # last column in remaining columns
            for i in range(startRow, endRow):
                result.append(matrix[i][endColumn - 1])

            endColumn -= 1

            # last row in remaining rows
            if startRow < endRow:
                for i in range(endColumn - 1, startColumn - 1, -1):
                    result.append(matrix[endRow - 1][i])

                endRow -= 1

            # first column in remaining columns
            if startColumn < endColumn:
                for i in range(endRow - 1, startRow - 1, -1):
                    result.append(matrix[i][startColumn])
                startColumn += 1
        return result


if __name__ == '__main__':
    cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().spiralOrder(case[0]) == case[1]
