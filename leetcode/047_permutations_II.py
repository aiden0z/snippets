"""Permutations II
Given a collection of numbers that might contain duplicates, retun all possible permutations.

Example:

    Input: [1, 1, 2]
    Output:
        [
            [1, 1, 3],
            [1, 2, 2],
            [2, 1, 1],
        ]
"""

import pprint
from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        l = []
        for i in range(len(nums)):
            m = nums[i]
            rem_nums = nums[:i] + nums[i + 1:]
            # Generating all permutations where m is first element
            for p in self.permuteUnique(rem_nums):
                tmp = [m] + p
                if tmp not in l:
                    l.append([m] + p)
        return l


class SolutionDFS:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: List[int], path: List[int], res: List[List[int]]):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


if __name__ == '__main__':
    cases = [
        (
            [1, 1, 2],
            [
                [1, 1, 2],
                [1, 2, 1],
                [2, 1, 1]
            ]
        ),
        (
            [1, 2],
            [
                [1, 2],
                [2, 1]
            ]
        ),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution, SolutionDFS]:
            result = S().permuteUnique(case[0])
            for item in case[1]:
                assert item in result
