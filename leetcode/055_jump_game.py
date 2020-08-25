""" Jump Game

Given an array of non-negative integers, you are initially positioned at the
first index of the array. Each element in the array represents your maximum
jump length at that position. Determine if you are able to reach the last idnex.

Example 1:

    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what.
    Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

    1 <= nums.length <= 3 * 10^4
    0 <= nums[i][j] <= 10^5
"""

from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= n:
                n = i
        return n == 0


if __name__ == '__main__':
    cases = [
        ([0], True),
        ([2, 0, 0], True),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([1, 0, 2, 2, 0], False)
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().canJump(case[0]) == case[1]
