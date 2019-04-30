"""Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0, 1, 2, 3, 4, 5, 6, 7]) might become [4, 5, 6, 7, 0, 1, 2]).

You are given a target value to search. If found in the arrary return its index, otherwise return
- 1. You may assume no duplicate exists in the array. Your algorithm's runtime complexity must be
in the order of O(logn).

Example 1:

    Input: nums = [4 ,5, 6, 7, 0, 1, 2],
           target = 0
    Output: 4

Example 2:

    Input: nums = [4, 5, 6, 7, 0, 1, 2],
           target = 3
    Ouput: -1
"""


class Solution:
    """二分搜索"""

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find(nums, l, r, key):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == key:
                return mid
            # nums[l:mid] is sorted
            if nums[l] <= nums[mid]:
                if key >= nums[l] and key <= nums[mid]:
                    return find(nums, l, mid - 1, key)
                return find(nums, mid + 1, r, key)
            # if nums[l:mid] is not sorted, then nums[mid:r] must be sorted
            if key >= nums[mid] and key <= nums[r]:
                return find(nums, mid + 1, r, key)
            return find(nums, l, mid - 1, key)

        return find(nums, 0, len(nums) - 1, target)


class SoltuionIteration:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                if nums[i] < target and nums[i] > nums[mid]:
                    j = mid - 1
                elif nums[i] == target:
                    return i
                else:
                    i = mid + 1
            elif nums[mid] > target:
                if nums[j] > target and nums[j] < nums[mid]:
                    i = mid + 1
                elif nums[j] == target:
                    return j
                else:
                    j = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ]

    solutions = [Solution, SoltuionIteration]

    for case in cases:
        for S in solutions:
            result = S().search(case[0], case[1])
            assert result == case[2]
