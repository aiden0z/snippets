"""Next Permutation

Implement the next permuation, which rearranges numbers into the lexicographically next greater
permutation of numbers.

If such aggrangement is not possible, it must rearrange it as the lowest possible order(ie, sorted
in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in
the right-hand column.

    1, 2, 3 -> 1, 3, 2
    3, 2, 1 -> 1, 2, 3
    1, 1, 5 -> 1, 5, 1
"""
import copy


class Solution:
    """
    1. Find largest index i such that array[i − 1] < array[i].
       (If no such i exists, then this is already the last permutation.)

    2. Find largest index j such that j ≥ i and array[j] > array[i − 1].

    3. Swap array[j] and array[i − 1].

    4. Reverse the suffix starting at array[i].

    Reference https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    """

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # find non-increasing suffix
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i <= 0:
            nums.sort()
            return

        # find successor to pivot
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        # swap
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # reverse suffix
        nums[i:] = nums[len(nums) - 1:i - 1:-1]


if __name__ == '__main__':
    cases = [([1, 2, 3], [1, 3, 2]), ([3, 2, 1], [1, 2, 3]), ([1, 1, 5], [1, 5, 1])]

    solutions = [Solution]

    for case in cases:
        for S in solutions:
            nums = copy.copy(case[0])
            S().nextPermutation(nums)
            assert case[1] == nums
