from typing import List, Optional


class ListNode:

    def __init__(self, value):
        self.val = value
        self.next = None


def create_linked_list(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return
    head = ListNode(nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next
    return head


def iter_linked_list(head: ListNode):
    node = head
    while node is not None:
        yield node
        node = node.next
