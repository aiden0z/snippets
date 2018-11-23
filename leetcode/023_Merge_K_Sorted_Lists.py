"""Merge k Sorted Lists

Merge k sorted linkd lists and return it as one sorted list. Analyze and describe its complexity.

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
    """迭代递归解法"""

    def mergeTwoLists(self, l1, l2):
        if(l1 == None): return l2
        if(l2 == None): return l1
        
        if(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists):
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

    def mergeTwoLists(self, l1, l2):
        if(l1 == None): return l2
        if(l2 == None): return l1
        
        if(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) ==0:
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
    def addToList(lists):
        values = []
        for node in lists:
            current = node
            while current != None:
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
                current=current.next
        return head


if __name__ == '__main__':
    cases = [
        [generate_linked_list(3, 2), generate_linked_list(6, 2), generate_linked_list(6, 3)],
        [generate_linked_list(7, 2), generate_linked_list(8, 2), generate_linked_list(6, 3)],
    ]

    solutions = [Solution, SolutionMergeRecursive, SolutionSimple ]
    for case in cases:
        inputs = []
        for node in case:
            inputs.append('{}'.format([n.val for n in iter_linked_list(node)]))
        print('Input:', ', '.join(inputs))
        for solution in solutions:
            l = solution().mergeKLists(copy.deepcopy(case))
            print('{}: {}'.format(solution.__name__, [node.val for node in iter_linked_list(l)]))
