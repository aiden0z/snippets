"""Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicate in-place sunch that each element appear only once 
and return the new length.

Do not allocate extra space for another array, you must to this by modifying the input array 
in-place with O(1) extray memory.

Example 1:

    Gieven nums = [1, 1, 2],

    Your function should return length = 2, 
    with the first two elements of nums being 1 and 2
    respectively.

    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    Your function should return length = 5, 
    with the first five elements of nums being
    modified to 0, 1, 2, 3, and 4 respectively.

    It does't matter what values are set byond the returned length.


Clarification:

Confused why the returned value is an integer but you answer is an array?

Note that input array is passed in by reference, which means modification to the input array will 
be known to the caller as well.

Internally you can think of this:

    // nums is passed in by reference. (i.e., witout makeing a copy)
    int len = removeDuplicates(nums);

    // any modifcation to the nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++)
    {
        print(nums[i]);
    }
"""
import copy


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return len(nums)
        l, r = 0, 1
        n = len(nums)

        while r < n:
            while r < n and nums[r] == nums[l]:
                r += 1
            if r < n:
                l += 1
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                r += 1
        return l + 1

class SolutionFast:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = 0

        for i in range(1, len(nums)):
            current = nums[i] 
            if current != nums[prev]:
                prev += 1
                nums[prev] = current
        return prev + 1

class SolutionSlow:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        right = len(nums) - 1 
        for i in range(1, len(nums)):
            while True:
                if i == right + 1:
                    break
                if nums[i] == nums[i-1]:
                    tmp = nums[i]
                    # 移动所有元素
                    k = i
                    while k <= len(nums) - 2:
                        nums[k] =nums[k+1]
                        k += 1
                    # 将重复元素移动到末尾
                    nums[len(nums) - 1] = tmp
                    right -= 1
                else:
                    break
            if i == right + 1:
                break
        if right == len(nums) - 1:
            return len(nums)
        return i


if __name__ == '__main__':
    cases = [
        ([1, 1], 1),
        ([1, 1, 1], 1),
        ([1, 2, 3, 4], 4),
        ([1, 1, 2, 3, 4], 4),
        ([1, 1, 2, 3, 3, 4, 4, 5], 5),
        ([1, 2, 3, 3, 3, 4, 4, 5, 5], 5),
        ([1, 1, 1, 1, 2], 2),
    ]

    solutions = [Solution, SolutionFast]
    for case in cases:
        print('Input: {}, {}'.format(case[0], case[1]))
        for s in solutions:
            nums = copy.deepcopy(case[0])
            result = s().removeDuplicates(nums)
            assert result == case[1]
            print('{} Output: {}, {}'.format(s.__name__, nums, result))