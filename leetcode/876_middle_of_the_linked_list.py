"""Middle of the Linked List
Given the head of a singly linked list, return the middle of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1, 2, 3, 4, 5]
    Output: [3, 4, 5]
    Explanation: The middle node of the list is node 3.


Example 2:
    Input: head = [1, 2, 3, 4, 5, 6]
    Output: [4, 5, 6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the
    second one.

Constraints:
    * The number of nodes in the list is in the range [1, 100]
    * 1 <= Node.val < 100
"""
from typing import Optional

from utils.list import ListNode, create_linked_list


class Solution:
    """利用快慢双指针"""
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    cases = [
        (create_linked_list([1, 2, 3, 4, 5]), [3, 4, 5]),
        (create_linked_list([1, 2, 3, 4, 5, 6]), [4, 5, 6])
    ]
    solutions = (Solution(), )
    for case in cases:
        for solution in solutions:
            result = [node.val for node in solution.middleNode(case[0])]
            assert result == case[1]
