from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    @property
    def is_separator(self):
        return self.val == '#'

    def __str__(self):
        return f'TreeNode<{self.val}>'


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
            if node is None:
                nodes.pop(0)
                continue
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
    def level_order_with_connected_binary_tree(root: TreeNode) -> List[TreeNode]:
        if root is None:
            return None
        result = []
        node = root
        while node:
            head = node
            while head:
                result.append(head)
                head = head.next
            result.append(TreeNode('#'))
            node = node.left
        return result


    @staticmethod
    def level_order_with_separator_for_perfect_binary_tree(root: TreeNode) -> List[TreeNode]:
        if root is None:
            return None

        result = list()
        queue = list()
        queue.append(root)
        loop = 1
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            result.append(node)
            if len(result) == 2**loop + loop - 2:
                result.append(TreeNode('#'))
                loop += 1
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
