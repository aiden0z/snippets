"""Permutations
Given a collection of distinct integers, retun all possible permutations.

Example:

    Input: [1, 2, 3]
    Output:
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
"""

import pprint
from typing import List


class Solution:

    def cal(self, nums: List[int], result: []):
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            value = [nums[i]]
            left = nums[:i] + nums[i + 1:]
            result.append(value + self.cal(left, result))
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.cal(nums, [])


if __name__ == '__main__':
    cases = [
        (
            [1, 2, 3],
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]
            ]
        ),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            pprint.pprint(S().permute(case[0]))
            # assert S().permute(case[0]) == case[1]
