"""Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where
   left <= right.

Implement the NumArray class:

* NumArray(int[] nums) Initializes the object with the integer array nums.
* int sumRange(int left, int right) Returns the sum of the elements of nums between indices
  left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
    Input:
        ["NumArray", "sumRange", "sumRange", "sumRange"]
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output:
        [null, 1, -1, -3]

Explanation:
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:
    * 1 <= nums.length <= 10^4
    * -10^5 <= nums[i] <= 105
    * 0 <= left <= right < nums.length
    * At most 10^4 calls will be made to sumRange.
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = nums.copy()
        for i in range(1, len(nums)):
            self.prefix_sum[i] += self.prefix_sum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.get(right) - self.get(left - 1)

    def get(self, i):
        if i < 0 or i >= len(self.prefix_sum):
            return 0
        return self.prefix_sum[i]


if __name__ == '__main__':
    cases = [
        ([-2, 0, 3, -5, 2, -1], [[0, 2], [2, 5], [0, 5]], [1, -1, -3])
    ]

    for case in cases:
        num_array = NumArray(case[0])
        for item in zip(case[1], case[2]):
            assert num_array.sumRange(*item[0]) == item[1]
