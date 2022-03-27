"""Count of Range Sum
Given an integer array nums and two integers lower and upper, return the number of range nums that
lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive,
where i <= j.

Example 1:
    Input: nums = [-2, 5, -1], lower = -2, upper = 2
    Output: 3
    Explanation: The three ranges are: [0, 0], [2, 2], and [0, 2] and their respective sums are:
    -2, -1, 2.

Example 2:
    Input: nums = [0], lower = 0, upper = 0
    Output: 1

Constraints:
    * 1 <= nums.length <= 10^5
    * -2^31 <= nums[i] <= 2^31 - 1
    * -10^5 <= lower <= upper <= 10^5
    * The answer is guaranteed to fit in a 32-bit integer.
"""


import bisect
from typing import List


class Solution:
    """
    简单说，题目让你计算元素和落在 [lower, upper] 中的所有子数组的个数。
    拍脑袋的暴力解法我就不说了，依然是嵌套 for 循环，这里还是说利用归并排序实现的高效算法。
    首先，解决这道题需要快速计算子数组的和，所以你需要阅读前文 前缀和数组技巧。
    有了前缀和数组 preSum，那么计算区间和 S(i, j) 只需要用 preSum[j] - preSum[i] 就可以计算出来。
    我继续用比较数学的语言来表述下这道题，题目让你通过 preSum 数组求一个 count 数组，使得：
    count[i] = COUNT(j) where lower <= preSum[j] - preSum[i] <= upper
    然后请你求出这个 count 数组中所有元素的和。
    你看，这是不是和题目描述一样？两个 preSum 中的元素之差其实就是区间和。
    """
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        self.count = 0

        # 前缀和记录
        pre_sum = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        self._sort(pre_sum)
        return self.count

    def _sort(self, nums):
        self.tmp = [0] * len(nums)
        self._merge_sort(nums, 0, len(nums) - 1)

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
        """
        for i in range(lo, hi+1):
            self.tmp[i] = nums[i]

        # 维护左闭右开区间 [start, end) 中的元素和 nums[i] 的差在 [lower, upper] 中
        start = mid + 1
        end = mid + 1
        for i in range(lo, mid +1):
            # 如果 nums[i] 对应的区间是 [start, end)
            # 那么 nums[i] 对应区间一定会整体右移，类似滑动窗口
            while start <= hi and nums[start] - nums[i] < self.lower:
                start += 1
            while end <= hi and nums[end] - nums[i] <= self.upper:
                end += 1
            self.count += (end - start)

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
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num)
        res = 0
        prefix_sorted = prefix[1:].copy()
        prefix_sorted.sort()
        for r in range(1, len(nums) + 1):
            lf = upper + prefix[r - 1]
            lu = lower + prefix[r - 1]
            i, j = bisect.bisect_left(prefix_sorted, lu), bisect.bisect_right(prefix_sorted, lf)
            res += (j - i)
            prefix_sorted.pop(bisect.bisect_left(prefix_sorted, prefix[r]))
        return res


if __name__ == '__main__':
    cases = [
        ([-2, 5, -1], (-2, 2), 3),
        ([0], (0, 0), 1)
    ]

    ss = (Solution(), SolutionB())
    for s in ss:
        for case in cases:
            result = s.countRangeSum(case[0], *case[1])
            assert result == case[2]
