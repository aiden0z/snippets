"""Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where perorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:
            3
          /  \
         9    20
             /  \
            15   7

    Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
    Output: [3, 9, 20, null, null, 15, 7]

Example 2:

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:

    * 1 <= preorder.length <= 3000
    * inorder.length == preorder.length
    * -3000 <= preorder[i], inorder[i] <= 3000
    * preorder and inorder consist of unique values.
    * Each value of inorder also appears in preorder.
    * preorder is guaranteed to be the preorder traversal of the tree.
    * inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import Optional, List

from utils.binary_tree import TreeNode, BinaryTreeFormatter, BinaryTreeBuilder


class Solution:
    """
    通过前序和中序序列递归构建子树
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return

        root_val = preorder[0]
        index = inorder.index(root_val)
        root = TreeNode(root_val)

        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return root


if __name__ == '__main__':

    testcases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1])
    ]

    ss = (Solution(), )
    for case in testcases:
        for s in ss:
            root = s.buildTree(case[0], case[1])
            expect_root = BinaryTreeBuilder.build_from_level_ordered(case[2])
            result = [node.val for node in BinaryTreeFormatter.level_order(root)]
            expect_result = [node.val for node in BinaryTreeFormatter.level_order(expect_root)]
            assert result == expect_result
