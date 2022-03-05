"""Lowest Common Ancestor of a Binary Search Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor):
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendants of itself)".

Example 1:
             3
           /  \
          /    \
         5      1
        / \    / \
       6   2  0   8
          / \
         7   4

    Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
             3
           /  \
          /    \
         5      1
        / \    / \
       6   2  0   8
          / \
         7   4

    Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the
    LCA definition.

Example 3:

    Input: root = [1, 2], p = 1, q = 2
    Output: 1

Constraints:

    * The number of nodes in the tree is in the range [2, 105].
    * -109 <= Node.val <= 109
    * All Node.val are unique.
    * p != q
    * p and q will exist in the tree.
"""

from typing import Optional, List

from utils.binary_tree import TreeNode, BinaryTreeBuilder


class Solution:
    """
    根据这个定义，分情况讨论：
    情况 1，如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）。
    情况 2，如果 p 和 q 都不在以 root 为根的树中，直接返回 null。
    情况 3，如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点。

    而又由于是后序遍历，从下往上走，就好比从 p 和 q 出发往上走，第一次相交的节点就是这个root。
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None and right is None:
            return None

        return left if left is not None else right


class SolutionB:
    """该解法将出现超时错误
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.p_in_left = False
        self.p_in_right = False
        self.q_in_left = False
        self.q_in_right = False
        self.ancestor = None
        self.traverse(root)
        return self.ancestor

    def traverse(self, root):
        if root.val == self.p.val or root.val == self.q.val:
            self.ancestor = root
            return

        self.found(root.left, True)
        if self.p_in_left and self.q_in_left:
            self.p_in_left = False
            self.q_in_left = False
            self.traverse(root.left)
        elif self.p_in_left or self.q_in_left:
            self.ancestor = root
            return
        self.found(root.right, False)
        if self.p_in_right and self.q_in_right:
            self.p_in_right = False
            self.q_in_right = False
            self.traverse(root.right)

        if (self.p_in_left and self.q_in_right) or (self.p_in_right and self.q_in_left):
            self.ancestor = root
            return

    def found(self, root, left):
        if root is None:
            return
        if root.val == self.p.val:
            self.p_in_left = left
            self.p_in_right = not left
        elif root.val == self.q.val:
            self.q_in_left = left
            self.q_in_right = not left

        self.found(root.left, left)
        self.found(root.right, left)


if __name__ == '__main__':

    testcases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
        ([-1, 0, 3, -2, 4, None, None, 8], 8, 4, 0)
    ]

    ss = (Solution(), SolutionB())
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        for s in ss:
            result = s.lowestCommonAncestor(root, TreeNode(case[1]), TreeNode(case[2]))
            assert result.val == case[3]

