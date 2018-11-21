"""4Sum
Given an array `nums` of n integers and an integer `target`,  are there elements a, b, c and d in 
`nums` such that a + b + c + d = target ? Find all unique quadruplets in the array which gives the 
sum of target.

Note:
The solution set must not contain duplicate quadrupletes.

Example:

Givane array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is :
[
    [-1, 0, 0, 1],
    [-2, -1, 1, 2],
    [-2, 0, 0, 2]
]

Refer https://leetcode.com/problems/4sum
"""

class Solution:
    """二分法思想"""

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        results = []
        
        if len(nums) < 4:
            return results
        nums.sort()

        for i1 in range(len(nums) - 3):
            left = target - nums[i1]
            # 注意右边界的选择，还剩余两个元素需要选择
            for i2 in range(i1 + 1, len(nums) - 2):
                l = i2 + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i2] + nums[l] + nums[r]
                    if s == left:
                        item = [nums[i1], nums[i2], nums[l], nums[r]]
                        # 已存在判断
                        if item not in results:
                            results.append(item)
                        l += 1
                        r -= 1
                    elif s < left:
                        l += 1
                    else:
                        r -= 1
        return results


class SolutionRecursive:
    """递归解法

    基于递归思想缩小问题规模，两个要点：

    1. 如何缩小问题规模?
    2. 何时停止递归？
    """

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        results = set()

        def find_nsum(low, high, target, n, subresult):
            if n < 2:
                return
            if high - low + 1 < n:
                return 
            if target < nums[low] * n:
                return
            if target > nums[high] * n:
                return

            if n == 2:
                # two sum
                while low < high:
                    s = nums[low] + nums[high]
                    if s < target:
                        low += 1
                    elif s > target:
                        high -= 1
                    else:
                        results.add((*subresult, nums[low], nums[high]))
                        low += 1
                        high -= 1
            else:
                for i in range(low, high + 1):
                    # why ?
                    if i == low or (i > low and nums[i-1] != nums[i]):
                        find_nsum(i+1, high, target-nums[i], n-1, (*subresult, nums[i]))
        find_nsum(0, len(nums)-1, target, 4, [])
        return list(results)

if __name__ == '__main__':
    cases = [
        (
            [1, 0, -1, 0, -2, 2], 
            0, 
            [
                [-1, 0, 0, 1],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2]
            ]
        ),
        (
            [0, 0, 0, 0],
            0, 
            [ 
                [0, 0, 0, 0] 
            ]
        ),
        (
            [-3, -2, -1, 0, 0, 1, 2, 3],
            0,
            [
                [-3, -2, 2, 3],
                [-3, -1, 1, 3],
                [-3, 0, 0, 3],
                [-3, 0, 1, 2],
                [-2, -1, 0, 3],
                [-2, -1 , 1 ,2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1]
            ]
        )
    ]
    solutions = [Solution, SolutionRecursive]
    for case in cases:
        target_set = set()
        for item in case[2]:
            target_set.add(tuple(item))
        for solution in solutions:
            result_set = set()
            for item in solution().fourSum(case[0], case[1]):
                result_set.add(tuple(item))
            assert target_set == result_set
