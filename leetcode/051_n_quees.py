"""N-Queens

The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no
two queens attack each other.

![image](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where
'Q' and '.' both indicate a queen and an empty space respectively.

Example:

    Input: 4
    Output:
        [
            [
                ".Q..",  // Solution 1
                "...Q",
                "Q...",
                "..Q."
            ],

            [
                "..Q.",  // Solution 2
                "Q...",
                "...Q",
                ".Q.."
            ]
        ]

    Exaplanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

from typing import List


class Solution:

    def __init__(self):
        self.queens = None
        self.results = []

    def printResults(self):
        for i, board in enumerate(self.results):
            print('Solution %d\n' % i)
            for row in board:
                for item in row:
                    print(item, end=' ')
                print('\n')
            print('\n')

    def isSafe(self, board: List[str], row: int, col: int) -> bool:
        # check this row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # check lower diagonal on left side
        for i, j in zip(range(row, self.queens, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    def solve(self, board: List[str], col: int) -> bool:
        # find a solution
        if col == self.queens:
            self.results.append([''.join(rows) for rows in board])
            return True

        res = False
        # check row
        for i in range(self.queens):
            if self.isSafe(board, i, col):
                board[i][col] = 'Q'
                res = self.solve(board, col + 1)
                # backtracking
                board[i][col] = '.'
        return res

    def solveNQueens(self, n: int) -> List[str]:
        self.queens = n
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(board, 0)
        self.printResults()
        return self.results


if __name__ == '__main__':
    cases = [
        (
            4,
            [
                [
                    ".Q..",
                    "...Q",
                    "Q...",
                    "..Q."
                ],
                [
                    "..Q.",
                    "Q...",
                    "...Q",
                    ".Q.."
                ]
            ]
        )
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            result = S().solveNQueens(case[0])
            for item in case[1]:
                assert item in result
