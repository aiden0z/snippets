"""Merge Two Sorted Lists
Merge two sorted linked lists and return it as new list. The new list should be made by splicing
together the nodes of the first two lists.

Example:

    Input: 1 -> 2 -> 4, 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Refer https://leetcode.com/problems/merge-two-sorted-lists/
"""

from utils.list import ListNode
from utils.list import create_linked_list, iter_linked_list


class Solution:
    """迭代解法"""

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode('dummy')
        node = head

        while True:
            if l1 is None or l2 is None:
                break
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        while l1 is not None:
            node.next = l1
            node = node.next
            l1 = l1.next

        while l2 is not None:
            node.next = l2
            node = node.next
            l2 = l2.next
        return head.next


class SolutionRecursive:
    """递归解法"""

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    cases = [
        ((create_linked_list([1, 3, 5, 7]), create_linked_list([2, 4, 6, 8])), create_linked_list(list(range(1, 9)))),
    ]
    solutions = [SolutionRecursive]

    for case in cases:
        for solution in solutions:
            expect = [node.val for node in iter_linked_list(case[1])]
            result = solution().mergeTwoLists(*case[0])
            assert [node.val for node in iter_linked_list(result)] == expect
