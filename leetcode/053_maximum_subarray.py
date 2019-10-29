"""Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

Example:

    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: [4, -1, 2, 1] ahs the largest sum = 6.


Follow up: If you have figured out the O(n) solution using the dvide and conquer approach, which
is more subtle.
"""

from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        cur = nums[0]
        for i in nums[1:]:
            cur = max(cur + i, i)
            res = max(res, cur)
        return res


class SolutionDivideConquer:

    def maxSubArray(self, nums: List[int]) -> int:
        return self.divide(nums, 0, len(nums) - 1)

    def divide(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return nums[left]

        mid = left + (right - left) // 2
        left_max = self.divide(nums, left, mid - 1)
        right_max = self.divide(nums, mid + 1, right)

        all_max, tmp = nums[mid], nums[mid]
        for i in range(mid - 1, left - 1, -1):
            tmp += nums[i]
            all_max = max([all_max, tmp])
        tmp = all_max
        for i in range(mid + 1, right + 1):
            tmp += nums[i]
            all_max = max([tmp, all_max])
        return max([all_max, left_max, right_max])


if __name__ == '__main__':
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-2, -1], -1)
    ]  # yapf: disable

    for case in cases:
        for S in [Solution, SolutionDivideConquer]:
            assert S().maxSubArray(case[0]) == case[1]
