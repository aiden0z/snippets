"""Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST)，find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor):
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendants of itself)".

Example 1:
             6
           /  \
          /    \
         2      8
        / \    / \
       0   4  7   9
          / \
         3   5
    Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
             6
           /  \
          /    \
         2      8
        / \    / \
       0   4  7   9
          / \
         3   5
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the
    LCA definition.

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTreeBuilder:

    @staticmethod
    def build_from_level_ordered(level_ordered_tree: List) -> Optional[TreeNode]:
        if not level_ordered_tree:
            return None
        root = TreeNode(level_ordered_tree[0])
        nodes = [root]
        start = 1
        while nodes and start < len(level_ordered_tree):
            node = nodes[0]
            node.left = TreeNode(level_ordered_tree[start]) if level_ordered_tree[start] is not None else None
            nodes.append(node.left)
            if start < len(level_ordered_tree) - 1 and level_ordered_tree[start+1] is not None:
                node.right = TreeNode(level_ordered_tree[start + 1])
            else:
                node.right = None
            nodes.append(node.right)
            start += 2
            nodes.pop(0)
        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if p.val > q. val:
            return self.lowestCommonAncestor(root, q, p)

        # p <= root <= q
        # 即 p 和 q 分别在 root 的左右子树，那么 root 就是 LCA
        if p.val <= root.val <= q.val:
            return root

        # p 和 q 都在 root 左子树
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p 和 q 都在 root 右子树
        return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':

    testcases = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ]

    ss = (Solution(),)
    for case in testcases:
        root = BinarySearchTreeBuilder.build_from_level_ordered(case[0])
        for s in ss:
            assert s.lowestCommonAncestor(root, TreeNode(case[1]), TreeNode(case[2])).val == case[3]

