"""3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Refer https://leetcode.com/problems/3sum
"""


class Solution:
    def threeSum(self, nums):
        """ based on binary search
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1
                elif s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
        return res


class SolutionB:
    @staticmethod
    def get_id(nums):
        return '{0}{1}{2}'.format(*sorted(nums))

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = {}
        length = len(nums)
        for i1, v1 in enumerate(nums):
            if i1 + 2 == length:
                break
            for i2, v2 in enumerate(nums[i1 + 1:]):
                left = 0 - (v1 + v2)
                if i1 + i2 + 2 == length:
                    break
                for v3 in (nums[i1 + i2 + 2:]):
                    if v3 == left:
                        item = [v1, v2, v3]
                        identifiy = self.get_id(item)
                        if identifiy not in result:
                            result[identifiy] = item
        return list(result.values())


if __name__ == '__main__':
    cases = [([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]], 2),
             ([0, 0], [], 0), ([0], [], 0), ([3, -2, 1, 0], [], 0),
             ([1, 2, -2, -1], [], 0), ([0, 0, 0], [[0, 0, 0]], 1)]
    s = Solution()
    for case in cases:
        result = s.threeSum(case[0])
        if len(result) != case[2]:
            assert False
        # ids = [s.get_id(item) for item in result]
        # for nums in case[1]:
        #     assert s.get_id(nums) in ids
