"""Diameter of Binary Tree
Given the root of a binary tree, return the lengthof the diameter of
the tree.

The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. Tis path may of may not pass through the root
node.

The length of a path betwwen two nodes is represented by the number of
edges between them.

Example 1:
    https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg
                    1
                   / \
                  2   3
                /  \
               4    5
    Input: root = [1, 2, 3, 4, 5]
    Output: 3
    Explanation: 3 is the lenght of path [4, 2, 1, 3] or [5, 2, 1, 3]

Example 2:
    Input: root = [1, 2]
    Output: 1

Constraints:

    * The number of nodes in the tree is in the range [1, 10**4] .
    * -100 <= Node.val <= 100
"""


from typing import Optional

from utils.bst import TreeNode, BinaryTreeBuilder


class Solution:
    """
    每一条二叉树的「直径」长度， 就是一个节点的左右子树的最大深度之和。

    解法是正确的，但是运行时间很长，原因也很明显，traverse 遍历每个节点的
    时候还会调用递归函数 maxDepth，而 maxDepth 是要遍历子树的所有节点的，
    所以最坏时间复杂度是 O(N^2)。

    那如何优化？我们应该把计算「直径」的逻辑放在后序位置，准确说应该是放在
    maxDepth 的后序位置，因为 maxDepth 的后序位置是知道左右子树的最大深度的。

    具体解法查看 SolutionB
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.traverse(root)
        return self.max_diameter

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        current_diameter = left_depth + right_depth
        self.max_diameter = max(self.max_diameter, current_diameter)

        self.traverse(root.left)
        self.traverse(root.right)
        

    def max_depth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return 1 + max(left_depth, right_depth)


class SolutionB:
    """基于后序遍历的解法

    相对于第一种解法，复杂度只有 O(N)。

    遇到子树问题，首先想到的是给函数设置返回值，然后在后序位置做文章。
    反过来，如果你写出了类似一开始的那种递归套递归的解法，大概率也需要
    反思是不是可以通过后序遍历优化了。
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.max_depth(root)

        return self.max_diameter

    def max_depth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        # 后序位置顺便计算最大路径
        current_diameter = left_depth + right_depth
        self.max_diameter = max(self.max_diameter, current_diameter)

        return 1 + max(left_depth, right_depth)

if __name__ == '__main__':
    testcases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ]

    ss = (Solution(), SolutionB())
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        for s in ss:
            assert s.diameterOfBinaryTree(root) == case[1]
