"""Reverse Pairs
Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j]

Example 1:
    Input: nums = [1, 3, 2, 3, 1]
    Output: 2

Example 2:
    Input: nums = [2, 4, 3, 5, 1]
    Output: 3


Constraints:
    1 <= nums.length <= 5 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> List[int]:
        self.tmp = [None] * len(nums)
        self.count = 0

        self._merge_sort(nums, 0, len(nums) -1)
        return self.count

    def _merge_sort(self, nums: List[int], lo: int, hi: int):
        if lo == hi:
            return
        # 防止溢出，py 中不存在该问题
        mid = lo + (hi - lo) // 2
        self._merge_sort(nums, lo, mid)
        self._merge_sort(nums, mid + 1, hi)
        self._merge(nums, lo, mid, hi)

    def _merge(self, nums: List[int], lo: int, mid: int, hi: int):
        """
        对于 nums[i], lo <= i <= mid，我们在找到的符合 nums[i] > 2*nums[j] 的 nums[j],
        mid+1 <= j <= hi，也必然也符合 nums[i+1] > 2*nums[j]。
        换句话说，我们不用每次都傻乎乎地去遍历整个 nums[mid+1..hi]，只要维护一个开区间边界 end，
        维护 nums[mid+1..end-1] 是符合条件的元素即可。
        """
        for i in range(lo, hi+1):
            self.tmp[i] = nums[i]

        # 合并有序数组之前，处理 reverse paris
        end = mid + 1
        for i in range(lo, mid+1):
            while end <= hi and nums[i] > nums[end] * 2:
                end += 1
            self.count += (end - (mid + 1))
            # for j in range(mid+1, hi+1):
            #     if nums[i] > nums[j] * 2:
            #         self.count += 1

        # 双指针合并两个有序数组
        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            # 左半边数组已被全部合并
            if i == mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            # 右半边数组已被全部合并
            elif j == hi + 1:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] > self.tmp[j]:
                nums[p] = self.tmp[j]
                j += 1
            else:
                nums[p] = self.tmp[i]
                i += 1


class SolutionB:

    def reversePairs(self, nums):
        nums, count = self._merge_sort(nums)
        return count

    def _merge_sort(self, nums):
        if len(nums) <= 1:
            return nums, 0

        l_arr, left = self._merge_sort(nums[:len(nums) // 2])
        r_arr, right = self._merge_sort(nums[len(nums) // 2:])

        l_pointer = len(l_arr) - 1
        r_pointer = len(r_arr) - 1
        count = left + right
        while l_pointer >= 0:
            while r_arr[r_pointer] * 2 >= l_arr[l_pointer]:
                r_pointer -= 1
                if r_pointer < 0:
                    break
            if r_pointer < 0:
                break
            count += r_pointer + 1
            l_pointer -= 1
        l_arr += r_arr
        l_arr.sort()
        return l_arr, count


if __name__ == '__main__':
    cases = [
        ([1, 3, 2 ,3, 1], 2),
        ([2, 4, 3, 5, 1], 3)
    ]
    solutions = (Solution(), SolutionB())
    for s in solutions:
        for case in cases:
            result = s.reversePairs(case[0][:])
            assert result == case[1]
