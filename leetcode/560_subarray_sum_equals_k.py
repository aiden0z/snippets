"""Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum
equals to k.

Example 1:
    Input: nums = [1, 1, 1], k = 2
    Output: 2

Example 2:
    Input: nums = [1, 2, 3], k = 3
    Output: 2

Constraints:
    * 1 <= nums.length <= 2*10^4
    * -1000 <= nums[i] <= 1000
    * -10^7 <= k <= 10^7
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和的出现次数
        #
        pre_sum = {0: 1}
        res = 0
        sum0_i = 0
        for i in range(0, len(nums)):
            sum0_i += nums[i]
            # nums[0..j] 前缀和
            sum0_j = sum0_i - k
            # 如果出现了前缀和，则直接更新结果
            if sum0_j in pre_sum:
                res += pre_sum[sum0_j]
            # 把前缀和 nums[0..i] 加入并记录出现次数
            pre_sum[sum0_i] = pre_sum.get(sum0_i, 0) + 1
        return res


class SolutionB:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        res = 0
        # 穷举所有子数组
        for i in range(1, len(nums) + 1):
            for j in range(0, i):
                if pre_sum[i] - pre_sum[j] == k:
                    res += 1
        return res


if __name__ == '__main__':
    cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3)
    ]

    ss = (Solution(), )
    for s in ss:
        for case in cases:
            result = s.subarraySum(case[0], case[1])
            assert result == case[2]
