"""First Missing Positive
Gien an unsorted integer array, find the smallest missing positive integer.

Example 1:

    Input: [1, 2, 0]
    Output: 3

Example 2:

    Input: [3, 4, -1, 1]
    Output: 2

Example 3:

    Input: [7, 8, 9, 11, 12]
    Output: 1

Note:
    Your algorithm should run in O(n) time and uses constant extra space.
"""

from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        minimum = min(nums)
        maximum = max(nums)

        if minimum > 1:
            return 1

        if maximum < 1:
            return 1

        for i in range(1, maximum + 2):
            if i not in nums:
                return i


if __name__ == '__main__':
    cases = [([], 1), ([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1)]

    for case in cases:
        print(Solution().firstMissingPositive(case[0]))
        assert Solution().firstMissingPositive(case[0]) == case[1]
