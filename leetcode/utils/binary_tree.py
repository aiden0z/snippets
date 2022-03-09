from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeBuilder:

    @staticmethod
    def build_from_level_ordered(level_ordered_tree: list) -> Optional[TreeNode]:
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


class BinaryTreeFormatter:

    @staticmethod
    def level_order(root: TreeNode) -> List[TreeNode]:
        if root is None:
            return None
        result = list()
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            result.append(node)
        return result

    @staticmethod
    def inorder(self, root: TreeNode) -> List[TreeNode]:
        raise NotImplemented

    @staticmethod
    def preorder(self, root: TreeNode) -> List[TreeNode]:
        raise NotImplemented

    @staticmethod
    def postorder(self, root: TreeNode) -> List[TreeNode]:
        raise NotImplemented
