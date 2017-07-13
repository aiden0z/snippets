# coding:utf-8

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):

    def twoSum(self, nums, target):
        i = -1
        for v1 in nums:
            i += 1
            j = i + 1
            for v2 in nums[j:]:
                if v1 + v2 == target:
                    return [i, j]
                j += 1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([-1, 2, -7, 0], -8))
