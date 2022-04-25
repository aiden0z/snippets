"""Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
    Input:
    [
        1 -> 4 -> 5,
        1 -> 3 -> 4,
        2 -> 6
    ]

    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Refer https://leetcode.com/problems/merge-k-sorted-lists/
"""

import heapq
from typing import List

from utils.list import ListNode, create_linked_list



class Solution:
    """迭代递归解法"""

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
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

    def mergeKLists(self, lists: List[ListNode]):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 0:
            return

        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeTwoLists(lists[i], head)
        return head


class SolutionMergeRecursive:
    """归并递归解法"""

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
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

    def mergeKLists(self, lists: List[ListNode]):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        middle = len(lists) // 2
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])
        return self.mergeTwoLists(left, right)


class SolutionSimple:
    """取值排序再拼接"""

    @staticmethod
    def addToList(lists: List[ListNode]):
        values = []
        for node in lists:
            current = node
            while current is not None:
                values.append(current.val)
                current = current.next
        return values

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        values = self.addToList(lists)

        values.sort()
        head = None
        current = None
        for i in values:
            if head is None:
                head = ListNode(i)
                current = head
            else:
                current.next = ListNode(i)
                current = current.next
        return head


class SolutionBasedOnDeque:
    """基于堆排序"""

    @staticmethod
    def addToList(lists: List[ListNode]):
        h = []
        for node in lists:
            current = node
            while current is not None:
                heapq.heappush(h, current.val)
                current = current.next
        return [heapq.heappop(h) for i in range(len(h))]

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        values = self.addToList(lists)

        head = None
        current = None
        for i in values:
            if head is None:
                head = ListNode(i)
                current = head
            else:
                current.next = ListNode(i)
                current = current.next
        return head

if __name__ == '__main__':
    cases = [
        (
            (
                [1, 3, 5],
                [2, 4, 8],
                [6, 7],
            ),
            [1, 2, 3, 4, 5, 6, 7, 8]
        )
    ]

    solutions = [Solution(), SolutionMergeRecursive(), SolutionSimple(), SolutionBasedOnDeque()]
    for case in cases:
        for ss in solutions:
            lists = [create_linked_list(array) for array in case[0]]
            result = ss.mergeKLists(lists)
            assert [node.val for node in result] == case[1]
