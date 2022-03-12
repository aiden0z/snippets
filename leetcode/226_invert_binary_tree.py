"""Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg
          4                   4
        /   \               /   \
       2     7      -->    7     2
     /  \   /  \         /  \   /  \
    1    3 6    9       9    6 3    1

    Input: root = [4, 2, 7, 1, 3, 6, 9]
    Output: [4, 7, 2, 9, 6, 3, 1]

Example 2:
    https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg
          2                   2
        /   \      -->      /   \
       1     3             3     1

    Input: root = [2, 1, 3]
    Output: [2, 3, 1]

Example 3:
    Input: root = []
    Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 100]
    * -100 <= Node.val <= 100
"""


from typing import Optional

from utils.binary_tree import TreeNode, BinaryTreeBuilder, BinaryTreeFormatter


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root


if __name__ == '__main__':
    testcases = [
        ([1, 2, 3, 4, 5, 6, 7], [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']),
        (None, None),
    ]

    ss = (Solution(), )
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        for s in ss:
            inverted_tree = s.invertTree(root)
            if inverted_tree:
                result = [node.val for node in BinaryTreeFormatter.level_order(inverted_tree)]
            else:
                result = inverted_tree
            assert result == case[1]
