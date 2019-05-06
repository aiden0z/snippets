"""Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all
unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    * All numbers (including target) will be positive integers.
    * The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

Example 2:

    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
      [1,2,2],
      [5]
    ]
"""

from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        self.dfs(sorted(candidates), target, [], results, 0)
        return results

    def dfs(self, candidates: List[int], target: int, answer: List[int], results: List[List[int]],
            i: int):

        if target < 0:
            return

        if target == 0:
            results.append(answer)
            return

        for index in range(i, len(candidates)):
            if index > i and candidates[index] == candidates[index - 1]:
                continue
            self.dfs(candidates, target - candidates[index], answer + [candidates[index]], results,
                     index + 1)


class SolutionBacktracking:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        self.find(sorted(candidates), target, [], results, 0)
        return results

    def find(self, candidates: List[int], target: int, answer: List[int], results: List[List[int]],
             start: int):

        if target < 0:
            return

        if target == 0:
            results.append(answer[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            answer.append(candidates[i])
            self.find(candidates, target - candidates[i], answer, results, i + 1)
            answer.pop()


if __name__ == '__main__':
    cases = [([10, 1, 2, 7, 6, 1, 5], 8), ([2, 5, 2, 1, 2], 5)]

    for case in cases:
        for S in [Solution, SolutionBacktracking]:
            print(S().combinationSum2(case[0], case[1]))
