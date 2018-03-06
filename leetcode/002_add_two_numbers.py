# coding:utf-8

"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Refer: https://leetcode.com/problems/add-two-numbers/description/
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def init_from_list(cls, l):
        head = cls(l[0])
        n = head
        for k in l[1:]:
            node = cls(k)
            n.next = node
            n = node
        return head

    def __str__(self):
        result = ""
        n = self
        while True:
            result += str(n.val)
            if n.next is None:
                break
            else:
                n = n.next
        return result


class Solution(object):
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

if __name__ == '__main__':
    l1 = ListNode.init_from_list([5])
    print(l1)
    l2 = ListNode.init_from_list([5])
    print(l2)
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
