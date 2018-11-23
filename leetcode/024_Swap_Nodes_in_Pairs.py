"""Swap Nodes in Paris

Given a linked list, swap very twoo adjacent nodes and return its head.

Eample:

    1 -> 2 -> 3 -> 4

Output:

    2 -> 1 -> 4 -> 3

Note:

* Yor algorithm should use only constant extra space.
* You may not modify the values in the lists' nodes, only nodes itself may be changed.


Refer https://leetcode.com/problems/swap-nodes-in-pairs/
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 需要记录当前节点的前一个节点
        new, prev = None, None
        current = head
        while current is not None:
            node = current.next
            if node is None:
                if new is None:
                    new = current
                break
            current.next = node.next
            node.next = current
            if new is None:
                new = node
            if prev is not None:
                prev.next = node
            prev = current
            current = current.next
        return new

if __name__ == '__main__':
    cases = [
        generate_linked_list(8, 1),
        generate_linked_list(2, 1)
    ]

    solutions = [Solution]
    for case in cases:
        print('Input:', [node.val for node in iter_linked_list(case)])
        for solution in solutions:
            l = solution().swapPairs(copy.deepcopy(case))
            print('{}: {}'.format(solution.__name__, [node.val for node in iter_linked_list(l)]))
