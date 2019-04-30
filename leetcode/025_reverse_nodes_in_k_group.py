"""Reverse Nodes in K-Group


Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to length of the linked list. If the number of
nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1 -> 2 -> 3 -> 4 -> 5
For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5
For k = 3, you should return: 3 -> 2 -> 1 -> 4 -> 5

Note:

* Only constan extra memory is allowed.
* You may not alter the values in the list's nodes, only nodes itself may be changed.

"""
import copy


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
    """使用栈解法"""

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stack = []
        size = 0
        current = head
        dummy = ListNode("dummy")
        tmp = dummy

        while current is not None:
            stack.append(current)
            size += 1
            current = current.next
            if size == k:
                while size > 0:
                    tmp.next = stack.pop()
                    tmp = tmp.next
                    size -= 1

        while len(stack) > 0:
            tmp.next = stack.pop(0)
            tmp = tmp.next
        tmp.next = None
        return dummy.next


class SolutionRecursive:

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if k <= 1:
            return head
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
        return self.reverseHelper(head, k, count)

    def reverseHelper(self, head, k, count):
        target = k
        if count < k:
            return head
        curr_node = head
        next_node = head.next
        while k > 1:
            temp = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = temp
            k -= 1
        head.next = self.reverseHelper(next_node, target, count - target)
        return curr_node


if __name__ == '__main__':
    cases = [
        (generate_linked_list(9, 1), 1),
        (generate_linked_list(9, 1), 2),
        (generate_linked_list(9, 1), 3),
        (generate_linked_list(9, 1), 4),
        (generate_linked_list(9, 1), 7),
        (generate_linked_list(8, 1), 4),
    ]

    solutions = [Solution, SolutionRecursive]
    for case in cases:
        print('Input:', [node.val for node in iter_linked_list(case[0])], case[1])
        for solution in solutions:
            result = solution().reverseKGroup(copy.deepcopy(case[0]), case[1])
            print('{}: {}'.format(solution.__name__,
                                  [node.val for node in iter_linked_list(result)]))
