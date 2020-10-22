""" Unique Paths II

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids.
How many unique paths would there be?


+-----------+-----+-----+-----+-----+-----+
|start|     |     |     |     |     |     |
|     |     |     |     |     |     |     |
+-----------------------------------------+
|     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |
+-----------------------------------------+
|     |     |     |     |     |     |finish
|     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+

![leetcode picture](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example 1:

    Input:

        [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]

    Output: 2

    Explanation:

    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right
"""

from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """DP solution
        维护一个二维数组 dp，其中 dp[i][j] 表示到 i,j 所在位置不同的走法的个数
        可以获得状态转移方程 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
            return 0

        # 创建 (m+1)x(n+1) 的二维数组，可以更简单的处理溢出情况
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [([0] * (n + 1)) for _ in range(m + 1)]
        print(dp)
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 处理障碍物
                if obstacleGrid[i - 1][j - 1] != 0:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    cases = [
        (
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            2
        ),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().uniquePathsWithObstacles(case[0]) == case[1]
