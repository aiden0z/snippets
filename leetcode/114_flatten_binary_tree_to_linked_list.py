"""Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

    * The "linked list" should use the same TreeNode class where the right child pointer points
      to the next node in the list and the left child pointer is always null;
    * The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
    https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg
              1                      1
            /   \                     \
          /      \                     2
         2        5        -->          \
       /  \        \                     3
      3    4        6                     \
                                           4
                                            \
                                             5
                                              \
                                               6

    Input: root = [1, 2, 5, 3, 4, null, 6]
    Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]

Example 2:

    Input: root = []
    Output: []

Example 3:

    Input: root = [0]
    Output: [0]


Constraints:
    * The number of nodes in the tree is in the range [0, 2000]
    * -100 <= Node.val <= 100

Follow-up: Can you flatten the tree in-place (with O(1) extra space)?
"""

from typing import Optional

from utils.binary_tree import TreeNode
from utils.binary_tree import BinaryTreeFormatter, BinaryTreeBuilder


class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        1. 将 root 的左子树和右子树木拉平；
        2. 将 root 的右子树接到左子树下方，然后将整个左子树作为右子树；
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置
        # 1. 左右子树已经被拉平成一条链表
        left = root.left
        right = root.right

        # 2. 将左子树作为右子树
        root.left = None
        root.right = left

        # 3. 将原右子树接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right
        p.right = right


if __name__ == '__main__':
    testcases = [
        ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ([0], [0]),
        (None, None),
    ]

    ss = (Solution(), )
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        expect_root = BinaryTreeBuilder.build_from_level_ordered(case[1])
        for s in ss:
            s.flatten(root)
            if root is None:
                assert root == expect_root
            else:
                result = [node.val for node in BinaryTreeFormatter.level_order(root)]
                assert result == [node.val for node in BinaryTreeFormatter.level_order(expect_root)]

