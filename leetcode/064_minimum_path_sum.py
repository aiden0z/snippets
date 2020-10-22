""" Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path
from top left to bottom right which minimizes the sum of all
numbers along its path.

Note: You can only move either down or rigth at any point in time.

Example 1:

    Input:

        [
          [1, 3, 1],
          [1, 5, 1],
          [4, 2, 1]
        ]

    Output: 7
    Explanation: Because the path 1->3->1->1->1 minimizes the sum.
"""

from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # 第 0 列的和等于上一项加上一行的值
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # 第 0 行和等于等于前一列的值累加
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    cases = [
        # (
        #     [
        #         [1],
        #     ],
        #     1
        # ),
        (
            [
                [1, 2],
                [1, 1]
            ],
            3
        ),
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1]
            ],
            7
        ),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            count = S().minPathSum(case[0])
            print(count, case[1])
            assert count == case[1]
