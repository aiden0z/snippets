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


class SolutionBacktrace:

    def cal(self, nums: List[int], l: int, r: int, result: List):
        nums = nums[:]
        if l == r:
            result.append(nums)
            return
        for i in range(l, r + 1):
            nums[l], nums[i] = nums[i], nums[l]
            self.cal(nums, l + 1, r, result)
            # 进行回溯, why ？
            nums[l], nums[i] = nums[i], nums[l]

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.cal(nums, 0, len(nums) - 1, result)
        return result


class SolutionB:

    # The idea is to one by one extract all elements,
    # place them at first position and recur for remaining list.
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        l = []

        for i in range(len(nums)):
            m = nums[i]
            rem_nums = nums[:i] + nums[i + 1:]
            # Generating all permutations where m is first element
            for p in self.permute(rem_nums):
                l.append([m] + p)

        return l


class SolutionDFS:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: List[int], path: List[int], res: List[List[int]]):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


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
        (
            [1, 2],
            [
                [1, 2],
                [2, 1]
            ]
        ),
        (
            [1, 2, 3, 4],
            [
                [1, 2, 3, 4],
                [1, 2, 4, 3],
                [1, 3, 2, 4],
                [1, 3, 4, 2],
                [1, 4, 2, 3],
                [1, 4, 3, 2],
                [2, 1, 3, 4],
                [2, 1, 4, 3],
                [2, 3, 1, 4],
                [2, 3, 4, 1],
                [2, 4, 1, 3],
                [2, 4, 3, 1],
                [3, 1, 2, 4],
                [3, 1, 4, 2],
                [3, 2, 1, 4],
                [3, 2, 4, 1],
                [3, 4, 1, 2],
                [3, 4, 2, 1],
                [4, 1, 2, 3],
                [4, 1, 3, 2],
                [4, 2, 1, 3],
                [4, 2, 3, 1],
                [4, 3, 1, 2],
                [4, 3, 2, 1]
            ]
        )

    ]  # yapf: disable

    for case in cases:
        for S in [SolutionBacktrace, SolutionB, SolutionDFS]:
            result = S().permute(case[0])
            for item in case[1]:
                assert item in result
            # assert S().permute(case[0]) == case[1]
