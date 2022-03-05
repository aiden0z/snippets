"""Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest
value (1-indexed) of all the values of nodes in the tree.

Example 1:

            3
           / \
         1     4
          \
           2

    Input: root = [3, 1, 4, null, 2], k = 1
    Output: 1


Example 2:
            5
           / \
         3     6
        / \
       2   4
      /
     1

    Input: root = [5, 3, 6, 2, 4, nul, nul, 1], k = 3
    Output: 3

Constrians:
    * The number of nodes in the tree is n.
    * 1 <= k <= n <= 10^4
    * 0 <= Node.val <= 10^4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) 
and you need to find the kth smallest frequently, how would you optimize?
"""

from typing import Optional

from utils.binary_tree import TreeNode, BinaryTreeBuilder


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = 0
        self.traverse(root)
        return self.result

    def traverse(self, root):
        """中序排序解决
        """
        if root is None:
            return
        self.traverse(root.left)
        if self.k == 0:
            return
        self.result = root.val
        self.k -= 1
        if self.k == 0:
            return
        self.traverse(root.right)


if __name__ == '__main__':
    testcases = [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ]

    ss = (Solution(),)
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        for s in ss:
            assert s.kthSmallest(root, case[1]) == case[2]
