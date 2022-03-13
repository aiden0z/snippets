"""Maximum Binary Tree
You are given an integer array nums with no duplicates. A maximum binary tree can be build
recursively from nums using following algorithm:

    1. Create a root node whose value is the maximum value in nums;
    2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
    3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built form nums.


Example 1:
             6
           /  \
          /    \
         3      5
          \    /
           2  0
            \
             1

    Input: root = [3, 2, 1, 6, 0, 5]
    Output: [6, 3, 5, null, 2, 0, nul, nul, 1]
    Explanation: The recursive calls are follow:
    - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0, 5].
        - The largest value in [3, 2, 1] is 3. left prefix is [] and right suffix is [2, 1].
            - Empty array, so no child.
            - The largest value in [2, 1] is 2. Left prefix is [] and right suffix is [1].
                - Empty array, so no child.
                - Only one element, so child is a node with value 1.
        - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
            - Only one element, so child is a node with value 0.
            - Empty array, so no child.


Example 2:
             3
              \
               2
                \
                 1

    Input: nums = [3, 1, 1]
    Output: [3, null, 2, null, 1]

Constraints:
    * 1 <= nums.length <= 1000
    * 0 <= nums[i] <= 1000
    * All integers in nums are unique
"""

from typing import Optional, List

from utils.binary_tree import TreeNode, BinaryTreeFormatter, BinaryTreeBuilder

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_value = max(nums)
        index = nums.index(max_value)
        left = self.constructMaximumBinaryTree(nums[0:index])
        right = self.constructMaximumBinaryTree(nums[index+1:])
        node = TreeNode(max_value)
        node.left = left
        node.right = right
        return node



if __name__ == '__main__':

    testcases = [
        ([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1]),
        ([3, 2, 1], [3, None, 2, None, 1])
    ]

    ss = (Solution(), )
    for case in testcases:
        for s in ss:
            root = s.constructMaximumBinaryTree(case[0])
            expect_root = BinaryTreeBuilder.build_from_level_ordered(case[1])
            result = [node.val for node in BinaryTreeFormatter.level_order(root)]
            expect_result = [node.val for node in BinaryTreeFormatter.level_order(expect_root)]
            assert result == expect_result
