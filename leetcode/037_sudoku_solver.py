"""Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Note:

* The given board contain only digits 1-9 and the chracter '.'.
* You may assume that given Sudoku puzzle will have signle unique soultion.
* The given board size is always 9x9.
"""

def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print(arr[i][j], end=' ')
        print('\n')

class Solution:
    """回溯解法

    Find row, col of an unassigned cell
    If there is none, return true
    For digits from 1 to 9
      a) If there is no conflict for digit at row, col
          assign digit to row, col and recursively try fill in rest of grid
      b) If recursion successful, return true
      c) Else, remove digit and try another
    If all digits have been tried and nothing worked, return false
    """

    @staticmethod
    def inRow(matrix, row, num):
        for i in range(9):
            if matrix[row][i] == num:
                return True
        return False

    @staticmethod
    def inCol(matrix, col, num):
        for i in range(9):
            if matrix[i][col] == num:
                return True
        return False

    @staticmethod
    def inBox(matrix, row, col, num):
        for i in range(3):
            for j in range(3):
                if matrix[i+row][j+col] == num:
                    return True
        return False

    @staticmethod
    def findEmptyCell(matrix):
        for row in range(9):
            for col in range(9):
                if matrix[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self, matrix):
        row, col = self.findEmptyCell(matrix)
        if row == -1:
            return True

        for num in range(1, 10):
            digit = str(num)
            if not (self.inBox(matrix, row-row%3, col-col%3, digit) or 
                    self.inCol(matrix, col, digit) or self.inRow(matrix, row, digit)):
                matrix[row][col] = digit
                if self.solve(matrix):
                    return True
                matrix[row][col] = '.'
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        

if __name__=="__main__": 
      
    # assigning values to the grid 
    grid=[['3','.','6','5','.','8','4','.','.'], 
          ['5','2','.','.','.','.','.','.','.'], 
          ['.','8','7','.','.','.','.','3','1'], 
          ['.','.','3','.','1','.','.','8','.'], 
          ['9','.','.','8','6','3','.','.','5'], 
          ['.','5','.','.','9','.','6','.','.'], 
          ['1','3','.','.','.','.','2','5','.'], 
          ['.','.','.','.','.','.','.','7','4'], 
          ['.','.','5','2','.','6','3','.','.']] 

    Solution().solveSudoku(grid)
    print_grid(grid)
