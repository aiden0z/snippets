""""Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it whould be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

    Input: [1, 3, 5, 6], 5
    Output: 2

Example 2:

    Input: [1, 3, 5, 6], 2
    Output: 1

Example 3:

    Input: [1, 3, 5, 6], 7
    Output: 4

Example 4:

    Input: [1, 3, 5, 6], 0
    Output: 0
"""


class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if nums[r] > target:
            return r - 1 or 0
        return r + 1


if __name__ == '__main__':
    cases = [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4), ([1, 3, 5, 6], 0, 0),
             ([1, 2, 4, 6, 7], 3, 2), ([1], 1, 0)]

    solutions = [Solution]
    for case in cases:
        for S in solutions:
            result = S().searchInsert(case[0], case[1])
            print(S.__name__, case, result)
            assert result == case[2]
