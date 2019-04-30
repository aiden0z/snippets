"""Add Two Numbers
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Refer https://leetcode.com/problems/add-two-numbers/description/
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_from_list(cls, l):
        head = cls(l[0])
        n = head
        for k in l[1:]:
            node = cls(k)
            n.next = node
            n = node
        return head

    def list(self):
        l = []
        node = self
        while True:
            l.append(node.val)
            if node.next is None:
                break
            node = node.next
        return l

    def integer(self):
        return int(''.join(map(str, self.list()[::-1])))

    def __str__(self):
        return ''.join(map(str, self.list()))


class Solution(object):
    """
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n))
    """

    def addTwoNumbers(self, l1, l2):
        dummpy_head = ListNode(0)
        p, q = l1, l2
        curr = dummpy_head
        carry = 0

        while (p is not None or q is not None):
            x = 0 if p is None else p.val
            y = 0 if q is None else q.val
            count = carry + x + y
            carry = count // 10
            curr.next = ListNode(count % 10)
            curr = curr.next

            if p is not None:
                p = p.next

            if q is not None:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)
        return dummpy_head.next


class SolutionComplex(object):

    def addTwoNumbers(self, l1, l2):
        head = l1
        tail = head
        i = 0
        while True:
            l1.val = l1.val + l2.val + i
            i = 0
            if l1.val >= 10:
                i = l1.val // 10
                l1.val = l1.val % 10
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                tail = l1
            elif l1.next is None or l2.next is None:
                break
        if l1.next is None and l2.next is not None:
            l1.next = l2.next
            l2.next = None
        if l2.next is None:
            while l1.next is not None:
                l1 = l1.next
                tail = l1
                l1.val += i
                i = 0
                if l1.val >= 10:
                    i = l1.val // 10
                    l1.val = l1.val % 10
        if i > 0:
            tail.next = ListNode(i)
        return head


class SolutionConvert(object):

    def list_to_integer(self, head):
        l = []
        while True:
            l.append(head.val)
            if head.next is None:
                break
            head = head.next
        return int(''.join(map(str, l[::-1])))

    def integer_to_list(self, i):

        head = None
        node = None
        while i >= 10:
            if head is None:
                head = node = ListNode(i % 10)
            else:
                node.next = ListNode(i % 10)
                node = node.next
            i = i // 10

        if node is None:
            return ListNode(i)
        else:
            node.next = ListNode(i)
            return head

    def addTwoNumbers(self, l1, l2):
        i1 = self.list_to_integer(l1)
        i2 = self.list_to_integer(l2)
        return self.integer_to_list(i1 + i2)


if __name__ == '__main__':
    cases = [(([5, 2, 5], [7, 1, 6]), [2, 4, 1, 1]), (([2, 4, 3], [5, 6, 4]), [7, 0, 8])]

    for case in cases:
        l1 = ListNode.create_from_list(case[0][0])
        l2 = ListNode.create_from_list(case[0][1])

        for s in (Solution(), SolutionComplex(), SolutionConvert()):
            s.addTwoNumbers(l1, l2).list() == case[1]
