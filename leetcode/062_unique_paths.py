""" Unique Paths

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).


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

How many possible unique paths are there ?

Example 1:

    Input: m = 3, n = 2
    Output: 3
    Explation:

    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right


Example 2:

    Input: m = 7, n = 3
    Output: 28


Constraints:

* 1 <= m, n <= 100
* It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """DP solution
        维护一个二维数组 dp，其中 dp[i][j] 表示到 i,j 所在位置不同的走法的个数
        可以获得状态转移方程 dp[i][j] = dp[i-1] + dp[i][j-1]
        """
        # 使用一维数组实现
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]


if __name__ == '__main__':
    cases = [
        ((3, 2), 3),
        ((7, 3), 28),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().uniquePaths(case[0][0], case[0][1]) == case[1]
