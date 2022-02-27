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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeBuilder:

    @staticmethod
    def build_from_level_ordered(level_ordered_tree: List) -> Optional[TreeNode]:
        if not level_ordered_tree:
            return None
        root = TreeNode(level_ordered_tree[0])
        nodes = [root]
        start = 1
        while nodes and start < len(level_ordered_tree):
            node = nodes[0]
            node.left = TreeNode(level_ordered_tree[start]) if level_ordered_tree[start] else None
            nodes.append(node.left)
            if start < len(level_ordered_tree) - 1 and level_ordered_tree[start+1]:
                node.right = TreeNode(level_ordered_tree[start + 1])
            else:
                node.right = None
            nodes.append(node.right)
            start += 2
            nodes.pop(0)
        return root


class Solution:
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

