"""N-Queens

The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no
two queens attack each other.

![image](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where
'Q' and '.' both indicate a queen and an empty space respectively.

Example:

    Input: 4
    Output: 2
    Exaplanation: There exist two distinct solutions to the 4-queens puzzle as shown below.

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

"""

from typing import List


class Solution:

    def __init__(self):
        self.queens = None
        self.count = 0

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
            self.count += 1
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

    def totalNQueens(self, n: int) -> int:
        self.queens = n
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(board, 0)
        return self.count


class SolutionDFS:

    def totalNQueens(self, n: int) -> int:
        self.solutions = 0

        def dfs(state: List[int], pd: List[int], nd: List[int]):
            r = len(state)
            if r == n:
                self.solutions += 1
            else:
                for c in range(n):
                    # 表示所在列，主对角线（左上角到右下角），副对角线（左下角到右上角）均没有
                    if c not in state and c - r not in nd and c + r not in pd:
                        dfs(state + [c], pd + [c + r], nd + [c - r])

        dfs([], [], [])
        return self.solutions


if __name__ == '__main__':
    cases = [
        (4, 2)
    ]  # yapf: disable

    for case in cases:
        for S in [Solution, SolutionDFS]:
            assert S().totalNQueens(case[0]) == case[1]
