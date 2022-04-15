"""Merge Two Sorted Lists
Merge two sorted linked lists and return it as new list. The new list should be made by splicing
together the nodes of the first two lists.

Example:

    Input: 1 -> 2 -> 4, 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Refer https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Optional

from utils.list import ListNode
from utils.list import create_linked_list


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


class SolutionB:

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2
        return dummy.next


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
        (([1, 3, 5, 7], [2, 4, 6, 8]), create_linked_list(list(range(1, 9)))),
    ]
    solutions = (Solution(), SolutionB(), SolutionRecursive())
    for case in cases:
        for solution in solutions:
            expect = [node.val for node in case[1]]
            l1 = create_linked_list(case[0][0])
            l2 = create_linked_list(case[0][1])
            result = solution.mergeTwoLists(l1, l2)
            assert [node.val for node in result] == expect
