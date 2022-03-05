""" Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth ios the number of nodes along the logest
path from the root node down to the farthest leaf node

Example 1:

https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg
             3
            /  \
           9    20
               /  \
             15    7

    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 3

Example 2:

    Input: root = [1, null, 2]
    Output: 2


Constraints:
    * The number of nodes in the tree is in the range [0, 10**4]
    * -100 <= Node.val <= 100
"""

from typing import Optional, List

from utils.binary_tree import TreeNode, BinaryTreeBuilder


class Solution:
    """遍历 -> 回溯算法"""
    def max_depth(self, root: Optional[TreeNode]) -> int:
        res = 0
        depth = 0
        def traverse(root):
            nonlocal res
            nonlocal depth
            if root is None:
                res = max(res, depth)
                return
            # 前序遍历位置
            depth +=1
            traverse(root.left)
            traverse(root.right)
            # 后续位置
            depth -= 1

        traverse(root)
        return res


class SolutionB:
    """分解问题 -> 动态规划"""
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    testcases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ]

    ss = (Solution(), SolutionB())
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        for s in ss:
            assert s.max_depth(root) == case[1]

