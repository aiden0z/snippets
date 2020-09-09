""" Rotate List

Given a linked list, rotate the list to the right by k places,
where k is non-negative.

Example 1:

    Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL, k = 2
    Output: 4 -> 5 -> 1 -> 2 -> 3 -> NULL
    Explation:

    rotate 1 steps to the right: 5 -> 1 -> 2 -> 3 -> 4 -> NULL
    rotate 2 steps to the right: 4 -> 5 -> 1 -> 2 -> 3 -> NULL

Example 2:

    Input: 0 -> 1 -> 2 -> NULL, k = 4
    Output: 2 -> 0 -> 1 -> NULL
    Explanation:

    rotate 1 steps to the right: 2 -> 0-> 1-> NULL
    rotate 2 steps to the right: 1 -> 2-> 0-> NULL
    rotate 3 steps to the right: 0 -> 1-> 2-> NULL
    rotate 4 steps to the right: 2 -> 0-> 1-> NULL

"""

from typing import List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        values = [self.val]
        next = self.next
        while next is not None:
            values.append(next.val)
            next = next.next
        return '=>'.join(map(str, values))

    @classmethod
    def createList(cls, ints: List[int]) -> 'ListNode':
        head = cls(ints[0])
        if len(ints) == 1:
            return head

        node = head
        for i in ints[1:]:
            node.next = ListNode(i)
            node = node.next
        return head


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        if head.next is None:
            return head

        length = 1
        tail = head

        while tail.next is not None:
            tail = tail.next
            length += 1

        # create a cycle list
        tail.next = head

        i = length - k % length

        new_head = head
        while i > 0:
            new_head = new_head.next
            tail = tail.next
            i -= 1

        # break cycle list
        tail.next = None
        return new_head


if __name__ == '__main__':
    cases = [
        ((ListNode.createList([1, 2, 3, 4, 5]), 1), ListNode.createList([5, 1, 2, 3, 4])),
        ((ListNode.createList([1, 2, 3, 4, 5]), 2), ListNode.createList([4, 5, 1, 2, 3])),
        ((ListNode.createList([0, 1, 2]), 4), ListNode.createList([2, 0, 1])),
        ((ListNode.createList([0, 1, 2]), 3), ListNode.createList([0, 1, 2])),
        ((ListNode.createList([0, 1, 2]), 2), ListNode.createList([1, 2, 0])),
        ((ListNode.createList([0, 1, 2]), 1), ListNode.createList([2, 0, 1])),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            # print(S().rotateRight(case[0][0], case[0][1]).toString())
            # print(case[1].toString())
            assert S().rotateRight(case[0][0], case[0][1]).toString() == case[1].toString()
