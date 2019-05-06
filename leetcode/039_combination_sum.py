"""Combination Sum
Given a set of candidate numbers (cadidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

The same repeated number may be chosen from candidates ulimited number of times.

Note:
    * All numbers (include target) will be positive integers.
    * The solution set must not contain duplicate combinations.


Example 1:

    Input: candidates = [2, 3, 6, 7], target = 7,
    A solution set is:
    [
        [7],
        [2, 2, 3]
    ]

Example 2:

    Input: candidates = [2, 3, 5], target = 8,
    A solution set is:
    [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]
"""

from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(list(set(candidates)))

        results = []
        self.find(candidates, target, [], results, 0)

        return results

    # deep-first search
    def find(self, candidates: List[int], target: int, answer: List[int], results: List[List[int]],
             i: int):
        if target < 0:
            return

        if target == 0:
            results.append(answer[:])
            return

        while (i < len(candidates) and target - candidates[i] >= 0):
            answer.append(candidates[i])
            self.find(candidates, target - candidates[i], answer, results, i)
            i += 1
            answer.pop()


class SolutionB:

    def combinationSum(self, candidate: List[int], target: int) -> List[List[int]]:
        candidate = sorted(candidate)
        return self.find(candidate, target)

    def find(self, candidates, target):
        results = []
        for i, n in enumerate(candidates):
            if target > (n + n):
                tails = self.find(candidates[i:], target - n)
                results += [[n] + l for l in tails]
            elif target == (n + n):
                results.append([n, n])
            elif target == n:
                results.append([n])
            elif target < n:
                break
        return results


class SolutionDP:

    # dynamic programming
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        dp = [[[]]] + [[] for i in range(target)]
        for i in range(1, target + 1):
            for num in candidates:
                if num > i:
                    break
                for L in dp[i - num]:
                    if i == num or num >= L[-1]:
                        dp[i] += [L + [num]]
        return dp[target]


if __name__ == '__main__':
    cases = [([2, 3, 6, 7], 7), ([2, 3, 5], 8), ([2, 4, 6, 8], 8)]

    for case in cases:
        for S in [Solution, SolutionB, SolutionDP]:
            print(S().combinationSum(case[0], case[1]))
