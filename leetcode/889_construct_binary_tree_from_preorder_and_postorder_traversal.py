"""Construct Binary Tree from Preorder and Postorder Traversal
Given two integer arrays preorder and postorder where preorder is the preorder traversal of a binary
tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

If there exist multiple answers, you can return any of them.


Example 1:
              1
            /  \
          /     \
         2       3
       /   \    /  \
      4    5   6    7

    Input: preorder = [1, 2, 3, 4, 5, 6, 7], postorder = [4, 5, 2, 6, 7, 3, 1]
    Output: [1, 2, 3, 4, 5, 6, 7]

Example 2:

    Input: preorder = [1], inorder = [1]
    Output: [1]

Constraints:

    * 1 <= preorder.length <= 30
    * 1 <= preorder[i] <= preorder.length
    * All the values of preorder are unique.
    * postorder.length == preorder.length
    * 1 <= postorder[i] <= postorder.length
    * All the values of postorder are unique.
    * It is guaranteed that preorder and postorder are the preorder traversal and postorder
      traversal of the same binary tree.

## 分析

通过前序中序，或者后序中序遍历结果可以确定一棵原始二叉树，但是通过前序后序遍历结果无法确定原始二叉树。 题目也说了，
如果有多种可能的还原结果，你可以返回任意一种。 为什么呢？我们说过，构建二叉树的套路很简单，先找到根节点，然后找到
并递归构造左右子树即可。 105 和 106 两道题，可以通过前序或者后序遍历结果找到根节点，然后根据中序遍历结果确定左右子树。
这道题，你可以确定根节点，但是无法确切的知道左右子树有哪些节点。

不过话说回来，用后序遍历和前序遍历结果还原二叉树，解法逻辑上和前两道题差别不大，也是通过控制左右子树的索引来构建：
1. 首先把前序遍历结果的第一个元素或者后序遍历结果的最后一个元素确定为根节点的值。
2. 然后把前序遍历结果的第二个元素作为左子树的根节点的值。
3. 在后序遍历结果中寻找左子树根节点的值，从而确定了左子树的索引边界，进而确定右子树的索引边界，递归构造左右子树即可。
"""

from typing import Optional, List

from utils.binary_tree import TreeNode, BinaryTreeFormatter, BinaryTreeBuilder


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        cache = {}
        # 缓存节点在中序遍历结果中的索引
        for i, v in enumerate(postorder):
            cache[v] = i

        def build(preorder, pre_start, pre_end, postorder, post_start, post_end):
            if pre_start > pre_end:
                return
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            # root 节点是前序遍历结果的第一个元素
            root_val = preorder[pre_start]

            # root.left 的值是前序遍历结果的第二个元素
            # 通过前序和后序遍历狗子二叉树的关键在于通过左子树的根节点
            # 确定 preorder 和 postorder 中左右子树的元素区间
            root_left_val = preorder[pre_start+1]
            # root_left_val 在后序遍历结果中的索引
            index = cache[root_left_val]

            # 左子树的元素个数
            left_size = index - post_start + 1

            # 先构造当前根节点
            root = TreeNode(root_val)
            # 递归构建左右子树
            # 根据左子树的根节点索引和元素个数推导左右子树的索引边界
            root.left = build(
                preorder, pre_start + 1, pre_start + left_size, postorder, post_start, index)
            root.right = build(
                preorder, pre_start + left_size + 1, pre_end, postorder, index + 1, post_end - 1)
            return root
        n = len(postorder)
        return build(preorder, 0, n - 1, postorder, 0, n - 1)


class SolutionB:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return
        val = preorder.pop(0)
        postorder.pop()
        root = TreeNode(val)
        if not postorder:
            return root
        # index of right child
        index = preorder.index(postorder[-1])
        root.left = self.constructFromPrePost(preorder[:index], postorder[:index])
        root.right = self.constructFromPrePost(preorder[index:], postorder[index:])
        return root


if __name__ == '__main__':
    testcases = [
        ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 3, 4, 5, 6, 7]),
        ([1], [1], [1])
    ]

    ss = (Solution(), SolutionB())
    for case in testcases:
        for s in ss:
            root = s.constructFromPrePost(case[0][:], case[1][:])
            expect_root = BinaryTreeBuilder.build_from_level_ordered(case[2])
            result = [node.val for node in BinaryTreeFormatter.level_order(root)]
            expect_result = [node.val for node in BinaryTreeFormatter.level_order(expect_root)]
            assert result == expect_result
