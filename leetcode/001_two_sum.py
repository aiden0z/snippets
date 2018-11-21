"""Tow Sum
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


Refer https://leetcode.com/problems/two-sum/description/
"""


class Solution(object):
    """Brute force

    For each element, we try to find its complement by looping through the rest
    of array which takes O(n) time. Therefore, the time complexity is O(n^2).

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def twoSum(self, nums, target):
        for i, v1 in enumerate(nums):
            j = i + 1
            for v2 in nums[j:]:
                if v1 + v2 == target:
                    return [i, j]
                j += 1


class SolutionHash(object):
    """Hash table solution

    Store the each element's index in dict.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def twoSum(self, nums, target):
        hash = {}
        for i, v in enumerate(nums):
            hash[v] = i

        for i, v in enumerate(nums):
            complement = target - v
            if complement in hash:
                return [i, hash[complement]]


class SolutionHashOneLoop(object):
    """Hash table one loop solution

    Store the each element's index in dict.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def twoSum(self, nums, target):
        hash = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hash:
                return [hash[complement], i]
            hash[v] = i


if __name__ == "__main__":
    cases = [
        (([-1, 2, -7, 0], -8), [0, 2]),
        (([2, 7, 11, 15], 9), [0, 1]),
        (([2, 7, -15, 4], -11), [2, 3])
    ]

    solutions = (Solution(), SolutionHash(), SolutionHashOneLoop())
    for s in solutions:
        for case in cases:
            assert s.twoSum(*case[0]) == case[1]
