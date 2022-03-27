"""Count of Smaller Numbers After Self
You are given an integer array "nums" and you have to return a new counts array. The counts array
has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
    Input: nums = [5, 2, 6, 1]
    Output: [2, 1, 1, 0]
    Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.

Example 2:
    Input: nums = [-1]
    Output: [0]

Example 3:
    Input: nums = [-1, -1]
    Output: [0, 0]

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.tmp = [None] * len(nums)
        self.counts = [0] * len(nums)

        # 缓存原始索引位置
        pairs = []
        # 记录元素原始索引位置，以便在 count 数组中跟下结果
        for i in range(0, len(nums)):
            pairs.append((nums[i], i))

        self._merge_sort(pairs, 0, len(nums) -1)
        return self.counts

    def _merge_sort(self, pairs: List[tuple], lo: int, hi: int):
        if lo == hi:
            return
        # 防止溢出，py 中不存在该问题
        mid = lo + (hi - lo) // 2
        self._merge_sort(pairs, lo, mid)
        self._merge_sort(pairs, mid + 1, hi)
        self._merge(pairs, lo, mid, hi)

    def _merge(self, pairs: List[tuple], lo: int, mid: int, hi: int):
        """
        在对 nums[lo..hi] 合并的过程中，每当执行 nums[p] = temp[i] 时，
        就可以确定 temp[i] 这个元素后面比它小的元素个数为 j - mid - 1。
        当然，nums[lo..hi] 本身也只是一个子数组，这个子数组之后还会被执行 merge，
        其中元素的位置还是会改变。但这是其他递归节点需要考虑的问题，我们只要在 merge
        过程中叠加结果即可。
        """
        for i in range(lo, hi+1):
            self.tmp[i] = pairs[i]
        # 双指针合并两个有序数组
        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            # 左半边数组已被全部合并
            if i == mid + 1:
                pairs[p] = self.tmp[j]
                j += 1
            # 右半边数组已被全部合并
            elif j == hi + 1:
                pairs[p] = self.tmp[i]
                i += 1
                # 更新 counts 数组
                self.counts[pairs[p][1]] += j - mid - 1
            elif self.tmp[i][0] > self.tmp[j][0]:
                pairs[p] = self.tmp[j]
                j += 1
            else:
                pairs[p] = self.tmp[i]
                i += 1
                # 更新 count 数组
                self.counts[pairs[p][1]] += j - mid - 1


class SolutionB:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            result.append(self.found_right_smaller_count(nums, i))
        return result

    @staticmethod
    def found_right_smaller_count(nums: List[int], index: int) -> int:
        if index == len(nums) - 1:
            return 0
        value = nums[index]
        count = 0
        for i in nums[index:]:
            if i < value:
                count += 1
        return count


if __name__ == '__main__':
    cases = [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([-1], [0]),
        ([-1, -1], [0, 0])
    ]
    solutions = (Solution(), SolutionB())
    for s in solutions:
        for case in cases:
            result = s.countSmaller(case[0])
            assert result == case[1]
