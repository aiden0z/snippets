"""Sort an Array
Given an array of integers nums, sort the array in ascending order.

Example 1:

    Input: nums = [5, 2, 3, 1]
    Output: [1, 2, 3 ,5]

Example 2:

    Input: nums = [5, 1, 1, 2, 0, 0]
    Output: [0, 0, 1, 1, 2, 5]

Constraints:
    * 1 <= nums.length <= 5 * 10^4
    * -5 * 104 <= nums[i] <= 5 * 10^4
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._merge_sort(nums)

    def _merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2

        result = self._merge(self._merge_sort(nums[0:mid]), self._merge_sort(nums[mid:]))
        return result

    @staticmethod
    def _merge(left_nums: List[int], right_nums: List[int]) -> List[int]:
        result = []
        while left_nums and right_nums:
            if left_nums[0] < right_nums[0]:
                result.append(left_nums.pop(0))
            else:
                result.append(right_nums.pop(0))
        while left_nums:
            result.append(left_nums.pop(0))
        while right_nums:
            result.append(right_nums.pop(0))
        return result


class SolutionB:
    """快排会超时？"""

    def sortArray(self, nums: List[int]) -> List[int]:
        self._quik_sort(nums, 0, len(nums) - 1)
        return nums

    def _quik_sort(self, nums: List[int], low: int, high: int):
        if low >= high:
            return
        pi = self._partition(nums, low, high)
        self._quik_sort(nums, low, pi - 1)
        self._quik_sort(nums, pi + 1, high)

    @staticmethod
    def _partition(nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1


if __name__ == '__main__':
    cases = [
        [5, 2, 3, 0, 1],
        [5, 1, 1, 2, 0, 0]
    ]

    solutions = (SolutionB(), )
    for ss in solutions:
        for case in cases:
            assert ss.sortArray(case) == sorted(case)
