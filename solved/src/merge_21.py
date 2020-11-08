# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr_l1 = l1
        curr_l2 = l2
        placeholder = ListNode(0)
        curr_result = placeholder

        while curr_l1 and curr_l2:
            if curr_l1.val <= curr_l2.val:
                curr_result.next = ListNode(curr_l1.val)
                curr_l1 = curr_l1.next
            else:
                curr_result.next = ListNode(curr_l2.val)
                curr_l2 = curr_l2.next
            curr_result = curr_result.next

        if curr_l1:
            curr_result.next = curr_l1
        elif curr_l2:
            curr_result.next = curr_l2
        else:
            return None

        return placeholder.next

