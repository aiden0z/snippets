"""Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need be validated according to
following rules:

    1. Each row must contain the digits 1-9 wihout repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub boxes of the grid must contain he digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Example 1:

    Input:
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true

Example 2:

    Input:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]

    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    The given board contain only digits 1-9 and the character '.'.
    The given board size is always 9x9.
"""


class Solution:

    @staticmethod
    def notInRow(matrix, row):
        st = set()
        for i in range(9):
            if matrix[row][i] in st:
                return False
            if matrix[row][i] != '.':
                st.add(matrix[row][i])
        return True

    @staticmethod
    def notInCol(matrix, col):
        st = set()
        for i in range(9):
            if matrix[i][col] in st:
                return False
            if matrix[i][col] != '.':
                st.add(matrix[i][col])
        return True

    @staticmethod
    def notInBox(matrix, startRow, startCol):
        st = set()
        for i in range(3):
            for j in range(3):
                char = matrix[i + startRow][j + startCol]
                if char in st:
                    return False
                if char != '.':
                    st.add(char)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if not (self.notInRow(board, i) and self.notInCol(board, j)
                        and self.notInBox(board, i - i % 3, j - j % 3)):
                    return False
        return True


class SolutionSimple:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        big = set()

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (i, cur) in big or (cur, j) in big or (i // 3, j // 3, cur) in big:
                        return False
                    big.add((i, cur))
                    big.add((cur, j))
                    big.add((i // 3, j // 3, cur))
        return True


if __name__ == '__main__':
    cases = [([["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True),
             ([["8", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False),
             ([[".", ".", "4", ".", ".", ".", "6", "3", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               ["5", ".", ".", ".", ".", ".", ".", "9", "."],
               [".", ".", ".", "5", "6", ".", ".", ".", "."],
               ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
               [".", ".", ".", "7", ".", ".", ".", ".", "."],
               [".", ".", ".", "5", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."]], False)]

    solutions = [Solution, SolutionSimple]
    for case in cases:
        for S in solutions:
            assert S().isValidSudoku(case[0]) == case[1]
