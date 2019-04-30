"""Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new
length.

Do not allocate extra space for another array, you should this by modifying the input array in-palce
with O(1) extra memory.

The order of elements can be changed. It does'n matter what you ave beyond the new length.

Excample 1:

    Given nums = [3, 2, 2, 3], val = 3,
    You function should return length = 2, with the first two elements of nums being 2.

    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
    Your function should return length = 5, with the first five of nums
    containing 0, 1, 3, 0 and 4.

    Note that the order of those five elements can be arbitrary.

    It doesn't matter what values are set beyond the returned length.
"""
import copy


class Solution:

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


class SolutionBasedOnPop:

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i, n = 0, len(nums)
        while i < n:
            while n > i and nums[i] == val:
                nums.pop(i)
                n -= 1
            i += 1
        return n


if __name__ == '__main__':
    cases = [([], 1, 0), ([3, 3], 3, 0), ([3, 3, 3], 3, 0), ([3], 3, 0), ([3, 2, 2, 3], 3, 2),
             ([0, 1, 2, 2, 3, 0, 4], 2, 5)]
    solutions = [Solution, SolutionBasedOnPop]
    for case in cases:
        for s in solutions:
            nums = copy.deepcopy(case[0])
            assert s().removeElement(nums, case[1]) == case[2]
            # result = s().removeElement(nums, case[1])
            # print('result', result, nums, case[0])
