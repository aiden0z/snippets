"""Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the
array. Each element in the array represents your maximum jump length at that position.

Your goial is reach the last index in the minimum number of jumps.

Example:

    Input: [2, 3, 1, 1, 4]
    Output: 2
    Explanation: The minimumu number of jumps to reach the last index is 2.
        Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note: You can assume that you can always reach the last index.
"""

from typing import List
import sys


class Solution:

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        last_reach = 0
        reach = 0
        step = 0

        for i in range(len(nums)):
            # when last jump can not reach current i, increase the step by 1
            if i > last_reach:
                step += 1
                last_reach = reach
            # update the maximal jump
            reach = max(reach, nums[i] + i)

        if reach < len(nums) - 1:
            return 0

        return step


class SolutionDP:

    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [sys.maxsize for i in range(length)]
        dp[0] = 0

        for i in range(length):
            for j in range(nums[i], 0, -1):
                if i + j > length - 1 or dp[i + j] < dp[i] + 1:
                    continue
                dp[i + j] = dp[i] + 1
        return dp[length - 1]


if __name__ == '__main__':
    cases = [
        ([2, 3, 1, 1, 4], 2)
    ]  # yapf: disable

    for case in cases:
        for S in [Solution, SolutionDP]:
            assert S().jump(case[0]) == case[1]
