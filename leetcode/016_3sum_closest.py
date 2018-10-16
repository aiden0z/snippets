"""
Given an array nums of n integers and an integer target, find three integers in nums such that 
the sum is closest to target. Return the sum of the three integers. You may assume that each 
input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums or len(nums) < 3:
            return 0
        nums.sort()

        minimum = sum(nums[:3])

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if s < target:
                    l += 1
                if s > target:
                    r -= 1
                if abs(s-target) < abs(minimum - target):
                    minimum = s
        return minimum


if __name__ == '__main__':
    cases = [
        ([-1, 2, 1, -4], 1, 2),
        ([-1, -2, 4, 5, -2], 0, 0),
        ([-5, -10, 0, 20], 30, 15)
    ]
    s = Solution()

    for case in cases:
        assert s.threeSumClosest(case[0], case[1]) == case[2]
