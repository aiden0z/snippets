"""Populating Next Right Pointers in Each Node
You are given a prefect binary tree where all leaves are on the same level, and every parent has
too children. The binary tree has the following definition:

    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the
next pointer should be set to NULL. Initially, all next pointers are set to NULL.

Example 1:
    https://assets.leetcode.com/uploads/2019/02/14/116_sample.png
              1                       1   -> NULL
            /   \                   /   \
          /      \                /      \
         2        3              2   ->   3 -> NULL
       /  \     /  \           /  \     /  \
      4    5   6    7         4 -> 5 ->6 -> 7 -> NULL
           Figure A                Figure B

    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Output: 1, #, 2, 3, #, 4, 5, 6, 7, #]
    Explanation: Given the above perfect binary tree (Figure A), your function should populate each
    next pointer to point to its next right node, just like in Figure B. The serialized output is in
    level order as connected by the next pointers, which '#' signifying the end of each level.

Example 2:

    Input: root = []
    Output: []

Constraints:
    * The number of nodes in the tree is in the range (0, 2^12 -1]
    * -1000 <= Node.val <= 1000

Follow-up:
    * You may only use constant extra space.
    * The recursive approach is fine. You may assume implicit stack space does not count as extra
      space for this problem.
"""

from typing import Optional

from utils.binary_tree import TreeNode as Node
from utils.binary_tree import BinaryTreeFormatter, BinaryTreeBuilder


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = [root]
        loop = 1
        count = 0
        head = None
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if count == 2 ** (loop - 1) - 1:
                loop += 1
                head = node
            else:
                head.next = node
                head = node
            count += 1
        return root


class SolutionB:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        self.connect_two_node(root.left, root.right)
        return root

    def connect_two_node(self, node1: Node, node2: Node):
        if node1 is None or node2 is None:
            return

        # 前序遍历位置
        node1.next = node2

        # 连接相同父节点的两个子节点
        self.connect_two_node(node1.left, node1.right)
        self.connect_two_node(node2.left, node2.right)

        # 连接跨越父节点的两个子节点
        self.connect_two_node(node1.right, node2.left)


if __name__ == '__main__':
    testcases = [
        ([1, 2, 3, 4, 5, 6, 7], [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']),
        (None, None),
    ]

    ss = (Solution(), SolutionB())
    for case in testcases:
        root = BinaryTreeBuilder.build_from_level_ordered(case[0])
        if root is not None:
            correct_result = [
                node.val for node in
                BinaryTreeFormatter.level_order_with_separator_for_perfect_binary_tree(root)
            ]
        else:
            correct_result = None
        for s in ss:
            connected_tree = s.connect(root)
            if connected_tree is not None:
                result = [
                    node.val for node in
                    BinaryTreeFormatter.level_order_with_connected_binary_tree(connected_tree)]
            else:
                result = None
            assert result == correct_result
