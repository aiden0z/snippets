"""Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2.

After removing the second node from the end, the linked list becomes 1 -> 2 -> 3 ->5

Note:

Given n will always be valid.

Refer https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""


def generate_linked_list(n):
    assert n > 1
    head = ListNode(n)
    node = head
    for i in range(n - 1, 0, -1):
        next_node = ListNode(i)
        node.next = next_node
        next_node.prev = node
        node = node.next
    return head


def check_exist(head, val):
    while True:
        if head.val == val:
            return True
        if head.next is not None:
            head = head.next
        else:
            break
    return False


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class Solution:
    """ 单向链表只能遍历一次后才能知道其长度
    """

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


if __name__ == '__main__':
    cases = [(generate_linked_list(5), 5), (generate_linked_list(5), 6),
             (generate_linked_list(5), 3)]
    solutions = [Solution]

    for case in cases:
        for solution in solutions:
            assert not check_exist(solution().removeNthFromEnd(case[0], case[1]), case[1])
