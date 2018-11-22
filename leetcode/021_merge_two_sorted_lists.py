"""Merge Two Sorted Lists
Merge two sorted linked lists and return it as new list. The new list should be made by splicing
together the nodes of the first two lists.

Example:

    Input: 1 -> 2 -> 4, 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Refer https://leetcode.com/problems/merge-two-sorted-lists/
"""


def generate_linked_list(n, step):
    assert n > 1
    head = ListNode(1)
    node = head
    for i in range(2, n, step):
        node.next = ListNode(i)
        node = node.next
    return head


def iter_linked_list(head):
    node = head
    while node is not None:
        yield node
        node = node.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        if(l1 == None): return l2
        if(l2 == None): return l1
        
        if(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    cases = [
        (generate_linked_list(6, 2), generate_linked_list(6, 3)),
        (generate_linked_list(8, 2), generate_linked_list(6, 3)),
    ]
    solutions = [SolutionRecursive]

    for case in cases:
        print([node.val for node in iter_linked_list(case[0])])
        print([node.val for node in iter_linked_list(case[1])])
        for solution in solutions:
            l = solution().mergeTwoLists(case[0], case[1])
            print(solution.__name__, [node.val for node in iter_linked_list(l)])
