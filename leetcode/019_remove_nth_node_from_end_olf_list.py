"""Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2.

After removing the second node from the end, the linked list becomes 1 -> 2 -> 3 ->5

Note:

Given n will always be valid.

Refer https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""
from utils.list import ListNode, create_linked_list


class Solution:
    """单向链表只能遍历一次后才能知道其长度"""
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        node = head
        while node.next is not None:
            length += 1
            node = node.next

        if length < n:
            return head

        location = length - n

        if location == 0:
            return head.next

        i, node = 1, head
        while i < location:
            node = node.next
            i += 1

        node.next = node.next.next
        return head


class SolutionOnce:
    """利用双指针遍历一次"""
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy_node = ListNode(-1)
        dummy_node.next = head
        node = self.find_from_end(dummy_node, n+1)
        node.next = node.next.next
        return dummy_node.next

    def find_from_end(self, head: ListNode, n: int):
        p1 = head
        for i in range(n):
            p1 = p1.next
        p2 = head
        while p1 is not None:
            p2 = p2.next
            p1 = p1.next
        return p2


if __name__ == '__main__':
    cases = [
        (create_linked_list(list(range(5))), 4, 1),
        (create_linked_list(list(range(5))), 1, 4),
        (create_linked_list(list(range(5))), 5, 0),
    ]
    solutions = (Solution(), SolutionOnce())

    for case in cases:
        for ss in solutions:
            result = [node.val for node in ss.removeNthFromEnd(case[0], case[1])]
            assert case[2] not in result
