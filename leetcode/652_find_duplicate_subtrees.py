"""Find Duplicate Subtrees
Given the root of  binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
              1
            /  \
          /     \
         2       3
       /       /  \
      4       2    4
             /
            4


    Input: root = [1, 2, 3, 4, null, 2, 4, null, null, 4]
    Output: [[2, 4], [4]]

Example 2:
              2
            /  \
          /     \
         1       1

    Input: root = [2, 1, 1]
    Output: [[1]]

Example 1:
              2
            /  \
          /     \
         2       2
       /       /
      3       3


    Input: root = [2, 2, 2, 3, null, 3, null]
    Output: [[2, 3], [3]]


Example 4:
             10
            /  \
          /     \
         2      22
       /  \    /  \
      1   12  1    1


    Input: root = [10, 2, 22, 1, 12, 1, 1]
    Output: [[1]]

Constraints:
    * The number of the nodes in the tree will be in the range [1, 10^4]
    * -200 <= Node.val <= 200

"""

from typing import Optional, List

from utils.binary_tree import TreeNode, BinaryTreeFormatter, BinaryTreeBuilder


class Solution:

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.res = []
        self.cache = {}
        self.traverse(root)
        return self.res

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return ''
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        # 注意分隔符的使用，可以是任意字符，但左子树、右子树和当前值间需要分隔符
        subtree = f'{left}-{right}-{root.val}'
        fre = self.cache.get(subtree, 0)
        if fre == 1:
            self.res.append(root)
        self.cache[subtree] = fre + 1
        return subtree


if __name__ == '__main__':
    testcases = [
        ([1, 2, 3, 4, None, 2, 4, None, None, 4], [[2, 4], [4]]),
        ([2, 1, 1], [[1]]),
        ([2, 2, 2, 3, None, 3, None], [[2, 3], [3]]),
        ([0, 0, 0, 0, None, None, 0, None, None, None, 0], [[0]]),
        ([10, 2, 22, 1, 12, 1, 1], [[1]])
    ]

    ss = (Solution(), )
    for case in testcases:
        for s in ss:
            root = BinaryTreeBuilder.build_from_level_ordered(case[0])
            trees = s.findDuplicateSubtrees(root)
            assert len(trees) == len(case[1])
            for node in trees:
                found = False
                result = [node.val for node in BinaryTreeFormatter.level_order(node)]
                for expect_result in case[1]:
                    if result == expect_result:
                        found = True
                assert found
