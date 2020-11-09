class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # handle abnormal cases
        if head == None:
            return None

        # place holder
        ph = ListNode(val=0, next=head)
        done = ph

        while done.next is not None:
            if done.next.next is not None:
                # there are two nodes
                tmp1 = done.next
                tmp2 = done.next.next
                done.next = tmp2
                tmp2_next = tmp2.next
                tmp2.next = tmp1
                tmp1.next = tmp2_next
                done = tmp1
            else:
                # there is only one node
                break

        return ph.next
