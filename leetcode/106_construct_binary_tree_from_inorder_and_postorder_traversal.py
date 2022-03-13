"""Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary
tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Example 1:
            3
          /  \
         9    20
             /  \
            15   7

    Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
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
    通过中序和后序序列递归构建子树
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return

        root_val = postorder[-1]
        index = inorder.index(root_val)
        root = TreeNode(root_val)

        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])

        return root


class SolutionB:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        cache = {}
        # 缓存节点在中序遍历结果中的索引
        for i, v in enumerate(inorder):
            cache[v] = i

        # 递归构建左右子树
        def build(low, high):
            if low > high:
                return
            # 根节点是后序遍历结果中的最后一个节点
            root = TreeNode(postorder.pop())
            # 基于缓存查找 root 节点在中序序列中的索引
            mid = cache[root.val]

            # !!! 注意，一定需要先处理右子树，再处理左子树
            # why ???
            # 在中序序列中 root 节点位置所在的右边序列即是 root 节点的右子树
            root.right = build(mid + 1, high)
            # 在中序序列中 root 节点位置所在的左边序列即是 root 节点的左子树
            root.left = build(low, mid - 1)
            return root

        return build(0, len(inorder) - 1)


class SolutionC:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        cache = {}
        # 缓存节点在中序遍历结果中的索引
        for i, v in enumerate(inorder):
            cache[v] = i

        def build(postorder, post_start, post_end, inorder, in_start, in_end):
            if post_start > post_end or in_start > in_end:
                return
            root = TreeNode(postorder[post_end])
            root_index = cache[postorder[post_end]]
            left_len = root_index - in_start

            root.left = build(postorder, post_start, post_start + left_len - 1, inorder, in_start,
                              root_index - 1)
            root.right = build(
                postorder,
                post_start + left_len, post_end - 1, inorder, root_index + 1, in_end)
            return root

        n = len(postorder)
        return build(postorder, 0, n - 1, inorder, 0, n - 1)


if __name__ == '__main__':

    testcases = [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1])
    ]

    ss = (Solution(), SolutionB(), SolutionC(),)
    for case in testcases:
        for s in ss:
            root = s.buildTree(case[0][:], case[1][:])
            expect_root = BinaryTreeBuilder.build_from_level_ordered(case[2])
            result = [node.val for node in BinaryTreeFormatter.level_order(root)]
            expect_result = [node.val for node in BinaryTreeFormatter.level_order(expect_root)]
            assert result == expect_result
