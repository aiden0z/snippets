"""Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending postion of 
a given target value. Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1]

Example 1:
    
    Input: nums = [5, 7, 7, 8, 8, 10]
           target = 8
    Output: [3, 4]

Example 2:
    
    Input: nums = [5, 7, 7, 8, 8, 10],
           target = 6
    Output: [-1, -1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = [-1, -1]

        def search(nums, l, r):
            if l > r:
                return
            mid = (l + r) // 2

            if nums[mid] == target:
                if result[0] == -1:
                    result[0] = mid
                result[0] = min(result[0], mid)
                result[1] = max(result[1], mid)
                search(nums, l, mid - 1)
                search(nums, mid+1, r)

            if nums[mid] > target:
                search(nums, l, mid - 1)
            else:
                search(nums, mid + 1, r)

        search(nums, 0, len(nums) - 1)

        return result


if __name__ == '__main__':
    cases = [
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([1, 1, 1 ,1 ,1], 1, [0, 4])
    ]

    solutions = [Solution]

    for case in cases:
        for S in solutions:
            result = S().searchRange(case[0], case[1])
            print(S.__name__, case, result)
            assert result == case[2]

