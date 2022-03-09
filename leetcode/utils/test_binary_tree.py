from unittest import TestCase

from .binary_tree import BinaryTreeBuilder, BinaryTreeFormatter


class TestBinaryTreeFormatter(TestCase):

    def test_level_order(self):
        #       4
        #     /   \
        #    2     7
        #  /  \   /  \
        # 1    3 6    9
        level_order_result = [4, 2, 7, 1, 3, 6, 9]
        root = BinaryTreeBuilder.build_from_level_ordered(level_order_result)
        result = [node.val for node in BinaryTreeFormatter.level_order(root)]

        self.assertEqual(level_order_result, result, "invalid level ordered result")
